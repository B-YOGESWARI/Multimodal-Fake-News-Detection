from PIL import Image
import matplotlib.pyplot as plt

img = Image.open(
    r"C:\Users\Admin\Desktop\Multimodal_Fake_News_Project\data\img1.jpg"
)

plt.imshow(img)
plt.axis("off")
plt.title("Sample News Image")
plt.show()