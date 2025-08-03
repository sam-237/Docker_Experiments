# Docker Basics: Hello World Project 🐳🐍

Welcome to your first Docker project! In this guide, we will walk through the steps to create a simple Python application that prints `"Hello World"` and deploy it using Docker.

This project helps you understand the **basics of Docker**, including building and running containers.

---

## 📋 Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Python](https://www.python.org/downloads/)
- [Docker Desktop](https://docs.docker.com/desktop/)

---

## 🐍 Step 1: Create the Python Application

Create a file named `app.py`:

```python
# app.py
print("Hello World! 🐳")
```

---

## 🛠️ Step 2: Install Docker and Python

Install Docker and Python if not already done:

- [Docker Desktop Installation Guide](https://docs.docker.com/desktop/install/)
- [Python Installation Guide](https://www.python.org/downloads/)

---

## ✅ Step 3: Verify Installations

Run these commands in your terminal:

```bash
docker --version
# Example: Docker version 20.10.17, build 100c701

python --version
# Example: Python 3.9.7
```

---

## 📄 Step 4: Create a Dockerfile

Create a file named `Dockerfile` in the same folder:

```dockerfile
# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy contents to /app
COPY . /app

# Command to run the app
CMD ["python", "app.py"]
```

---

## 🏗️ Step 5: Build the Docker Image

Run the following command from the folder containing your `Dockerfile` and `app.py`:

```bash
docker build -t hello-world-app .
```

---

## 🖼️ Step 6: Verify the Image

Check if the image was created:

```bash
docker images
```

Expected output:

```
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
hello-world-app     latest    abc123def456   10 seconds ago   123MB
```

---

## 🚀 Step 7: Run the Docker Container

Run your app in a container:

```bash
docker run hello-world-app
```

Expected output:

```
Hello World! 🐳
```

---

## 📚 Documentation

- [Docker Documentation](https://docs.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Python Docs](https://docs.python.org/3/)

---

## 🎉 Conclusion

You’ve successfully created your first Dockerized Python app! This was your first step into the world of containerization.

Happy Coding! 🚀🐳
