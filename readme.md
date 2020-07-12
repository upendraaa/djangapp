Installation in MAC
To check python version  ‘python —version’
For python 3 ‘python3 —version’
Install Django 'pip install Django==3.0.8’
install Django for python 3 'pip3 install Django==3.0.8’ 

To check Installed Django version
xyz-MacBook-Air:~ xyz$ python3
Python 3.7.3 (default, Mar 27 2019, 09:23:32) 
[Clang 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> print(django.get_version())
3.0.8
>>> 

7. Create first project
django-admin startproject djangapp

9. Tree command to check default created file in djangapp  ‘tree'
.

├── djangapp

│   ├── __init__.py

│   ├── asgi.py

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py

└── manage.py



10. Run Django project, As this not required any External web server

python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

July 11, 2020 - 17:36:47
Django version 3.0.8, using settings 'djangapp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

11. Can browse 'http://localhost:8000/‘
12. Create admin user
xyz-MacBook-Air:djangapp xyz$ python3 manage.py createsuperuser
Username (leave blank to use ‘xyz'): XYZ
Email address: user@gmail.com
Password: 
Password (again): 

13: Run the server by command ‘python3 manage.py runserver’
14 open 'http://localhost:8000/admin/‘ in browser and enter Username and password
15: Creating first Django app
xyz-MacBook-Air:djangapp xyz$ python3 manage.py startapp demoapp
xyz-MacBook-Air:djangapp xyz$ cd demoapp
xyz-MacBook-Air:demoapp xyz$ tree
.
├── __init__.py
├── admin.py
├── apps.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

1 directory, 7 files

