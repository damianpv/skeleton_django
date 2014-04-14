# skeleton_django #

Basic skeleton for Django 1.6+ and Best practice.


## Overview ##

### Prerequisites ###

* Debian/Ubuntu
* Python 2.7+
* PIP
* virtualenv/virtualenvwrapper (optional)


## Installation ##

### Creating the environment ###
Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####
```bash
mkvirtualenv --no-site-packages {{ project_name }}-env
```

#### For virtualenv ####
```bash
virtualenv --no-site-packages {{ project_name }}-env
cd {{ project_name }}-env
source bin/activate
```

### Clone the code ###
Obtain the url to your git repository.

```bash
git clone <URL_TO_GIT_RESPOSITORY> {{ project_name }}
```

### Configure project ###

for development use:
```bash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sk_django.settings.local")
```

for staging use:
```bash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sk_django.settings.staging")
```
for production use : 
```bash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sk_django.settings.prod")
```

for test use : 
```bash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sk_django.settings.test")
```

in: 
```bash
vi {{ project_name }}/manage.py

```

### Install requirements ###

```bash
cd {{ project_name }}
pip install -r requirements/local.txt
or
pip install -r requirements/production.txt
or
pip install -r requirements/staging.txt
or
pip install -r requirements/test.txt
```
    

### Sync database ###

```bash
python manage.py syncdb
```
    
    
## Running ##
    
```bash
python manage.py runserver
or
python manage.py runserver --settings=sk_django.settings.local
or
python manage.py runserver --settings=sk_django.settings.prod
or
python manage.py runserver --settings=sk_django.settings.staging
or
python manage.py runserver --settings=sk_django.settings.test
```
    

Open browser to http://127.0.0.1:8000 or http://localhost:8000
