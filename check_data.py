import pickle

with open("asl_landmarks.pkl", "rb") as f:
    data = pickle.load(f)

print(len(data[0]))  # Number of samples in X
print(len(data[1]))  # Number of samples in y
