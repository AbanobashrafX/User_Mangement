# Django Styleguide Simple Project

This project is a simple Django application following the Django `Styleguide`. It includes user management functionalities such as creating, listing, updating, and deleting users.

## Requirements

- Python 3.x
- Django 3.x or higher
- Django REST Framework

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/AbanobashrafX/User_Mangement.git
    cd User_Mangement
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```sh
    python manage.py migrate
    ```

5. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```


## Endpoints

### Create User

- **URL:** `/api/users/create/`
- **Method:** `POST`
- **Description:** Creates a new user.

### List Users

- **URL:** `/api/users/list/`
- **Method:** `GET`
- **Description:** Lists all users.

### List Active Users

- **URL:** `/api/users/active/`
- **Method:** `GET`
- **Description:** Lists all active users.

### User Details

- **URL:** `/api/users/user/<uuid:uuid>/`
- **Method:** `GET`
- **Description:** Retrieves details of a specific user by UUID.

### Update User

- **URL:** `/api/users/user/<uuid:uuid>/update/`
- **Method:** `PUT`
- **Description:** Updates a specific user by UUID.

### Delete User

- **URL:** `/api/users/user/<uuid:uuid>/delete/`
- **Method:** `DELETE`
- **Description:** Deletes a specific user by UUID.

## Models

### User

- **id:** UUIDField (primary key)
- **username:** CharField (max_length=20, unique)
- **password:** CharField (max_length=255)

## License

This project is licensed under the MIT License. See the LICENSE file for details.