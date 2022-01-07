# Perpus
## Django Backend

[![N|Solid](https://static.djangoproject.com/img/logos/django-logo-negative.svg)](https://nodesource.com/products/nsolid)

## Features

- Create, Read, Update, Delete(CRUD) Book 
- Admin Page
- Export Database Data into Excel Files(XLS)
- List Table Data
- RestApi


## Tech

Build With

- [Python] - Python is a dynamically typed programming language.
- [Django] - Django is a web application framework for Python.
- [jQuery] - duh.
- [Bootstrap] - great UI boilerplate.
- [Django-Rest-Framework] - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [MySQL] Databases
- [SQLITE3] Databases
- [Django-Import-Export] - django-import-export is a Django application and library for importing and exporting data with included admin integration.


And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Set Up virtual environments

```sh
pip install virtualenv
python -m venv env
env\Scripts\activate
```

Install Required Package
```sh
python -m pip install -U pip
pip install django mysqlclient djangorestframework pillow django-import-export
```

Create Super User And Run Server
```sh
    python manage.py createsuperuser
    python manage.py runserver
```


## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Package | Docs |
| ------ | ------ |
| Django | [Django](https://www.djangoproject.com) |
| Django Import Export | [Django Import Export](django-import-export.readthedocs.io/en/latest/index.html) |
| Django Restframework | [Django Restframework](https://www.django-rest-framework.org) |
| Pillow | [Pillow](https://pillow.readthedocs.io/en/stable/) |
| MySqlClient | [MqSqlClient](https://pypi.org/project/mysqlclient/) |

## License

MIT
