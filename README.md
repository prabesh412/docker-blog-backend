# Docker Blog Backend

Behold My Awesome Project!


License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users


-   To create a **superuser account**, use this command:

        $  docker-compose - f local.yml run --rm django python manage.py createsuperuser



To run the tests, check your test coverage, and generate an HTML coverage report:

    $ docker-compose - f local.yml run --rm django python manage.py test

### Run the server 
    $ docker-compose - f local.yml run --rm django python manage.py up

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
