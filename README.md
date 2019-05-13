Django application to let user login/logout to/from facebook via python-social-auth. The app displays the user's name and user's profile picture once successfully authenticated.

## Features

- Django 2.0+
- Databse sqlite3
- User python-social-auth startegy to login and logout user.
- User data is stored in a seperate model once user is logged out the user instance is marked as false.

## How to install

```bash
$ mkdir project_name
$ cd project_name
$ git clone https://github.com/swamifalgun/facebook-login-python-social.git
$ pip install python3
$ create virtualenv folder
$ cd virtualenv folder
$ python3 -m venv sweetenv
$ activate virtualenv
$ source bin/activate
$ cd 
$ cd project_name
$ install requirements
$ pip install -r requirements.txt
$ python manage.py runserver 
```

Go to http://localhost:8000
