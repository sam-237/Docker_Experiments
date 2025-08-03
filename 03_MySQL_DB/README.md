
```
# 🗄️ MySQL Using Docker

This project demonstrates how to run a **MySQL** database inside a Docker container. It includes an initialization SQL script to create a database and populate it with sample data. This setup is great for development, testing, or learning SQL in a consistent environment.

---

## 📋 Prerequisites

Ensure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

---

## 📂 Project Structure

```
04_SQL_MySQL/
├── Dockerfile
├── init.sql
```

- **Dockerfile** – Builds the custom MySQL image
- **init.sql** – Contains the schema and sample data to initialize

---

## 🧾 init.sql

This SQL script creates a database called `student`, a table `students`, and inserts some sample data.

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
VALUES 
    ("Dhruv", "Kaushik"),
    ("Mehak", "Dhiman"),
    ("Sambit", "Majumder"),
    ("Saurabh", "Singh");
```

---

## 🐳 Dockerfile

```Dockerfile
# Use the official MySQL image as base
FROM mysql:latest

# Set root password for MySQL
ENV MYSQL_ROOT_PASSWORD=root

# Copy SQL file into Docker image for auto-init
COPY ./init.sql /docker-entrypoint-initdb.d/
```

This Dockerfile:
- Starts from the official MySQL image
- Sets a root password (`root`)
- Automatically runs `init.sql` during container startup

---

## 🏗️ Build the Docker Image

Run the following command in the project directory:

```bash
docker build -t mysql-db .
```

---

## 🚀 Run the MySQL Container

```bash
docker run -d --name mysql-container -p 3306:3306 mysql-db
```

- `-d` runs the container in detached mode
- `--name` gives it a recognizable name
- `-p 3306:3306` maps the container port to your machine

---

## 🛠️ Access the MySQL CLI

Once running, enter the container:

```bash
docker exec -it mysql-container bash
```

Then start the MySQL shell:

```bash
mysql -u root -p
# Password: root
```

Switch to the `student` database:

```sql
USE student;
SELECT * FROM students;
```

You should see output like:

```
+-----------+-----------+----------+
| StudentID | FirstName | Surname  |
+-----------+-----------+----------+
|         1 | Dhruv     | Kaushik  |
|         2 | Mehak     | Dhiman   |
|         3 | Sambit    | Majumder |
|         4 | Saurabh   | Singh    |
+-----------+-----------+----------+
```

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
