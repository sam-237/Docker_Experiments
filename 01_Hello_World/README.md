Docker Basics: Hello World Project 🐳🐍
Welcome to your first Docker project! In this guide, we will walk through the steps to create a simple Python application that prints "Hello World" and deploy it using Docker. This project will help you understand the basics of Docker, including building and running containers.

Prerequisites 📋
Before we begin, ensure you have the following installed on your system:

Docker: A platform for developing, shipping, and running applications in containers.
Python: A programming language used to write the application.
Docker Desktop: A tool to manage Docker containers on your local machine.
Step 1: Create the Python Application 🐍
First, let's create a simple Python script that prints "Hello World".

Create a file named app.py and add the following code:
# app.py
print("Hello World! 🐳")
Step 2: Install Docker and Python 🛠️
Install Docker
Download and install Docker Desktop from the official Docker website. Once installed, start Docker Desktop and ensure it is running.

Install Python. Download and install Python from the official Python website.
Step 3: Verify Installations ✅
Before proceeding, let's verify that Docker and Python are installed correctly.

Check Docker Version

Run the following command in your terminal:

docker --version
You should see an output similar to:

Docker version 20.10.17, build 100c701
Check Python Version

Run the following command in your terminal:

python --version
You should see an output similar to:

Python 3.9.7
Step 4: Create a Dockerfile 📄
A Dockerfile is a script that contains instructions for Docker to build an image. Create a file named Dockerfile (no file extension) in the same directory as app.py and add the following content:

# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the Python script
CMD ["python", "app.py"]
This Dockerfile does the following:

Uses the official Python 3.9 slim image as the base.
Sets the working directory inside the container to /app.
Copies the contents of the current directory (including app.py) into the container.
Runs the app.py script when the container starts.
Step 5: Build the Docker Image 🏗️
Now that we have our Dockerfile and app.py, let's build the Docker image.

Open a terminal in the directory containing the Dockerfile and app.py. Run the following command to build the Docker image:

docker build -t hello-world-app .
The -t flag tags the image with the name hello-world-app.
The . at the end specifies the build context (current directory).
Step 6: Verify the Docker Image 🖼️
After building the image, let's verify that it was created successfully.

Run the following command:

docker images
You should see an output similar to:

REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
hello-world-app     latest    abc123def456   10 seconds ago   123MB
Step 7: Run the Docker Container 🚀
Finally, let's run the Docker container to execute our Python script.

Run the following command:

docker run hello-world-app
You should see the output:

Hello World! 🐳
Documentation
Docker Docmunetation

Docker Desktop Documentation

Conclusion 🎉

Congratulations! 🎉 You’ve successfully created a Dockerized Python application that prints "Hello World! 🐳". This is just the beginning of your Docker journey. Keep exploring and building more complex applications with Docker!

Happy coding! 🚀🐳