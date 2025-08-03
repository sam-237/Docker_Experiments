🐳 Streamlit App with Docker
Welcome to the Python Streamlit App project! In this tutorial, we'll create a simple Streamlit web app and run it inside a Docker container. This project is ideal for beginners who want to understand how to dockerize a basic frontend using Python and Streamlit. 🚀

By the end of this tutorial, you’ll have a running web app asking for your name and responding with a personalized greeting – all inside a container!

📋 Prerequisites
Before we begin, make sure you have the following installed:

Docker – Platform for building, running, and sharing containers
👉 Install Docker

Docker Desktop – GUI to manage containers
👉 Install Docker Desktop

🗂️ Project Structure
bash
Copy
Edit
Python_App/
├── pythonapp.py           # Main Streamlit application
├── Dockerfile             # Docker configuration
└── README.md              # You are here!
🐍 Step 1: Create the Python App
Let's build a simple Streamlit app that greets the user:

python
Copy
Edit
# pythonapp.py

import streamlit as st
 
st.title("My First App")
 
st.write("Hello How are you")
 
name = st.text_input("What is your name")
 
if name:
    st.success(f"Nice to meet you , {name}!")
🛠️ Step 2: Create a Dockerfile
We'll now containerize this app using Docker. Here's the Dockerfile:

Dockerfile
Copy
Edit
# Use Python slim image
FROM python:3-slim

# Set working directory
WORKDIR /app

# Copy the app file
COPY pythonapp.py pythonapp.py

# Install dependencies
RUN pip install streamlit

# Expose the Streamlit port
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "pythonapp.py", "--server.port=8501", "--server.address=0.0.0.0"]
🧪 Step 3: Build the Docker Image
Open a terminal in the folder containing your Dockerfile and pythonapp.py.
Run the following command to build the image:

bash
Copy
Edit
docker build -t streamlit-app .
Explanation:

-t streamlit-app: Tags the image as streamlit-app

.: Specifies the current directory as the build context

🧾 Step 4: Run the Docker Container
Start the container using:

bash
Copy
Edit
docker run -p 8501:8501 streamlit-app
Explanation:

-p 8501:8501: Maps the container’s port 8501 to your local port 8501

🌐 Step 5: Open the App in Your Browser
Open this URL in your browser:

arduino
Copy
Edit
http://localhost:8501
You should see:

My First App
Hello How are you
[Text Input Box]
✅ Nice to meet you, <your_name>!

📦 Verify Docker Container (Optional)
Check if the container is running:

bash
Copy
Edit
docker ps
Stop it with:

bash
Copy
Edit
docker stop <container_id>
📚 Documentation
Streamlit Docs

Docker Docs

Docker Desktop

🎉 Conclusion
Congratulations! 🎉 You've successfully created and deployed a Streamlit app inside a Docker container. This is a great foundation for building interactive data apps, dashboards, or ML interfaces.

Keep experimenting and happy coding! 🚀💻