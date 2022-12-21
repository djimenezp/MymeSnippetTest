El objetivo es desarrollar una aplicación para gestionar el stock de diferentes almacenes.
Como usuario quiero consultar y gestionar los diferentes almacenes.
Además debo poder añadir nuevas mercancías a dichos almacenes y gestionar pedidos para consumir dichos productos.
Dejamos de tu lado las decisiones técnicas, el único requisito es que el backend esté hecho en python (puedes elegir el framework que quieras) y que el front sea web.

## Suposiciones:
* Un producto puede estar en un solo alamacén
* Cada linea de pedido hace referencia a un solo producto

# Models:
## Warehouse
### location
### capacity
### current_inventory
### products (Reversed)

## Product
### name
### sku
### ean
### stock
### warehouse (Foreign)
### order_lines (Reversed)

## Orders
### status
### stock:bool
### lines  (Reversed)

## Line
### product (Foreign)
### order  (Foreign)
### quantity

# Installation

### Dependencies
![Python](https://img.shields.io/badge/Python-3.9.2-greenyellow)
![Docker](https://img.shields.io/badge/Docker-3.9.2-blue)
![Django](https://img.shields.io/badge/Django-4.1.1-darkgreen)

Clone the repo 
```sh
git clone git@github.com:djimenezp/MymeSnippetTest.git .
```
For use in non-production environment 
```sh
docker-compose up -d --build
```
Server url will be at http://localhost:8000/
Browsable Api will be at http://localhost:8000/api
Swagger doc will be at http://localhost:8000/swagger

For run the tests
```sh
docker-compose exec web python manage.py test
```
