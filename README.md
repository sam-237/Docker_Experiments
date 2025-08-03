# Docker_Experiments
A collection of beginner-to-intermediate Docker experiments with step-by-step instructions, showcasing containerization of Python apps, MySQL, Streamlit, and more.

🧪 Experiment Portfolio: 6 Projects with Docker and Streamlit 🚀

Welcome to my experiment portfolio! This repository showcases 6 unique projects that demonstrate my growing proficiency with Docker, Streamlit, Python apps, volumes, and containerization best practices.

Each project folder contains its own README.md with detailed instructions, code, and deployment steps. This summary gives an overview of each.

Table of Contents 📑

Docker Basics: Hello World 🐳

Streamlit App Using Docker 🐍

Streamlit ML Classification App 🤖

Docker Volume with Logging 💾

Streamlit + Evidently for ML Monitoring 📊

Streamlit App on AWS EC2 ☁️

1. Docker Basics: Hello World 🐳

Description

A minimal Python script to get started with Docker. It prints a greeting from inside the container.

Code

FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
CMD ["python", "app.py"]

print("Hello, World from Docker! 🐳")

Deployment

docker build -t hello-world .
docker run hello-world

2. Streamlit App Using Docker 🐍

Description

A basic Streamlit app running inside Docker. Prompts the user for their name and displays a message.

Code

import streamlit as st
st.title("My First App")
st.write("Hello How are you")
name = st.text_input("What is your name")
if name:
    st.success(f"Nice to meet you , {name}!")

FROM python:3-slim
WORKDIR /app
COPY pythonapp.py pythonapp.py
RUN pip install streamlit
EXPOSE 8501
CMD ["streamlit", "run", "pythonapp.py", "--server.port=8501", "--server.address=0.0.0.0"]

Deployment

docker build -t streamlit-basic .
docker run -p 8501:8501 streamlit-basic

3. Streamlit ML Classification App 🤖

Description

A full-featured Streamlit app that classifies mushrooms as edible or poisonous. Users can choose between SVM, Logistic Regression, and Random Forest classifiers.

Highlights

Model training, evaluation, and visualization

Caching for performance

Interactive sidebar controls

Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
COPY mushrooms.csv /app
COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

Deployment

docker build -t mushroom-classifier .
docker run -p 8501:8501 mushroom-classifier

4. Docker Volume with Logging 💾

Description

Demonstrates persistent logging using Docker volumes. The Python script logs timestamps to a shared volume every 5 seconds.

Code

import time
import logging
logging.basicConfig(filename='/logs/app.log', level=logging.INFO)
while True:
    logging.info(f'Logging a new entry at {time.ctime()}')
    time.sleep(5)

FROM python:3.9-slim
WORKDIR /app
COPY app.py /app/
RUN mkdir -p /logs
CMD ["python", "app.py"]

Deployment

docker build -t volume-logger .
docker run -v logs:/logs volume-logger

5. Streamlit + Evidently for ML Monitoring 📊

Description

Uses Evidently and Streamlit to display monitoring dashboards. Helps detect data drift and visualize performance metrics.

Highlights

Data drift detection

Interactive charts with Streamlit

Commands

pip install streamlit evidently pandas
streamlit run app.py

Use Cases

Monitor model accuracy

Analyze input feature drift over time

6. Streamlit App on AWS EC2 ☁️

Description

Shows how to deploy a Streamlit Docker app on an AWS EC2 instance. Covers SSH, Docker installation, and remote hosting.

Deployment Steps

# Connect to EC2
ssh -i key.pem ec2-user@your-public-ip

# Install Docker
sudo yum update -y
sudo yum install docker
sudo service docker start

# Upload code and run
docker build -t my-streamlit-app .
docker run -p 8501:8501 my-streamlit-app

🎉 Thanks for exploring my Docker experiments! Each project was designed to learn, apply, and grow confidence with containers, Python apps, and ML deployments. For detailed walkthroughs, see the individual folders!

