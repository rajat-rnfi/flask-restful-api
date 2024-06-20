# flask-restful-api
A Clean CRUD Architecture with Flask RestFul API.

This project is for Creating,Updating,Deleting & Viewing the Articles with its nested comments. It is RestFul API based project so you have to set it up on your system and read the documentation to run the project.

## Basic Folder Structure
> app.py

Flask Application setup is there.

> db_config.py

SQLAlchemy DB configuration file

> helper.py

some helper function according to the project need

> main.py

The Application Layer that defines API controller & its endpoints, global exceptions and also Request/Response/Presenter/Validator adapters.

> models.py

The database models are defined here.


## Dependencies
* `flask`: Base Web Framework
* `SQLAlchemy`: For creating models and connectvity to mysql database
* `pytest`: Test Scripts
* `mysqlclient`: MySQL core library to handle mysql server
* `werkzeug`: Utility Library under Flask


## Run the project
```
> python -m venv env
```
```
For windows
> .\env\Scripts\activate
```
```
For Linux
> source env/bin/activate
```
```
> pip install -r requirements.txt
```
```
> python main.py
```

