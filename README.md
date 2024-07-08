
# Flask User Management System

## Overview

The Flask User Management System is a web-based application designed to manage user accounts with ease. Built with the Flask framework, this system provides a comprehensive suite of features for user authentication, user data management, and an administrative portal. The system leverages Docker for deployment, ensuring that the application is easy to set up and deploy in various environments.

## Key Features

### User Authentication
- **Secure Login:** Users can log in using their email and password.
- **Session Management:** Secure session handling to ensure user data is protected during their interaction with the system.

### Admin Portal
- **User Management:** Administrators can add, edit, and delete user accounts.
- **User Listing:** View a comprehensive list of all registered users, with options to edit or remove accounts.
- **Flash Messages:** Informative flash messages are displayed to notify administrators of actions such as successful user addition, updates, and deletions.

### User Management
- **Add New Users:** Easily add new users by providing their name and email.
- **Edit User Details:** Update user information such as name and email.
- **Delete Users:** Remove users from the system with a single click.

### Technology Stack

### Backend
- **Flask:** A lightweight WSGI web application framework in Python, perfect for building web applications with simplicity and flexibility.
- **Werkzeug:** A comprehensive WSGI web application library used by Flask for request and response handling.

### Frontend
- **HTML/CSS:** The structure and styling of the application are managed using standard HTML and CSS.
- **Bootstrap:** A popular CSS framework that ensures the application is responsive and visually appealing.

### Deployment
- **Docker:** The application is containerized using Docker, allowing for consistent and isolated environments across different stages of development and production.

## Installation and Setup

### Requirements
- **Docker:** Ensure Docker is installed on your machine. Follow the [official Docker installation guide](https://docs.docker.com/get-docker/) if needed.
- **Docker Compose:** Optional but recommended for advanced setups. Install Docker Compose from [here](https://docs.docker.com/compose/install/).

### Steps to Run the Application

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/flask-user-management-docker.git
   cd flask-user-management-docker
   ```

2. **Build the Docker Image:**

   ```sh
   docker build -t flask-app .
   ```

3. **Run the Docker Container:**

   ```sh
   docker run -d -p 5000:5000 --name flask-app-container flask-app
   ```

4. **Access the Application:**

   Open your web browser and navigate to `http://localhost:5000`.


## Docker Compose

For advanced setups using Docker Compose, create a `docker-compose.yml` file in the project root:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
```

Then run:

```sh
docker-compose up
```

## Docker Hub

The Docker image for this application is available on Docker Hub. You can pull it using the following command:

```sh
docker pull jagruti03shinde/user-management-application
```

## Admin Credentials

Use the following credentials to log in to the admin portal:

- **Email:** `jagruti03shinde@gmail.com`
- **Password:** `JagrutiShinde03`

## Contact

For any inquiries, please contact [jagruti03shinde@gmail.com](mailto:jagruti03shinde@gmail.com).
