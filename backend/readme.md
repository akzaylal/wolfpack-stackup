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

# URL Patterns Documentation

This document outlines the URL patterns for the Django project.

## Authentication

### Register a User

- **Path:** `/register/`
- **View Class:** `UserRegister`
- **Name:** `register`
- **Authorization:** Not required

This URL is used for user registration. When a user accesses this path, the `UserRegister` view is invoked, and no authorization header is required.

### User Login

- **Path:** `/login/`
- **View Class:** `UserLogin`
- **Name:** `login`
- **Authorization:** Not required

This URL is used for user login. When a user accesses this path, the `UserLogin` view is invoked, and no authorization header is required.

### User Logout

- **Path:** `/logout/`
- **View Class:** `UserLogout`
- **Name:** `logout`
- **Authorization:** Required

This URL is used for user logout. When a user accesses this path, the `UserLogout` view is invoked, and an authorization header is required.

## Task Operations

### Create a Task

- **Path:** `/create/`
- **View Class:** `TaskListView`
- **Name:** `create`
- **Authorization:** Required

This URL is used to create a new task. When a user accesses this path, the `TaskListView` view is invoked, and an authorization header is required.

### List Tasks

- **Path:** `/list/`
- **View Class:** `TaskListView`
- **Name:** `list`
- **Authorization:** Required

This URL is used to list all tasks. When a user accesses this path, the `TaskListView` view is invoked, and an authorization header is required.

### Update a Task

- **Path:** `/update/<int:pk>/`
- **View Class:** `TaskDetailView`
- **Name:** `update`
- **Authorization:** Required

This URL is used to update a specific task. When a user accesses this path, the `TaskDetailView` view is invoked, and an authorization header is required.

### Delete a Task

- **Path:** `/delete/<int:pk>/`
- **View Class:** `TaskDetailView`
- **Name:** `delete`
- **Authorization:** Required

This URL is used to delete a specific task. When a user accesses this path, the `TaskDetailView` view is invoked, and an authorization header is required.

## Running the Server

To run the Django development server, use the following command:

```bash
python manage.py runserver


