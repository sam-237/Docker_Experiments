# 🗄️ MySQL Using Docker

Welcome to the **MySQL Using Docker** project! This project demonstrates how to run a MySQL database container using Docker. It includes setting environment variables, initializing the database with a `.sql` file, and verifying everything works — all inside a Docker container.

---

## 📋 Prerequisites

Make sure the following are installed on your system:

- ✅ Docker (https://docs.docker.com/get-docker/)
- ✅ Docker Desktop (for GUI users)
- ✅ Basic terminal/command line usage

---

## 🗂️ Project Structure

```
04_SQL_MySQL/
├── Dockerfile
├── init.sql
```

---

## 📄 Step 1: Create the SQL Initialization Script

Create a file named `init.sql` with the following content:

```sql
-- init.sql
CREATE DATABASE IF NOT EXISTS student_db;

USE student_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    grade CHAR(1)
);

INSERT INTO students (name, grade) VALUES ('Dhruv', 'Kaushik'), ('Mehak', 'Dhiman'), ('Sambit', 'Majumder'), ('Saurabh', 'Singh');
```

This script will be executed automatically when the container is initialized.

---

## 🐳 Step 2: Create the Dockerfile

Now, add the following content to your `Dockerfile`:

```Dockerfile
# Dockerfile

FROM mysql:latest

# Set environment variables
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=student_db

# Copy SQL script into Docker image
COPY init.sql /docker-entrypoint-initdb.d/
```

📌 Notes:
- `MYSQL_ROOT_PASSWORD` sets the root password.
- The `.sql` file in `/docker-entrypoint-initdb.d/` runs automatically when the container starts for the first time.

---

## 🧱 Step 3: Build the Docker Image

Open your terminal in the project folder and run:

```bash
docker build -t mysql-student-db .
```

This command builds a Docker image with MySQL preloaded with your SQL script.

---

## 🚀 Step 4: Run the MySQL Container

Now, start the container:

```bash
docker run -d \
  --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=root \
  -p 3306:3306 \
  mysql-student-db
```

You should now have a MySQL server running on port `3306`.

---

## 🔍 Step 5: Verify the Setup

To verify that the database and table were created successfully:

1. Enter the container:

```bash
docker exec -it mysql-container mysql -uroot -proot
```

2. Run SQL commands:

```sql
SHOW DATABASES;
USE student_db;
SHOW TABLES;
SELECT * FROM students;
```

✅ THE OUTPUT

 +-----------+-----------+----------+
| StudentID | FirstName | Surname  |
+-----------+-----------+----------+
|         1 | Dhruv     | Kaushik  |
|         2 | Mehak     | Dhiman   |
|         3 | Sambit    | Majumder |
|         4 | Saurabh   | Singh    |
+-----------+-----------+----------+


---

## 📄 Documentation

- [MySQL Docker Hub Image](https://hub.docker.com/_/mysql)
- [Docker Volumes](https://docs.docker.com/storage/volumes/)
- [MySQL Docs](https://dev.mysql.com/doc/)

---

## 🎉 Conclusion

Congratulations! 🎉 You've successfully:

- Written a SQL schema file.
- Created a MySQL Docker container.
- Initialized a database on container startup.
- Verified your database and table from inside the container.

Keep experimenting! 🚀🐳
