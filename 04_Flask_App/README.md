# 🖥️ Full Stack App Using Docker (Flask + MySQL + CSV Data)

This project demonstrates how to build and run a **full stack web application** using **Flask (Python)** as the backend and **MySQL** as the database — all containerized using Docker and Docker Compose.

It also loads data from a **CSV file (`mushroom.csv`)** into the MySQL database.

---

## 📋 Prerequisites

Make sure you have the following installed:

- ✅ Docker: [Install Docker](https://docs.docker.com/get-docker/)
- ✅ Docker Desktop (optional GUI)
- ✅ Basic knowledge of Flask, MySQL, and Docker

---

## 🗂️ Project Structure

```
05_FullStack_App/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── mushroom.csv
├── Dockerfile
├── docker-compose.yml
```

---

## 🔧 Step 1: Flask Backend Code

### backend/app.py

```python
# app.py

from flask import Flask
import mysql.connector
import csv

app = Flask(__name__)

def load_csv_to_db():
    connection = mysql.connector.connect(
        host='mysql_db',
        user='root',
        password='root',
        database='test_db'
    )
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS mushrooms (class VARCHAR(10), cap_shape VARCHAR(10));")

    with open('mushroom.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            cursor.execute("INSERT INTO mushrooms (class, cap_shape) VALUES (%s, %s)", row)

    connection.commit()
    connection.close()

@app.route('/')
def hello():
    connection = mysql.connector.connect(
        host='mysql_db',
        user='root',
        password='root',
        database='test_db'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM mushrooms;")
    count = cursor.fetchone()[0]
    connection.close()
    return f"Mushroom dataset loaded with {count} records! 🍄"

if __name__ == '__main__':
    load_csv_to_db()
    app.run(host='0.0.0.0', port=5000)
```

---

## 📦 Step 2: Backend Requirements

### backend/requirements.txt

```
flask
mysql-connector-python
```

---

## 🐳 Step 3: Dockerfile

Create `Dockerfile` in the root folder:

```Dockerfile
# Dockerfile
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

---

## ⚙️ Step 4: Docker Compose

Create `docker-compose.yml` in the root:

```yaml
# docker-compose.yml

version: '3.8'

services:
  flask-app:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - mysql_db

  mysql_db:
    image: mysql:latest
    environment:
      MYSQL_ROOT_PASSWORD: root
      MYSQL_DATABASE: test_db
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
    command: --default-authentication-plugin=mysql_native_password

volumes:
  mysql_data:
```

---

## 🍄 Step 5: Mushroom CSV File

Place the `mushroom.csv` file inside the `backend/` folder.

**Sample `mushroom.csv` content:**

```
class,cap_shape
edible,bell
poisonous,conical
edible,flat
```

Ensure this file is present **before building the container** so it gets copied into the image.

---

## 🚀 Step 6: Build and Run

```bash
docker-compose up --build
```

---

## 🌐 Step 7: View in Browser

Open your browser and go to:

```
http://localhost:5000
```

You should see:

```
Mushroom dataset loaded with 3 records! 🍄
```

---

## 🧼 To Stop & Clean Up

```bash
docker-compose down -v
```

---

## 📚 Documentation

- [Flask](https://flask.palletsprojects.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [MySQL Docker Image](https://hub.docker.com/_/mysql)

---

## 🎉 Conclusion

You've successfully built a containerized full stack app that loads data from a CSV into a MySQL database and serves it through a Flask backend. Great job! 🍄🐳🚀

