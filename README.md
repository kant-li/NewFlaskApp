# Taraxa Sandbox

## 1. Init Environment

Configs will be parsed from file `.env`, please create it and write in basic configs.
Or the app will use the default value in `config.py`.

An example of `.env` file:
```
# mysql
MYSQL_ADDRESS=127.0.0.1
MYSQL_PORT=3306
MYSQL_DATABASE=sandbox
MYSQL_USER=sandbox
MYSQL_PASSWORD=password

# redis
...
```

### 1.1 Database
MySQL and Redis will be needed.

If there is no database running, run one by docker:
```
> docker-compose up
```

Init MySQL by running the sql scripts:
```
> mysql -u your_user_name -p

mysql> source sql/add_user_pv.sql;
mysql> source sql/add_tables.sql;
```

## 2. Run Server
Init the python virtual environment and install packages:
```
> virtualenv venv
> source venv/bin/activate
> pip install -r requirements.txt
```

Start server:
```
> python manage.py runserver
```

## 3. Check the Api Page
API: http://localhost:5000/apidocs/

## 4. Development
Do remember to commit to a new branch for new features.

### 4.1 Run Tests
Run pytest:
```
> python -m pytest
```
