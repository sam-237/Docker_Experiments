# Use the official MySQL image as the base image
FROM mysql:latest

# Set the root password for MySQL
ENV MYSQL_ROOT_PASSWORD=root

# Copy the SQL script to initialize the database
COPY ./database_students.sql /docker-entrypoint-initdb.d/