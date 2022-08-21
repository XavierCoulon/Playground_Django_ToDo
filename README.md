## TODO

TODO is a Google task-like website. My main motivation was to build an application from scratch, reviewing almost all concepts and technologies learnt during ["Python Developer"](https://openclassrooms.com/fr/paths/514-python-developer) course followed on Openclassrooms (cf. repositories OC-Pxx for projects realised).<br>




- Python,
- [Django](https://www.djangoproject.com/) as framework,
- OOP regarding models,
- PostgreSQL as database,
- [Allauth](https://django-allauth.readthedocs.io/en/latest/) to address authentification,
- [Pytest-django](https://pytest-django.readthedocs.io/en/latest/), [Factory Boy](https://factoryboy.readthedocs.io/en/stable/), [Faker](https://faker.readthedocs.io/en/master/) and [Coverage](https://coverage.readthedocs.io/en/6.4.4/) for testing,
- [Highcharts](https://www.highcharts.com/) to generate charts,
- [Docker Hub](https://hub.docker.com/signup) regarding container,
- [Gitlab](https://gitlab.com/gitlab-org/gitlab) as CI/CD,
- [Heroku](https://www.heroku.com/) as host,

A quick frontend has been generated using [Bootstrap](https://getbootstrap.com/).
<br><br>
The website is available on Heroku at the following address: https://xcotodo.herokuapp.com/



### 1. Features

- Create an account (potentially using Google connect),
- Create / update / delete lists, 
- Create / update / delete tasks of a list,
- Close / Reopen a task,
- Visualize statistics about tasks,
- Languages supported: French & English.

### 2. Installation

```bash
git clone https://github.com/XavierCoulon/ToDo.git
cd Todo
python3.9 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

A .env file will be required, listing the following variables:
- SECRET_KEY (Django one)
- GMAIL_PASSWORD (not used in actual version)
- GMAIL_EMAIL (not used in actual version)
- POSTGRES_USER
- POSTGRES_DB
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT

Start the server on your localhost and create a superuser:
````
python manage.py runserver
python manage.py createsuperuser
````
Admin available on http://127.0.0.1:8000/admin/

## 3.CI/CD and deployment

On Gitlab the following variables are required:
- SECRET_KEY: Django secret key,
- DOCKER_HUB_USER,
- DOCKER_HUB_PASSWORD,
- HEROKU_APP_NAME,
- HEROKU_API_KEY,
- HEROKU_APP_HOST.

On Heroku:
- DATABASE_URL,
- GMAIL_PASSWORD,
- SECRET_KEY (Django).