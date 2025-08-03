# 🧪 Experiment Portfolio: 6 Projects with Docker and Streamlit 🚀

Welcome to my experiment portfolio! This repository showcases 6 unique projects that demonstrate my growing proficiency with Docker, Streamlit, Python apps, volumes, and containerization best practices.

Each project below includes the description, code, and deployment steps right here in this single README for easy reference and copying.

---

## 📑 Table of Contents

1. [Docker Basics: Hello World 🐳](#1-docker-basics-hello-world-)
2. [Streamlit App Using Docker 🐍](#2-streamlit-app-using-docker-)
3. [Streamlit ML Classification App 🤖](#3-streamlit-ml-classification-app-)
4. [Docker Volume with Logging 💾](#4-docker-volume-with-logging-)
5. [Streamlit + Evidently for ML Monitoring 📊](#5-streamlit--evidently-for-ml-monitoring-)
6. [Streamlit App on AWS EC2 ☁️](#6-streamlit-app-on-aws-ec2-)

---

## 1. Docker Basics: Hello World 🐳

**Description**

> A minimal Python script to get started with Docker. It prints a greeting from inside the container.

**Code**

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
CMD ["python", "app.py"]
```

```python
print("Hello, World from Docker! 🐳")
```

**Deployment**

```bash
docker build -t hello-world .
docker run hello-world
```

---

## 2. Streamlit App Using Docker 🐍

**Description**

> A basic Streamlit app running inside Docker. Prompts the user for their name and displays a message.

**Code**

```python
import streamlit as st

st.title("My First App")
st.write("Hello How are you")
name = st.text_input("What is your name")
if name:
    st.success(f"Nice to meet you , {name}!")
```

```Dockerfile
FROM python:3-slim
WORKDIR /app
COPY pythonapp.py pythonapp.py
RUN pip install streamlit
EXPOSE 8501
CMD ["streamlit", "run", "pythonapp.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Deployment**

```bash
docker build -t streamlit-basic .
docker run -p 8501:8501 streamlit-basic
```

---

## 3. Streamlit ML Classification App 🤖

**Description**

> A full-featured Streamlit app that classifies mushrooms as edible or poisonous. Users can choose between SVM, Logistic Regression, and Random Forest classifiers.

**Highlights**

- Model training, evaluation, and visualization
- Caching for performance
- Interactive sidebar controls

**Dockerfile**

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
COPY mushrooms.csv /app
COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

**Deployment**

```bash
docker build -t mushroom-classifier .
docker run -p 8501:8501 mushroom-classifier
```

---

## 4. Docker Volume with Logging 💾

**Description**

> Demonstrates persistent logging using Docker volumes. The Python script logs timestamps to a shared volume every 5 seconds.

**Code**

```python
import time
import logging

logging.basicConfig(filename='/logs/app.log', level=logging.INFO)
while True:
    logging.info(f'Logging a new entry at {time.ctime()}')
    time.sleep(5)
```

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app.py /app/
RUN mkdir -p /logs
CMD ["python", "app.py"]
```

**Deployment**

```bash
docker build -t volume-logger .
docker run -v logs:/logs volume-logger
```

---

## 5. Streamlit + Evidently for ML Monitoring 📊

**Description**

> Uses Evidently and Streamlit to display monitoring dashboards. Helps detect data drift and visualize performance metrics.

**Highlights**

- Data drift detection
- Interactive charts with Streamlit

**Commands**

```bash
pip install streamlit evidently pandas
streamlit run app.py
```

**Use Cases**

- Monitor model accuracy
- Analyze input feature drift over time

---

## 6. Streamlit App on AWS EC2 ☁️

**Description**

> Shows how to deploy a Streamlit Docker app on an AWS EC2 instance. Covers SSH, Docker installation, and remote hosting.

**Deployment Steps**

```bash
# Connect to EC2
ssh -i key.pem ec2-user@your-public-ip

# Install Docker
sudo yum update -y
sudo yum install docker
sudo service docker start

# Upload code and run
docker build -t my-streamlit-app .
docker run -p 8501:8501 my-streamlit-app
```

---

🎉 **Thanks for exploring my Docker experiments!** Each project was designed to learn, apply, and grow confidence with containers, Python apps, and ML deployments.
