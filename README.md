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

You can contribute
