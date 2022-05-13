#!/bin/python

shoes = {"name": "fanchy shoes", "price": 14900}


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    print(price)

apply_discount(shoes, 0.25)
