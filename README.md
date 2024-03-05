# Store Inventory

A store inventory API for backend technical assessment

## Tech Stack

- [django](https://www.djangoproject.com/) : Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
- [python-dotenv](https://pypi.org/project/python-dotenv/) : Read key-value pairs from a .env file and set them as environment variables
- [djangorestframework](https://www.django-rest-framework.org/) : Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html) : Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.
- [pyjwt](https://pyjwt.readthedocs.io/en/stable/) : PyJWT is a Python library which allows you to encode and decode JSON Web Tokens (JWT). JWT is an open, industry-standard (RFC 7519) for representing claims securely between two parties.
- [black](https://pypi.org/project/black/)  : Black is the uncompromising Python code formatter.
- [isort](https://pycqa.github.io/isort/)  : isort is a Python utility / library to sort imports alphabetically, and automatically separated into sections and by type.
- [pre-commit](https://pre-commit.com/) : A framework for managing and maintaining multi-language pre-commit hooks.

## Building

The project uses pipenv or dependency management. In the project root directory run:

## Install Dependencies

```sh
pipenv install
```

## Activate virtual environment

```sh
pipenv shell
```

## setup environment variables

Rename `.env.example` to `.env` and add some random environment variables

## Setup database migrations

```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```

## Run the project

```sh
python manage.py runserver
```

This will spawn a local development server on [localhost:8000](localhost:8000). The swagger UI enables you to test the functionality directly in your browser without needing an external API client
