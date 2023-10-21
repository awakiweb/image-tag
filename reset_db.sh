### super users credentials

## admin: 65CJHJGFZzTmGq6

# delete migrations

rm -r */migrations
rm -r media/excel
rm -r media/geojson

# create migrations

python manage.py makemigrations
python manage.py makemigrations images
python manage.py migrate

# run seeds

python manage.py loaddata seeds/01_initial_superusers

# run project

python manage.py runserver
