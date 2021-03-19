# var environment

prod_database = 'd2jk06orkej8o7'
prod_user = 'qtrtlofyxfclao'
prod_password = '6ad640cf6ae18222e924072373f995c937d6ae49958031ce0884e322bdb5e3ba'
prod_host = 'ec2-18-204-101-137.compute-1.amazonaws.com'
prod_port = '5432'

dev_database = 'elephantus_db'
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
