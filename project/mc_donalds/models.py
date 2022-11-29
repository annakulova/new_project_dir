from django.db import models


class Order(models.Model):
    pass

# CREATE TABLE PRODUCTS (
# 	product id INT AUTO INCREMENT NOT NULL,
# 	name CHAR(255) NOT NULL,
# 	price FLOAT NOT NULL
# );


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)


class Staff(models.Model):
    pass


class ProductOrder(models.Model):
    pass