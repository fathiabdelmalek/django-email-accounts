# Django Email Accounts

Django Email Accounts is a Django app for user management with email-based authentication. It provides a customizable User model and registration view for handling user registration and authentication using email and password.

## Installation

Install the package using pip:

```shell
pip install django-email-accounts
```

## Usage

1. Add `'email_accounts'` to the `INSTALLED_APPS` list in your Django project's `settings.py` file:

```python
INSTALLED_APPS = [
   ...
   'email_accounts',
   ...
]
```

2. Change the default authentication user model by adding this line of code in your Django project's `settings.py` file:

```python
AUTH_USER_MODEL = 'email_accounts.User'
```

3. Update your project's `urls.py` file to include the email-accounts URLs:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('accounts/', include('email_accounts.urls')),
    ...
]
```

4. Run migrations to create the necessary database tables:

```shell
python manage.py migrate
```

5. You can now use the email-accounts functionality in your Django project.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/fathiabdelmalek/django-email-accounts).

To contribute to the project, follow these steps:

1. Fork the repository on GitHub.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make the necessary changes and commit them.
5. Push the changes to your forked repository.
6. Submit a pull request to the main repository.

Please ensure that your code adheres to the project's coding conventions and includes appropriate tests. Also, provide a clear description of the changes you have made in the pull request.

Thank you for your contributions!


## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://github.com/fathiabdelmalek/django-email-accounts/blob/main/LICENSE) file for more details.
