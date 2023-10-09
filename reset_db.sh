### super users credentials

## admin: 65CJHJGFZzTmGq6

# delete migrations

rm -r */migrations
rm -r media/excel
rm -r media/geojson

# create migrations

python manage.py makemigrations
python manage.py makemigrations counties
python manage.py makemigrations cities
python manage.py makemigrations projects
python manage.py makemigrations excel_columms
python manage.py makemigrations resources
python manage.py makemigrations customers
python manage.py migrate

# run seeds

python manage.py loaddata seeds/01_initial_superusers
python manage.py loaddata seeds/02_initial_excel_columns
python manage.py loaddata seeds/03_initial_counties
python manage.py loaddata seeds/04_initial_cities

# run project

python manage.py runserver
