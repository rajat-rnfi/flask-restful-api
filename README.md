# flask-restful-api
A Clean CRUD Architecture with Flask RestFul API.

This project is for Creating,Updating,Deleting & Viewing the Articles with its nested comments. It is RestFul API based project so you have to set it up on your system and read the documentation to run the project.

## Basic Folder Structur
> __init__.py

Handling all Flask Application and Database Configuration

> app.py

Flask Application Server.

> controller.py

The Application Layer that defines API controller & its logics, global exceptions and also Request/Response/Presenter/Validator adapters.

> helper.py

some helper function according to the project need

> models.py

The database models are defined here.

> urls.py

The Application Layer that defines API controller connectivity with its endpoints.

> raw

Database Structure and API collection backup.


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
> flask run
```
```
> http://127.0.0.1:5000/
```

## Documentation of APIs

openapi: 3.0.0
info:
  title: flask-restful-api-task
  version: 1.0.0
servers:
  - url: http://{{base_url}}articles
tags:
  - name: Articles
  - name: Comments
paths:
  /:
    get:
      tags:
        - Articles
      summary: list
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
    post:
      tags:
        - Articles
      summary: add
      requestBody:
        content:
          application/json:
            schema:
              type: object
              example:
                title: Test Title
                content: This is content of this Article
                author: rajat
                publication_date: '2024-06-20'
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
  /9:
    put:
      tags:
        - Articles
      summary: update
      requestBody:
        content:
          application/json:
            schema:
              type: object
              example:
                title: Test Title
                content: This is content of this Article
                author: rajat
                publication_date: '2024-06-20'
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
  /1:
    delete:
      tags:
        - Articles
      summary: delete
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
    get:
      tags:
        - Articles
      summary: detail
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
  /1/comments:
    post:
      tags:
        - Comments
      summary: add-comment
      requestBody:
        content:
          application/json:
            schema:
              type: object
              example:
                author: rajat
                content: Test Comment
      responses:
        '200':
          description: Successful response
          content:
            application/json: {}
