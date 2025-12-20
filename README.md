**📰📰 Multimodal Fake News Detection using Image–Text Similarity.**

Fake news has become a serious problem in today’s digital world, especially when misleading images are shared along with false information. To address this issue, I developed a Multimodal Fake News Detection system that analyzes both news text and its related image instead of relying on text alone.



This project works by understanding the meaning of the news content using natural language processing and comparing it with the information extracted from the uploaded image. If the image and text do not logically match, the system identifies the news as fake; otherwise, it is classified as real.



The application is built using Django, providing features like user registration, login, admin-controlled user activation, prediction history, and secure sessions. By combining machine learning with a user-friendly web interface, this project demonstrates how multimodal learning can improve the accuracy of fake news detection.



This project was developed as part of my final year academic work and helped me gain hands-on experience in machine learning, deep learning models, and full-stack development.



This project focuses on detecting fake news by analyzing both text content and associated images.

Unlike traditional approaches that rely only on text, this system uses a \*\*multimodal approach\*\* to verify whether the image and text are semantically related.



If the image does not match the given news content, the system predicts the news as \*\*Fake\*\*; otherwise, it is classified as \*\*Real\*\*.



---



**🚀 Features**

\- User Registration \& Login

\- Admin Activation Control

\- Image + Text based Fake News Detection

\- Multimodal Embedding Comparison

\- Prediction History Tracking

\- Django-based Web Interface

\- Secure Session Handling



---



**## 🧠 Technologies Used**

\- \*\*Python\*\*

\- \*\*Django Framework\*\*

\- \*\*BERT (Text Embeddings)\*\*

\- \*\*ResNet18 (Image Embeddings)\*\*

\- \*\*PyTorch\*\*

\- \*\*Scikit-learn\*\*

\- \*\*HTML, CSS\*\*

\- \*\*SQLite Database\*\*



---



**## 🔍 Methodology**

1\. Text input is converted into embeddings using \*\*BERT\*\*

2\. Image input is converted into embeddings using \*\*ResNet18\*\*

3\. Cosine similarity is calculated between text and image embeddings

4\. Based on similarity score:

   - Low similarity → Fake News

   - High similarity → Real News



---



**## 📂 Project Structure**

Multimodal\_Fake\_News\_Project/

├── data/

│ ├── img1.jpg

│ ├── img2.jpg

│ └── news.csv

├── fake\_news/

│ ├── views.py

│ ├── models.py

│ ├── ml\_model.py

│ ├── urls.py

│ └── templates/

├── multimodal\_site/

│ ├── settings.py

│ ├── urls.py

│ └── wsgi.py

├── manage.py

├── README.md

└── requirements.txt



**---**



**## ▶️ How to Run the Project**

1\. Create a virtual environment

2\. Install required dependencies

3\. Run migrations

4\. Start the Django server

5\. Open the application in your browser



Sample images are provided only for \*\*demo purposes\*\*. Users can upload images dynamically during prediction.



**---**



**## 👩‍💻 Developed By**

\*\*B. Yogeswari\*\*

Final Year B.Tech (CSE)

Interested in Machine Learning, AI, and Full Stack Development



**---**



**## 📌 Note**

This project is developed for \*\*academic and learning purposes\*\* and demonstrates how combining image and text analysis can improve fake news detection accuracy.
