### super users credentials

## admin: 65CJHJGFZzTmGq6
## test: 65CJHJGFZzTmGq6

# delete migrations

rm -r */migrations

# create migrations

python manage.py makemigrations
python manage.py makemigrations money
python manage.py migrate

# run seeds

python manage.py loaddata seeds/01_initial_superusers
python manage.py loaddata seeds/02_initial_moneys

# run project

python manage.py runserver