django-shop-skel
Skeleton for django-shop projects


INSTALLATION.

First install python and virtualenv. We use system site packages to prevent massive compilation on production servers, so first install important packages:

- install Mysql, Sqlite, Postgres, Pillow, gunicorn, werkzeug and pytz and PIP.

In debian:

git
python
python-async
python-crypto
python-dev
python-git
python-gitdb
python-imaging
python-m2crypto
python-markupsafe
python-mysqldb
python-pil
python-pil.imagetk
python-pip
python-pkg-resources
python-psycopg2
python-sane
python-setuptools
python-smmap
python-sqlite
python-tk
python-uwsgidecorators
python-virtualenv
python-yaml
python-zmq
gunicorn
python-werkzeug
python-tz

After that clone repo and create env:

- git clone https://github.com/amon-ra/django-shop-skel newshop
- cd newshop
- virtualenv --system-site-packages env
- source env/bin/activate

install requirements:
- pip install -r src/requirements.txt

Do initial configuration and start:
- edit local_settings.py and configure database 
- python manage.py syncdb --all
- python manage.py migrate --fake

Begin working:
- python manage.py runserver

And create one page with home slug.



