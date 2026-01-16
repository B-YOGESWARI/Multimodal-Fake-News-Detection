import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re

# Load tokenizer
with open("model/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load model
model = tf.keras.models.load_model("model/model.h5")

# Text cleaning function (same as training)
def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    return text

# Take input from user
news = input("Enter news text: ")

# Preprocess
news = clean_text(news)
seq = tokenizer.texts_to_sequences([news])
pad = pad_sequences(seq, maxlen=200)

# Prediction
prediction = model.predict(pad)[0][0]

# Output
if prediction > 0.5:
    print("\nPrediction: REAL NEWS ✅")
else:
    print("\nPrediction: FAKE NEWS ❌")