import os

sc = os.environ.get('SECRET_KEY')

if sc == None:
    print('nao')