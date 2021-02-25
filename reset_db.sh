### super users credentials

## admin: admin123
## test: test123

# delete migrations

rm -r */migrations

# create migrations

python manage.py makemigrations
python manage.py makemigrations employee
python manage.py makemigrations money
python manage.py makemigrations category
python manage.py makemigrations product
python manage.py makemigrations inventory
python manage.py makemigrations customer
python manage.py migrate

# run seeds

python manage.py loaddata seeds/01_initial_superusers
python manage.py loaddata seeds/02_initial_moneys
python manage.py loaddata seeds/03_initial_categories

# run project

python manage.py runserver