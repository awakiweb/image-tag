# Specifications

- Python 3.9
- Django 3.2.5
- graphene 2.1.8

# Install

```docker-compose up --build```

```docker-compose exec api python manage.py migrate```

```docker-compose exec api python loaddata seeds/01_initial_superusers```