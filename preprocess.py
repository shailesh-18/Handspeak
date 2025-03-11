import cv2
import mediapipe as mp
import numpy as np
import os
import pickle
import warnings


os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_LITE_DISABLE_XNNPACK"] = "1"
warnings.filterwarnings("ignore", category=UserWarning)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.5)  # Increased confidence
mp_draw = mp.solutions.drawing_utils


DATASET_PATH = r"C:\Users\khush\Sem 6\HandSpeak\ASL hand recognition\dataset\asl_alphabet_train\asl_alphabet_train"

# Ensure the dataset path exists
if not os.path.exists(DATASET_PATH):
    print(f"❌ Error: Dataset path not found: {DATASET_PATH}")
    exit()

# Get gesture labels (A-Z folders)
labels = [folder for folder in sorted(os.listdir(DATASET_PATH)) if os.path.isdir(os.path.join(DATASET_PATH, folder))]
print(f"📂 Found {len(labels)} gesture classes: {labels}")

# Prepare dataset
X = []  # Features (hand landmarks)
y = []  # Labels (gesture classes)
total_images = 0  # Count total processed images

for label in labels:
    label_path = os.path.join(DATASET_PATH, label)

    for img_name in os.listdir(label_path):
        img_path = os.path.join(label_path, img_name)

        # 🛠 Ensure file is an image
        if not img_name.lower().endswith((".png", ".jpg", ".jpeg")):
            continue  # Skip non-image files
        
        img = cv2.imread(img_path)
        if img is None:
            print(f"❌ ERROR: Unable to read image {img_path}, skipping...")
            continue

        # Resize image to improve hand detection
        img_rgb = cv2.resize(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), (640, 480))

        # Process image for hand landmarks
        result = hands.process(img_rgb)

        # Debugging: Check if hands are detected
        if result.multi_hand_landmarks:
            print(f"✅ Hand detected in {img_name}")
            total_images += 1
            for hand_landmarks in result.multi_hand_landmarks:
                landmarks = []
                for lm in hand_landmarks.landmark:
                    landmarks.append(lm.x)
                    landmarks.append(lm.y)

                X.append(landmarks)
                y.append(label)
        else:
            print(f"⚠️ No hands detected in {img_name}, skipping...")

# Convert to numpy arrays
X = np.array(X)
y = np.array(y)

# Check if dataset is empty
if len(X) == 0 or len(y) == 0:
    print("❌ ERROR: No valid data found. Check dataset images and preprocessing steps.")
    exit()

# Save preprocessed data
pkl_path = os.path.join(os.path.dirname(__file__), "asl_landmarks.pkl")  # Save in the same directory as script
with open(pkl_path, "wb") as f:
    pickle.dump((X, y), f)

print(f"✅ Dataset processed and saved successfully! ({pkl_path})")
print(f"📊 Total processed images: {total_images}")
