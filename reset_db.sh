### super users credentials

## admin: admin123
## test: test123

# delete migrations

rm -r */migrations

# create migrations

python manage.py makemigrations
python manage.py migrate

# run seeds

python manage.py loaddata seeds/01_initial_superusers