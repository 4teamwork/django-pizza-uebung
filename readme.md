# django-pizza-uebung
Dieses Projekt funktioniert mit python 3.7

## Installation
 
 ```bash
 git clone git@github.com:4teamwork/django-pizza-uebung.git
 cd django-pizza-uebung
 python3 -m venv .
 source ./bin/activate
 pip install -r requirements.txt
```
## Runserver

```bash
source ./bin/activate
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```