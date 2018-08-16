![logo](https://i.ytimg.com/vi/s_ht4AKnWZg/maxresdefault.jpg)

# Flasky server

The goal of this project is to create a single flask server which can be use to deploy our machine learning models through an API.
This server can be deployed easily with docker. Working this way allow us to work only on IA and industrialize our work through this server whithout implementing a lot of codes.

## Prerequisites

You will need the following things properly installed on your computer. This installation is only for Linux Debian system.

- [Git](http://git-scm.com/)
- [Docker](https://www.docker.com/)
- [Docker-compose](https://docs.docker.com/compose/)

## Installation

This installation works only in Sopra Steria network (proxy configuration). If you want to use it in a public network, you need to remove all proxies confiurations.
Run following commands :

    $ git clone https://innersource.soprasteria.com/DataLab195/flasky.git
    $ cd flasky
    $ docker-compose up

Wait for building... You server is now running.

## Contribution

### Blueprint + FLask = application factory

You can contribute to this server by make it robust (handle errors, create home page, documentations...) or creating new API based on model that you implemented.
This server is based on blueprint package. if you friendly with application factory with flask you wont have any difficulties to contribute to this project. For those who don't know much about it :

Follow the same structure as api directory :
- Create a new folder in app
- Add a __init__.py 
- Add a route.py with all your url for your api
- If your application need a web page, add a hmtl file in /app/template/yourapplication/file.hmtl and use render_template function in your route.py
- Implement functions which will be used by your application in /app/yourappliation/model.py
- Don't forget to register your application in the server by updating /app/__init__.py file

__Ask for complete pdf tutorial for more information__

### How to code?

After cloning the repo, update any files to add your implementation. You will need to rebuild your image to see update on the server:

    $ docker-compose up --build

### How to test?

You can install the package httpie:

    $ pip install httpie

This python package simulate REST request, by using it you can test your API:

    $ http GET http://<ip_host_adress>:5001/api/prediction

This API is not implemented but you can test your server by using it.
