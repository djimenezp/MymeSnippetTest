# Wharehouse TEST
El objetivo es desarrollar una aplicación para gestionar el stock de diferentes almacenes.
Como usuario quiero consultar y gestionar los diferentes almacenes.
Además debo poder añadir nuevas mercancías a dichos almacenes y gestionar pedidos para consumir dichos productos.
Dejamos de tu lado las decisiones técnicas, el único requisito es que el backend esté hecho en python (puedes elegir el
framework que quieras) y que el front sea web.

## Suposiciones:
* Un producto puede estar en un solo almacén
* Cada linea de pedido hace referencia a un solo producto
* No se pueden consumir mas productos que su stock en almacén
* No se pudden añadir mas productos si se completa la capacidad del alamacén

# Models:
## Warehouse
* location
* capacity
* current_inventory (property)
* products (Reversed)

## Product
* name
* sku
* ean
* stock
* warehouse (Foreign)

## Orders (Para consumir productos)
* status
* order_lines  (Reversed)

## OrderLine
* product (Foreign)
* order (Foreign)
* quantity

## Restock (para añadir nuevas mercancias)
* status
* restock_lines  (Reversed)

## RestockLine
* product (Foreign)
* order (Foreign)
* quantity

# Installation
### Dependencies
![Python](https://img.shields.io/badge/Python-3.9.6-greenyellow)
![Docker](https://img.shields.io/badge/Docker-3.9.2-blue)
![Django](https://img.shields.io/badge/Django-4.1.4-darkgreen)
![DjangoRestFramework](https://img.shields.io/badge/DjangoRestFramwork-3.13.1-darkred)

To clone the repository

```sh
git clone git@github.com:djimenezp/MymeSnippetTest.git .
```

To use in non-production environment

```sh
docker-compose up -d --build
```

Server url will be at http://localhost:8000/

Browsable Api will be at http://localhost:8000/api

Swagger doc will be at http://localhost:8000/swagger

Django admin will be at http://localhost:8000/admin

To run the tests

```sh
docker-compose exec web python manage.py test
```
To add an user for the django admin

```sh
docker-compose exec web python manage.py createsuperuser
```
