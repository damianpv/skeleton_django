# skeleton_django # 

Basic skeleton for Django.


## Overview ##

### Prerequisites ###

* Debian/Ubuntu
* Python >= 2.7+
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
```bash
cp {{ project_name }}/__local_settings.py {{ project_name }}/local_settings.py
vi {{ project_name }}/local_settings.py
```

### Install requirements ###

```bash
cd {{ project_name }}
pip install -r requirements.txt
```
    

### Sync database ###

```bash
python manage.py syncdb
```
    
    
### Running ###
    
```bash
python manage.py runserver
```
    

Open browser to http://127.0.0.1:8000 or http://localhost:8000
