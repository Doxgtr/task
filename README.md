# Employee Management System

A simple Django web application for managing employee records.

## Features

- View all employees
- Add new employees
- Edit employee information
- Manage employee status (Active/Inactive)
- Store employee details: name, email, department, salary, and status

## Requirements

- Python 3.x
- Django 4.2+
- SQLite (included with Django)

## Installation & Setup

1. Clone or navigate to the project directory:
   ```bash
   cd employee
   ```

2. Install Django (if not already installed):
   ```bash
   pip install django
   ```

3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

## Running the Application

Start the development server:
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Admin Panel

Access Django admin panel at `http://127.0.0.1:8000/admin/`

Create a superuser if needed:
```bash
python manage.py createsuperuser
```

## Project Structure

```
employee/
├── emp/                      # Main app
│   ├── models.py            # Employee model
│   ├── views.py             # Views for CRUD operations
│   ├── urls.py              # URL routing
│   ├── templates/emp/       # HTML templates
│   │   ├── home.html        # List all employees
│   │   ├── add.html         # Add new employee
│   │   └── edit.html        # Edit employee
│   └── migrations/          # Database migrations
├── employee/                # Project settings
├── manage.py               # Django management script
└── db.sqlite3              # SQLite database
```

## Database Models

### Employee
- **name** - Employee name (max 100 characters)
- **email** - Employee email (unique)
- **department** - Department name (max 100 characters)
- **salary** - Employee salary
- **status** - Active or Inactive status

## Notes

- This is a development project. Do not use in production without proper security configurations.
- Keep the `SECRET_KEY` safe and use environment variables in production.
- Update `ALLOWED_HOSTS` in settings.py for production deployment.
