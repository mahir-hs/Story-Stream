# Story Stream API

Welcome to the Story Stream API! This API provides endpoints for managing users, profiles, articles, ratings, bookmarks, and more.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Story Stream API is designed to handle various functionalities related to user-generated content, including user authentication, profile management, article creation, and interaction through ratings and bookmarks.

## Features

- User Authentication (Login, Registration, Password Reset)
- User Profile Management
- Article Creation and Management
- Rating and Bookmarking System
- Search Functionality with Elasticsearch

## Installation

To get started with the Story Stream API, follow these steps:

### Using Docker Compose
**All the neccessary commands can be found in "commands.txt"**

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mahir-bot/Story-Stream.git
    cd Story-Stream
    ```

2. **Create and configure environment variables:**

    Copy the example environment files and update them with your settings.

    ```bash
    cp .envs/.local/.django.example .envs/.local/.django
    cp .envs/.local/.postgres.example .envs/.local/.postgres
    ```

3. **Build and start the Docker containers:**

    ```bash
    docker compose -f local.yml up --build -d --remove-orphans
    ```

4. **Apply migrations and create a superuser:**

    Open a new terminal and run the following commands:

    ```bash
    docker compose -f local.yml run --rm api python manage.py makemigrations
    docker compose -f local.yml run --rm api python manage.py migrate
    docker compose -f local.yml run --rm api python manage.py createsuperuser
    ```

5. **Access the application:**

    - The API will be available at `http://localhost:8080/api/v1/`
    - The Django admin will be available at `http://localhost:8080/supersecret/`
    - The API documentation (Redoc) will be available at `http://localhost:8080/redoc/`
    - Elasticsearch will be available at `http://localhost:9200/`
    - PgAdmin will be available at `http://localhost:5050/`
    - MailHog will be available at `http://localhost:8025/`
    - Flower will be available at `http://localhost:5555/`

### Without Docker

If you prefer not to use Docker, you can set up the project manually:

1. **Create a virtual environment and activate it:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

2. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

You can use the API endpoints to interact with the Story Stream platform. Below are some example endpoints:

- **User Details:** `/api/v1/auth/user/`
- **User Registration:** `/api/v1/auth/registration/`
- **Password Reset Confirm:** `/api/v1/auth/password/reset/confirm/<uidb64>/<token>/`
- **Profiles:** `/api/v1/profiles/`
- **Articles:** `/api/v1/articles/`
- **Ratings:** `/api/v1/ratings/`
- **Bookmarks:** `/api/v1/bookmarks/`
- **Responses:** `/api/v1/responses/`
- **Elasticsearch:** `/api/v1/elastic/`

## API Documentation

For detailed API documentation, please visit [Story Stream API Documentation](https://mahir-bot.github.io/Story-Stream/).

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using the Story Stream API! If you have any questions or need further assistance, feel free to open an issue or contact us at mahirhasan333@gmail.com.
