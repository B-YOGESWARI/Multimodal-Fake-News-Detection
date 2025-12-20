import torch
import pandas as pd
from transformers import BertTokenizer, BertModel
from torchvision import models, transforms
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity

# =============================
# LOAD DATASET
# =============================
data = pd.read_csv("data/news.csv")

print("Total News Samples:", len(data))
print("=" * 50)

# =============================
# LOAD MODELS ONCE
# =============================

# BERT for text
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
bert_model = BertModel.from_pretrained("bert-base-uncased")
bert_model.eval()

# CNN for image
cnn_model = models.resnet18(pretrained=True)
cnn_model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# =============================
# PROCESS EACH NEWS ITEM
# =============================
for index in range(len(data)):
    print(f"\nTesting Sample Index: {index}")
    print("-" * 40)

    text = data["text"][index]
    image_name = data["image"][index]

    print("News Text:", text)
    print("Image File:", image_name)

    # -------------------------
    # TEXT EMBEDDING (BERT)
    # -------------------------
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        text_output = bert_model(**inputs)

    text_embedding = text_output.last_hidden_state.mean(dim=1)

    # -------------------------
    # IMAGE EMBEDDING (CNN)
    # -------------------------
    img = Image.open(f"data/{image_name}").convert("RGB")
    img = transform(img).unsqueeze(0)

    with torch.no_grad():
        image_embedding = cnn_model(img)

    # Reduce image embedding from 1000 → 768
    image_embedding = image_embedding[:, :768]

    # -------------------------
    # IMAGE–TEXT SIMILARITY
    # -------------------------
    similarity = cosine_similarity(
        text_embedding.numpy(),
        image_embedding.numpy()
    )

    score = similarity[0][0]
    print("Cosine Similarity Score:", round(score, 3))

    # -------------------------
    # FINAL PREDICTION
    # -------------------------
    if score < 0.2:
        print("Prediction: FAKE NEWS (Image does not match text)")
    else:
        print("Prediction: REAL NEWS (Image matches text)")

print("\n=== Testing Completed Successfully ===")