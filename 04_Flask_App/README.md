🍄 Binary Classification with Streamlit + Docker
This project demonstrates how to deploy a machine learning binary classification model using Streamlit inside a Docker container. The app predicts whether mushrooms are edible or poisonous based on various features.

📋 Prerequisites
Make sure the following are installed:

Docker 👉 Install Docker

Internet connection (to download base image and Python packages)

🗂️ Project Structure
bash
Copy
Edit
04_Streamlit_Classifier/
├── app.py              # Streamlit app (mushroom classifier)
├── mushrooms.csv       # Dataset used for training
├── Dockerfile          # Docker instructions
├── requirements.txt    # Python dependencies
└── README.md           # You're here
🧠 App Features
Train and compare SVM, Logistic Regression, and Random Forest

Tune hyperparameters via sidebar

Plot:

Confusion Matrix

ROC Curve

Precision-Recall Curve

Show raw dataset with a checkbox

📦 Step-by-Step Setup
📌 Step 1: Dockerfile
Here's the Dockerfile used:

Dockerfile
Copy
Edit
FROM python:3.9-slim

WORKDIR /app

COPY app.py /app
COPY mushrooms.csv /app
COPY requirements.txt /app

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
📦 Step 2: requirements.txt
Make sure your requirements.txt includes:

txt
Copy
Edit
streamlit
pandas
scikit-learn
matplotlib
You can generate it using:

bash
Copy
Edit
pip freeze > requirements.txt
🏗️ Step 3: Build Docker Image
Navigate to your project folder and run:

bash
Copy
Edit
docker build -t streamlit-mushroom .
🚀 Step 4: Run the Container
bash
Copy
Edit
docker run -p 8501:8501 streamlit-mushroom
Then, open your browser and go to:

arduino
Copy
Edit
http://localhost:8501
You’ll see the full interactive Streamlit UI!

🖼️ Screenshot
(Optional: Add a screenshot of the app in action)

🧪 Bonus Tips
⏱️ Modify File Without Rebuilding (Dev Mode)
Mount local files instead of rebuilding image every time:

bash
Copy
Edit
docker run -p 8501:8501 -v $(pwd):/app streamlit-mushroom
📚 References
Streamlit Docs

scikit-learn Docs

Dockerizing Streamlit

🎉 Conclusion
You've now deployed a full-featured ML classifier inside a Docker container using Streamlit.
Play around with classifiers, tweak hyperparameters, and visualize results — all from your browser! 🧠📊

Keep building! Every project like this sharpens your real-world ML + DevOps skills 🚀