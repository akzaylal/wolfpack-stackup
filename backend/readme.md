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
    cd django_todo_app
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

## API Endpoints

### Task List

- **URL:** `/tasks/`
- **Method:** `GET`
- **Description:** Get a list of all tasks for the authenticated user.
- **Example Request:**

  ```bash
  http GET http://localhost:8000/tasks/ "Authorization: Token <your_token>"
