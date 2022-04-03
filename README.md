# Stores REST API using Flask
by Kallibek Kazbekov

Date: 3 Apr 2022 

---
# Summary

The API was developed using Flask-RESTful which is an extension for Flask that adds support for quickly building REST APIs. In this case, it works with the SQLAlchemy ORM library.

The API developed in this project allows making CRUD operations on stores and items in those stores.

All CRUD endpoints require a JSON Web Token (JWT) which can be obtained upon signing up ("/register") and authorization ("/Auth")

# Database and Data modeling

The database resides on Managed PostgreSQL from Heroku

![alt text](/data_model.png)

# Documentation
Documentation is published at: 

https://documenter.getpostman.com/view/18229026/UVyswvb2

# Deployment

The API is deployed with Heroku at https://stores-rest-api-kallibek.herokuapp.com/

# Packages used

Flask==2.0.3

Flask-JWT==0.3.2

Flask-RESTful==0.3.9

Flask-SQLAlchemy==2.5.1

gunicorn==20.1.0

psycopg2==2.9.3

PyJWT==1.4.2

SQLAlchemy==1.4.32

Werkzeug==2.0.3

