import os
DATABASE_CONFIG ={
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.sqlite3'),
}

SECRET_KEY = 'secret'
