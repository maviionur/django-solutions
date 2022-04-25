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


# Project Description 

I thought of different solution methods for this case. I added two of them to the project. These are included in the project as two different applications. The names of these applications are method1 and method2. Both methods were produced as a solution to the same problem and implemented differently from each other.


## Method1
In the first method, the models are defined as follows.


![method1_erd.png](https://github.com/maviionur/django-solutions/blob/main/Q2/images/method1_erd.png)




## Method2
I added this solution to the project as I thought it was a more extensible method. In the future, different attributes may be required for different operations. For this reason, I thought it would make more sense to keep the attributes in a jsonfield. Thus, when new attributes are required, the project can continue to work without making any changes to the model. And we can store values ​​like last_collection and collection_frequency under attributes.


![method2_erd.png](https://github.com/maviionur/django-solutions/blob/main/Q2/images/method2_erd.png)


