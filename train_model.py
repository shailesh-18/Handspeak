from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

# Load preprocessed dataset
LANDMARKS_PATH = "asl_landmarks.pkl"

# Ensure the file exists before loading
if not os.path.exists(LANDMARKS_PATH):
    raise FileNotFoundError(f"❌ Error: {LANDMARKS_PATH} not found! Run preprocess.py first.")

with open(LANDMARKS_PATH, "rb") as f:
    X, y = pickle.load(f)

# Ensure dataset is not empty
if len(X) == 0 or len(y) == 0:
    raise ValueError("❌ Dataset is empty. Ensure preprocess.py generated valid data.")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained successfully! Accuracy: {accuracy * 100:.2f}%")

# Save trained model
MODEL_PATH = "asl_model.pkl"
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model saved as {MODEL_PATH}")
