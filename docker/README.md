Move the `docker-compose.yaml` and `Dockerfile` to the main directory and follow the instructions below:
## Installation
```
docker-compose run app django-admin startproject app .
```
Note: If on Linux you will need to adjust the file permissions as they are owned by root. To do so execute the following command
```
sudo chown -R $USER:$USER .
```

## Getting Started
```
docker-compose build
docker-compose up
```
Open another terminal and run the following commands to create the database superuser.
```
docker-compose exec app python manage.py migrate
docker-compose exec app bash
python manage.py createsuperuser --username admin --email admin
```
To run other django commands simply type:
```
docker-compose exec app [cmd]
```

Once the the following commands have been ran head on over back to the section `Setting up the Webpage` in the main README for further instructions.
