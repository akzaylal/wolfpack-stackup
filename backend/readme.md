# Django TODO App Documentation

## Overview

This Django TODO app allows users to manage their tasks. Users can view a list of their tasks, create new tasks, update existing tasks, and delete tasks.

## How to Run the Development Server

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd backend
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (if needed):

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the API at [http://localhost:8000](http://localhost:8000).

### Admin Login

## API Endpoints

### Admin Login
- **URL:** `http://localhost:8000/admin/`
-  **Description:** use superuser username and password.
### Authentication

- **URL:** `http://localhost:8000/login/`
- **Method:** `POST`
- **Description:** pass username and password .and return the token.

- **URL:** `http://localhost:8000/register/`
- **Method:** `POST`
- **Description:** to register new user.

- **URL:** `http://localhost:8000/logout/`
- **Method:** `POST`
- **Description:** to logout user which delete the token assosiated with user.
- **Example Request:**

