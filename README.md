# Django-Blog

A simple django blog.

## Installation
```console
$ git clone https://github.com/ridvanaltun/django-blog.git
$ cd django-blog/
$ pip install -r requirements.txt
```
## Usage

Start http server:
```console
$ python manage.py runserver
```

- **adress:** http://localhost:8000/
- **admin panel:** http://localhost:8000/admin
- **username:** santa
- **password:** cruz

If you want create a new database follow this directions:

- You need to stop your http server by pressing <kbd>ctrl</kbd> + <kbd>c</kbd>  if it running.
- Then you can type codes below to terminal:
```console
$ rm -rf db.sqlite3
$ rm -rf media
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```
