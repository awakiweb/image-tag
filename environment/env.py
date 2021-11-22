# var environment

prod_database = 'd4kqtbjva3j5cn'
prod_user = 'igemzljnsyymdq'
prod_password = 'bfe3d3502a4c8bfab06e4b17d3210faa369cf81d23fa7fe64a13b829108f8f27'
prod_host = 'ec2-23-23-141-171.compute-1.amazonaws.com'
prod_port = '5432'

dev_database = 'd4kqtbjva3j5cn'
dev_user = 'igemzljnsyymdq'
dev_password = 'bfe3d3502a4c8bfab06e4b17d3210faa369cf81d23fa7fe64a13b829108f8f27'
dev_host = 'ec2-23-23-141-171.compute-1.amazonaws.com'
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
