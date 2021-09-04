# Food-Delivery-Application
Food delivery application created using Python, Flask, RabbitMQ, Docker.This is a  Project implementing Food Delivery System and acting as connection between Restaurant and their customers. This project includes the creation of ID for individual order by using customer name, phone number and address.

## TO RUN
Install PyCharm. (Professional 2020.3+ required)

##Database setup

- Python v3.8.x
- [Poetry](https://python-poetry.org/)
- Pika
- RabbitMQ

All dependencies required for the python project including [flask web framework](https://flask.palletsprojects.com/en/1.1.x/) are  installed by poetry.

## Development Setup

1. Run `poetry install` to install the dependencies using poetry
2. Set the environment variables `FLASK_APP` and `FLASK_ENV` with the appropriate values based on the environment.
For example, in a *nix development environment following command can be used to set the environment variables.

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
```


## Starting the server

Start the flask server by running `flask run` from the terminal.

##Running the server on localhost
Open main.py application/food-delivery/main.py
Configure the python interpreter and run the application
Navigate the site

## Verification
You should be able to access the server at http://localhost:5000/

#Project setup using docker  

##Back-end Setup: 

    • Python v3.8.x  

    • Poetry

    • Rabbitmq  

    • Docker  


#Installation using Docker Compose: 

## commands required:
```
1) start containers  - docker-compose up  

2) stop containers   - docker-compose down

```
##Pytest
```
1) Go to Backend docker using sudo docker exec -it food-delivery-backend bash
2) use pytest command to run pytest
