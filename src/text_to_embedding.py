import pandas as pd
import torch
from transformers import BertTokenizer, BertModel

# Load dataset
data = pd.read_csv("data/news.csv")

# Load BERT
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")
model.eval()

# Take one sample text
text = data["text"][0]

# Convert text to tokens
inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=128
)

# Get embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Mean pooling
text_embedding = outputs.last_hidden_state.mean(dim=1)

print("Text:", text)
print("Embedding shape:", text_embedding.shape)