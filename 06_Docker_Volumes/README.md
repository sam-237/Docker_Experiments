# 💾 Docker Volume: Time Logging App

This project demonstrates how to use **Docker Volumes** to persist log data between container runs. The app logs a timestamp every 5 seconds using Python’s built-in `logging` module. The logs are stored in a mounted Docker volume, so even if the container is removed, your logs remain.

---

## 📋 Prerequisites

Make sure the following are installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Python (optional, for local testing)](https://www.python.org/)

---

## 🎯 Objective

To understand how Docker volumes help in persisting container data, specifically logs generated over time.

---

## 📂 Project Structure

```
06_Docker_Volume/
├── app.py
├── Dockerfile
```

---

## 🐍 `app.py`

This script logs the current time to `/logs/app.log` every 5 seconds.

```python
import time
import logging

# Set up logging
logging.basicConfig(filename='/logs/app.log', level=logging.INFO)

while True:
    logging.info(f'Logging a new entry at {time.ctime()}')
    time.sleep(5)  # Simulate a delay of 5 seconds between log entries
```

---

## 🐳 `Dockerfile`

Defines how the Docker image is built for the time-logging app.

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy the Python script to the container
COPY app.py /app/

# Create log directory
RUN mkdir -p /logs

# Run the Python logging script
CMD ["python", "app.py"]
```

---

## 🏗️ Build the Docker Image

Navigate to the project directory and run:

```bash
docker build -t time-logger .
```

---

## 💾 Create a Docker Volume

This volume will store your log data:

```bash
docker volume create time_logs
```

---

## 🚀 Run the Container with Volume Attached

Mount the volume to `/logs` in the container:

```bash
docker run -v time_logs:/logs time-logger
```

The script will log the current timestamp every 5 seconds into `/logs/app.log`.

---

## 📜 View the Logged Output

To check what’s inside the log file:

```bash
docker run -it --rm -v time_logs:/logs ubuntu cat /logs/app.log
```

You should see entries like:

```
INFO:root:Logging a new entry at Sun Aug  3 21:13:12 2025
INFO:root:Logging a new entry at Sun Aug  3 21:13:17 2025
```

---

## 📚 References

- [Docker Volumes](https://docs.docker.com/storage/volumes/)
- [Python `logging`](https://docs.python.org/3/library/logging.html)

---

## 🎉 Conclusion

You’ve built a persistent logging service with Docker using **volumes**. This technique is essential for real-world applications where logs and state data must survive container restarts.

Keep logging, keep learning! 📘🐳🕒
