# skeleton_django# 

Basic skeleton for Django.


## Overview ##

### Prerequisites ###

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

### Install requirements ###

    ```bash
    cd {{ project_name }}
    pip install -r requirements.txt
    ```
    

### Sync database ###
    
    ```bash
    manage.py syncdb
    ```
    
    
### Running ###
    
    ```bash
    manage.py runserver
    ```
    

Open browser to http://127.0.0.1:8000 or http://localhost:8000
