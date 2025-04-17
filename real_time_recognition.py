import cv2
import mediapipe as mp
import numpy as np
import pickle
import os

# 🔹 Load trained model
MODEL_PATH = r"C:\Users\khush\Sem 6\HandSpeak\ASL hand recognition\src\asl_model.pkl"
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# 🔹 Correct dataset path (Matching preprocess.py)
DATASET_PATH = r"C:\Users\khush\Sem 6\HandSpeak\ASL hand recognition\dataset\asl_alphabet_train\asl_alphabet_train"

# Get gesture labels (A-Z folders)
labels = sorted(os.listdir(DATASET_PATH))

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Start webcam capture
cap = cv2.VideoCapture(0)

print("🎥 Starting real-time ASL recognition. Press 'q' to exit.")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("❌ ERROR: Failed to capture image")
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)

            # Convert to numpy array and reshape for prediction
            landmarks = np.array(landmarks).reshape(1, -1)

            # Predict gesture
            prediction = model.predict(landmarks)
            predicted_label = prediction[0]

            # Display label on screen
            cv2.putText(frame, f"Prediction: {predicted_label}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("ASL Hand Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
