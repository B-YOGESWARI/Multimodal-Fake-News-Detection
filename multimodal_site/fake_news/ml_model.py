import torch
from transformers import BertTokenizer, BertModel
from torchvision import models, transforms
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity

# Load BERT
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
bert = BertModel.from_pretrained("bert-base-uncased")
bert.eval()

# Load CNN
cnn = models.resnet18(pretrained=True)
cnn.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict_fake_news(text, image_path):
    # ---- TEXT EMBEDDING ----
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        text_emb = bert(**inputs).last_hidden_state.mean(dim=1)

    # ---- IMAGE EMBEDDING ----
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        img_emb = cnn(image)

    # Match dimensions
    img_emb = img_emb[:, :768]

    # ---- SIMILARITY ----
    score = cosine_similarity(text_emb.numpy(), img_emb.numpy())[0][0]
    THRESHOLD = 0.25 # adjustable value
    return "REAL NEWS" if THRESHOLD >= 0.25 else "FAKE NEWS"