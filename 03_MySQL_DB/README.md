Running MySQL Using Docker 🐳📊
In this project, we will deploy a MySQL database using Docker, a powerful platform for containerizing applications. Docker ensures that your database is portable, scalable, and independent of the underlying system. This guide will walk you through the process of setting up a MySQL database inside a Docker container, initializing it with a sample dataset, and interacting with it using SQL queries.

By the end of this tutorial, you will have a fully functional MySQL database running inside a Docker container, ready for development or production use. 🚀

Project Overview 📖
This project demonstrates how to containerize a MySQL database using Docker. The database is initialized with a sample schema and data, allowing you to interact with it using SQL queries. The setup is ideal for development, testing, or even production environments where portability and scalability are critical.

Documentation 📚
For more information, refer to the official documentation:

Docker Documentation

MySQL Documentation

Docker Desktop Documentation

Prerequisites 📋
Before we begin, ensure you have the following installed on your system:

Docker: A platform for developing, shipping, and running applications in containers.

Docker Desktop: A tool to manage Docker containers on your local machine.

Installation and Setup 🛠️
Step 1: Verify Docker Installation
Run the following command in your terminal to check if Docker is installed:

bash
Copy
Edit
docker --version
You should see an output similar to:

bash
Copy
Edit
Docker version 20.10.17, build 100c701
Project Structure 🗂️
The project consists of the following files:

database_students.sql: A SQL script to create a database and insert sample data.

Dockerfile: A script containing instructions for Docker to build an image.

Create the SQL Script 📄
The database_students.sql file contains the SQL commands to create a database and insert sample data:

sql
Copy
Edit
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
Explanation of the SQL Script
CREATE DATABASE student;: Creates a new database named student.

USE student;: Switches to the student database.

CREATE TABLE students (...);: Creates a table named students with columns StudentID, FirstName, and Surname.

INSERT INTO students (...);: Inserts sample data into the students table.

Dockerfile 📄
The Dockerfile is a script that contains instructions for Docker to build an image:

Dockerfile
Copy
Edit
# Use the official MySQL image as the base image
FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=root

# Copy the SQL script to initialize the database
COPY ./database_students.sql /docker-entrypoint-initdb.d/
Explanation of the Dockerfile
FROM mysql:latest: Specifies the base image (official MySQL image).

ENV MYSQL_ROOT_PASSWORD=root: Sets the root password for MySQL.

COPY ./database_students.sql /docker-entrypoint-initdb.d/: Copies the SQL script to the Docker auto-init folder.

Deployment 🚀
Step 1: Build the Docker Image
Navigate to the directory containing the Dockerfile and run:

bash
Copy
Edit
docker build -t mysql_db .
-t mysql_db: Tags the image.

.: Specifies the build context (current directory).

Step 2: Verify the Docker Image
Run:

bash
Copy
Edit
docker images
Expected output:

nginx
Copy
Edit
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
mysql_db     latest    abc123def456   10 seconds ago   500MB
Step 3: Run the Docker Container
bash
Copy
Edit
docker run -d --name mysql_container mysql_db
-d: Detached mode

--name mysql_container: Names the container

Step 4: Access the MySQL Container
bash
Copy
Edit
docker exec -it mysql_container /bin/bash
Step 5: Connect to MySQL
bash
Copy
Edit
mysql -u root -p
Enter password root.

Step 6: Query the Database
sql
Copy
Edit
USE student;
SELECT * FROM students;
Expected output:

diff
Copy
Edit
+-----------+-----------+----------+
| StudentID | FirstName | Surname  |
+-----------+-----------+----------+
|         1 | Dhruv     | Kaushik  |
|         2 | Mehak     | Dhiman   |
|         3 | Sambit    | Majumder |
|         4 | Saurabh   | Singh    |
+-----------+-----------+----------+
Conclusion 🎉
Congratulations! 🎉 You’ve successfully deployed a MySQL database using Docker. This setup ensures that your database is portable, scalable, and easy to reproduce anywhere.

Keep exploring and building more complex applications with Docker and MySQL! 🚀📊

Happy coding! 💻✨