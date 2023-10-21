# var environment

prod_database = 'image_tags_db'
prod_user = 'postgres'
prod_password = '12345'
prod_host = 'localhost'
prod_port = '5432'

dev_database = 'image_tags_db'
dev_user = 'postgres'
dev_password = '12345'
dev_host = 'localhost'
dev_port = '5432'

# profile environment

dev_environment = {
    'name': dev_database,
    'user': dev_user,
    'password': dev_password,
    'host': dev_host,
    'port': dev_port,
    'production': False
}

prod_environment = {
    'name': prod_database,
    'user': prod_user,
    'password': prod_password,
    'host': prod_host,
    'port': prod_port,
    'production': True
}

environment = prod_environment
