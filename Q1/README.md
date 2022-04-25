# Project Requirements
- PostgreSql

# Project Installation
Run the following command.
```
sudo apt install python3-pip python3-dev python3-django python3-virtualenv
```

Run the following command to download the project.

```
git clone https://github.com/fatihtufekci/EvrekaQ2.git
```

Run the following commands in order to install the virtual environment.
```sh
virtualenv -p python3 venv
source venv/bin/activate
```

Run the following command to install the required packages.

```sh
pip3 install -r requirements.txt 
```

Change .env.sample to .env and set its contents
```sh
mv .env.sample .env
```

Create PostgreSQl user and database. After migrate project database with following command.

```sh
python3 manage.py migrate
```

Create admin user with following command.

```sh
python3 manage.py createsuperuser
```

And run project.
```
python3 manage.py runserver
```

You can see the api documentation in following url
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)