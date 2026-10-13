# AWS 3-Tier Student Management System

## Project Overview
This project is a student management web application deployed using Amazon Web Services (AWS). It displays student records stored in a MySQL database.

## Architecture
User → Application Load Balancer → EC2 (Flask Application) → Amazon RDS (MySQL)

## AWS Services Used
- Amazon EC2: Hosts the Python Flask application.
- Amazon RDS for MySQL: Stores student records.
- Application Load Balancer: Routes incoming HTTP traffic to the application.
- Amazon VPC: Provides network isolation using subnets.
- Security Groups: Restrict access between the load balancer, application server, and database.
- AWS Systems Manager: Provides secure instance access.
- Amazon CloudWatch: Monitors EC2, RDS, and load balancer metrics and CPU alarms.
- IAM: Controls permissions for EC2 and Systems Manager.

## Application Features
- Displays student IDs, names, email addresses, and courses.
- Retrieves records from the MySQL database.
- Uses Flask and PyMySQL to connect the application to the database.
- Runs as a systemd service with automatic startup enabled.

## Security
- Database credentials are stored in a local `.env` file.
- The `.env` file is excluded using `.gitignore`.
- The database accepts connections from the application security group.
- The Flask application accepts traffic from the load balancer security group.

## Monitoring
A CloudWatch dashboard tracks EC2 CPU utilization, RDS CPU utilization, and load balancer HTTP 4XX responses. An EC2 high-CPU alarm is configured.

## Technologies
Python, Flask, MySQL, PyMySQL, Amazon EC2, Amazon RDS, Application Load Balancer, VPC, IAM, Systems Manager, and CloudWatch.

## Future Improvements
- Configure HTTPS using a domain and an SSL/TLS certificate.

## Local Setup
1. Clone this repository:
   ```bash
   git clone YOUR_REPOSITORY_URL
   cd aws-3-tier-student-management
- Add student creation, editing, and deletion features.
- Improve application styling and error handling.

## Disclaimer
This project was created for learning and demonstration purposes.
