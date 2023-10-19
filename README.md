# AWS-Project


Welcome to the AWS Web Deployment Project. This project demonstrates the end-to-end deployment of a web application on Amazon Web Services (AWS), leveraging services like Route 53, EC2, RDS, and S3. The web application allows users to input and manage employee details, such as first name, last name, employee ID, primary skills, and location, which are securely stored in an AWS RDS database.


Database Schema
The project includes a structured database schema consisting of five tables:

empid for Employee ID.
fname for First Name.
lname for Last Name.
priskill for Primary Skills.
location for Work Locations.
This schema ensures organized data storage and retrieval.

AWS Configuration
The project is configured with the following AWS parameters:

RDS Database Host: Your_RDS_Host
RDS Database User: Your_RDS_User
RDS Database Password: Your_RDS_Password
RDS Database Name: Your_RDS_DB
S3 Bucket Name: Your_S3_Bucket
AWS Region: Your_AWS_Region
Getting Started



# Example setup steps
git clone https://github.com/yourusername/aws-web-deployment.git
cd aws-web-deployment
npm install

# Acknowledgments

- https://www.youtube.com/watch?v=7Gym2XVcA5A&ab_channel=Intellipaat
- https://www.cloudways.com/blog/aws-for-beginners/
