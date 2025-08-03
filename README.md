# 🎢 Experiment Portfolio: 6 Projects with Docker and Streamlit 🚀

Welcome to my Docker experiment portfolio! This repository contains 6 practical projects demonstrating my skills with Docker, Python, Streamlit, MySQL, Flask, and containerized logging systems. Each project is explained in detail below with description, code, and deployment instructions.

---

## 📁 Table of Contents

1. [Docker Basics: Hello World 🐫](#1-docker-basics-hello-world-)
2. [Basic Streamlit App 🐍](#2-basic-streamlit-app-)
3. [MySQL with Docker 💄](#3-mysql-with-docker-)
4. [Flask Mushroom Classification App 🍄](#4-flask-mushroom-classification-app-)
5. [Streamlit Spiral Visualizer 🔀](#5-streamlit-spiral-visualizer-)
6. [Docker Volume Time Logger 📀](#6-docker-volume-time-logger-)

---

## 1. Docker Basics: Hello World 🐫

A minimal Python script that prints "Hello World!" inside a Docker container.

### `app.py`
```python
print("Hello, World from Docker! 🐫")
```

### `Dockerfile`
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
CMD ["python", "app.py"]
```

### Deployment
```bash
docker build -t hello-world-app .
docker run hello-world-app
```

---

## 2. Basic Streamlit App 🐍

A Streamlit app that greets users and takes user input inside a Docker container.

### `pythonapp.py`
```python
import streamlit as st
st.title("My First App")
st.write("Hello How are you")
name = st.text_input("What is your name")
if name:
    st.success(f"Nice to meet you , {name}!")
```

### `Dockerfile`
```dockerfile
FROM python:3-slim
WORKDIR /app
COPY pythonapp.py pythonapp.py
RUN pip install streamlit
EXPOSE 8501
CMD ["streamlit", "run", "pythonapp.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Deployment
```bash
docker build -t streamlit-input-app .
docker run -p 8501:8501 streamlit-input-app
```

---

## 3. MySQL with Docker 💄

Deploys a MySQL container initialized with student data.

### `init.sql`
```sql
CREATE DATABASE student;
USE student;
CREATE TABLE students (
    StudentID INT NOT NULL AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    Surname VARCHAR(100) NOT NULL,
    PRIMARY KEY (StudentID)
);
INSERT INTO students (FirstName, Surname)
VALUES ("Dhruv", "Kaushik"), ("Mehak", "Dhiman"), ("Sambit", "Majumder"), ("Saurabh", "Singh");
```

### `Dockerfile`
```dockerfile
FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=root
COPY init.sql /docker-entrypoint-initdb.d/
```

### Deployment
```bash
docker build -t mysql_db .
docker run -d --name mysql_container mysql_db
docker exec -it mysql_container mysql -u root -p
```

---

## 4. Flask Mushroom Classification App 🍄

A Streamlit-based ML app that classifies mushrooms as edible or poisonous.

### `app.py` (simplified overview)
```python
# Uses pandas, scikit-learn, streamlit to build a classification UI.
# Supports SVM, Logistic Regression, Random Forest.
# Shows metrics like accuracy, precision, recall.
```

### `Dockerfile`
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
COPY mushrooms.csv /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Deployment
```bash
docker build -t mushroom-flask-app .
docker run -p 8501:8501 mushroom-flask-app
```

---

## 5. Streamlit Spiral Visualizer 🔀

This Streamlit app generates and visualizes spiral patterns using matplotlib.

### `Dockerfile`
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "spiral.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Deployment
```bash
docker build -t spiral-app .
docker run -p 8501:8501 spiral-app
```

---

## 6. Docker Volume Time Logger 📀

Logs timestamps every 5 seconds into a persistent Docker volume.

### `app.py`
```python
import time
import logging
logging.basicConfig(filename='/logs/app.log', level=logging.INFO)
while True:
    logging.info(f'Logging a new entry at {time.ctime()}')
    time.sleep(5)
```

### `Dockerfile`
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY app.py /app/
RUN mkdir -p /logs
CMD ["python", "app.py"]
```

### Deployment
```bash
docker build -t volume-logger .
docker run -v logs:/logs volume-logger
```

---

🎉 **Thanks for checking out my Docker projects!**

Each project is built to reinforce real-world containerization skills with Python and Docker. Feel free to clone, explore, or contribute!

Happy coding! 🚀
