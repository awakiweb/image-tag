# var environment

prod_database = 'd5ch7c9o8s92vp'
prod_user = 'vwrdqwbndtkpky'
prod_password = 'a017f48b3d1b9e581d1abc4561c703e1fe1eebbfc8a2e6904e6b0fe563e32d44'
prod_host = 'ec2-174-129-253-125.compute-1.amazonaws.com'
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

environment = dev_environment
