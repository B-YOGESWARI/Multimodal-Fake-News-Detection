import torch
import clip
from PIL import Image

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def predict_fake_news(text, image_path):
    # Prepare inputs
    image = preprocess(Image.open(image_path).convert("RGB")).unsqueeze(0).to(device)
    text_input = clip.tokenize([text]).to(device)

    with torch.no_grad():
        image_features = model.encode_image(image)
        text_features = model.encode_text(text_input)

        # Normalize
        image_features /= image_features.norm(dim=-1, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)

        similarity = (image_features @ text_features.T).item()

    # 🔥 EXACT LOGIC
    if similarity > 0.25:
        return "REAL NEWS ✅ (Image matches text)"
    else:
        return "FAKE NEWS ❌ (Image does not match text)"