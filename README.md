# Flask User Management System

This is a simple user management system built with Flask and deployed using Docker.

## Features

- User login and authentication
- Add, edit, and delete users
- Admin portal for managing users

## Requirements

- Docker
- Docker Compose (optional, for more advanced setups)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/flask-user-management.git
   cd flask-user-management
   ```

2. **Build the Docker image:**

   ```sh
   docker build -t flask-app .
   ```

3. **Run the Docker container:**

   ```sh
   docker run -d -p 5000:5000 --name flask-app-container flask-app
   ```

4. **Access the application:**

   Open your web browser and go to `http://localhost:5000`.

## Usage

### Admin Login

- Email: `jagruti03shinde@gmail.com`
- Password: `JagrutiShinde03`

### Managing Users

- Add new users
- Edit existing users
- Delete users

## Development

To run the application locally without Docker:

1. **Set up a virtual environment:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```sh
   python app.py
   ```

4. **Access the application:**

   Open your web browser and go to `http://localhost:5000`.

## Docker Compose

For more advanced setups, you can use Docker Compose. Create a `docker-compose.yml` file in the project root:

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

## Contributing

Feel free to submit issues and pull requests.

## Contact

For any inquiries, please contact [jagruti03shinde@gmail.com](mailto:jagruti03shinde@gmail.com).
