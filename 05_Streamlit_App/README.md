# 🌀 Spiral Streamlit App Using Docker

Welcome to the Spiral Visualization Project! In this experiment, we use **Streamlit** to build an interactive Python web app that plots a beautiful spiral using `matplotlib`. The app is containerized using Docker to demonstrate deploying visual tools with ease.

---

## 📋 Prerequisites

Before we begin, make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Python (for local testing)](https://www.python.org/)
- Internet connection (for installing packages during image build)

---

## 🧠 Objective

To containerize a **Streamlit** app that plots a spiral using basic mathematical functions and make it accessible via a browser using Docker.

---

## 📂 Project Structure

```
05_Streamlit_Spiral_App/
├── app.py
├── Dockerfile
```

---

## 🐍 `app.py`

This is the main Python script that uses **Streamlit** and **matplotlib** to plot a spiral.

```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Spiral Visualization")

a = st.slider("a (starting radius)", 0.1, 2.0, 0.5)
b = st.slider("b (growth factor)", 0.1, 2.0, 0.2)
theta = np.linspace(0, 4 * np.pi, 1000)
r = a + b * theta

x = r * np.cos(theta)
y = r * np.sin(theta)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal')

st.pyplot(fig)
```

---

## 🐳 `Dockerfile`

This file defines how the Docker image is built.

```Dockerfile
# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY app.py .

# Install dependencies
RUN pip install streamlit matplotlib numpy

# Expose Streamlit's default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🏗️ Build the Docker Image

Navigate to the `05_Streamlit_Spiral_App/` directory in your terminal and run:

```bash
docker build -t spiral-app .
```

---

## 🚀 Run the Docker Container

Launch your Streamlit spiral app:

```bash
docker run -p 8501:8501 spiral-app
```

Then open your browser and visit:

```
http://localhost:8501
```

---

## 📌 Sample Output

You’ll see an interactive spiral with sliders for real-time changes to the parameters `a` and `b`.

---

## 📚 References

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Docker Documentation](https://docs.docker.com/)

---

## 🎉 Conclusion

Congratulations! You've built and containerized a visually interactive app using Streamlit and Docker. This project demonstrates the power of combining mathematics, interactivity, and deployment tools.

Keep spiraling into deeper projects! 🐳🌀🚀
