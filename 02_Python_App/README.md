# Streamlit App Using Docker 🚀📊

Welcome to the Streamlit App project! In this guide, we will containerize a simple interactive Python app using Streamlit and Docker. This is a great introduction to building and deploying modern Python-based web apps inside containers.

---

## 📋 Prerequisites

Ensure the following tools are installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop/)
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

---

## 🐍 Step 1: Create the Streamlit App

Create a file named `pythonapp.py` with the following code:

```python
import streamlit as st

st.title("My First App")

st.write("Hello How are you")

name = st.text_input("What is your name")

if name:
    st.success(f"Nice to meet you , {name}!")
```

---

## 📄 Step 2: Create the Dockerfile

Create a file named `Dockerfile` in the same directory and add the following content:

```dockerfile
# Use a slim Python base image
FROM python:3-slim

# Set working directory
WORKDIR /app

# Copy the Python script into the container
COPY pythonapp.py pythonapp.py

# Install Streamlit
RUN pip install streamlit

# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "pythonapp.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🏗️ Step 3: Build the Docker Image

Open your terminal, navigate to the directory with your files, and run:

```bash
docker build -t streamlit-app .
```

---

## 🚀 Step 4: Run the Docker Container

To run the app and access it in your browser:

```bash
docker run -p 8501:8501 streamlit-app
```

Visit [http://localhost:8501](http://localhost:8501) to use your app.

---

## 📂 File Structure

```
Streamlit_App/
├── Dockerfile
└── pythonapp.py
```

---

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Docker Documentation](https://docs.docker.com/)
- [Python Official Docs](https://docs.python.org/3/)

---

## 🎉 Conclusion

Congratulations! 🎉 You've created and deployed your first interactive Streamlit app using Docker. Try expanding this project by adding more interactivity or visualizations.
