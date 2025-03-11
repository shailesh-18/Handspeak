import cv2
import mediapipe as mp
import numpy as np
import pickle
import os

# Load trained model
with open("asl_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load labels
DATASET_PATH = "asl_alphabet_train"
labels = sorted(os.listdir(DATASET_PATH))

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Start capturing video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    h, w, _ = frame.shape
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)
            
            # Predict gesture
            landmarks = np.array(landmarks).reshape(1, -1)
            prediction = model.predict(landmarks)[0]
            
            # Draw rectangle and label
            cv2.putText(frame, prediction, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display output
    cv2.imshow("ASL Gesture Recognition", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
