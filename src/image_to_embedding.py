import torch
from torchvision import models, transforms
from PIL import Image

# Load pre-trained ResNet model
model = models.resnet18(pretrained=True)
model.eval()

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# Load image from correct path
img = Image.open("data/img1.jpg").convert("RGB")
img = transform(img).unsqueeze(0)

# Extract image features
with torch.no_grad():
    image_embedding = model(img)

print("Image embedding shape:", image_embedding.shape)