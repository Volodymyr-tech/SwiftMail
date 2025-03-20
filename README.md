# SwiftMail 2

SwiftMail 2 is an email marketing service built with Django. It allows you to send messages after configuring the mail service.

## Mail Service Configuration
Before using the service, you need to configure the email provider. Instructions can be found in the `env.example` file.

## Database
The project uses **PostgreSQL** as the main database. Configuration instructions are available in the `env.example` file.

## User Roles and Permissions
The service includes a role-based access system:
- **Service Users**
- **Managers**

## Custom Commands and Functions
Custom management commands for user and group management are available in the `users/management/commands` module. There are also custom functions for **creating and deleting admin users**.

## Caching
Low-level caching is implemented using **Redis** to improve system performance.

## Debugging
The project uses **Django Debug Toolbar**. The settings are located in the `settings.py` file.

## Install dependencies using Poetry
poetry install

## Apply migrations
poetry run python manage.py migrate

# Start the development server
poetry run python manage.py runserver
