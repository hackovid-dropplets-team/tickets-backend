# main

Projecte participant a la Hackovid, hackató ciutadana per afrontar el confinament pel COVID-19.

```bash
python3 -m venv ./venv-dropplets
source venv-dropplets/bin/activate
pip install -r requirements.txt
```

## Migrate

````bash
cd tickets-backend
python manage.py makemigrations
python manage.py migrate
````

## Create superuser

````bash
cd tickets-backend
python manage.py createsuperusercrea
````

## Serve

````bash
cd tickets-backend
python manage.py runserve
````
