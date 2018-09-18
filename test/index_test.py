import pytest
from ipynb.fs.full.index import *


def test_shopping_cart_class():
    example_shc = ShoppingCart()
    assert type(example_shc) == type(ShoppingCart())

def test_shopping_cart_initial_values():
    example_shc = ShoppingCart()
    assert example_shc._total == 0
    assert example_shc._items == []

def test_cash_register_initial_values_with_discount():
    example_shc = ShoppingCart(50)
    assert example_shc._total == 0
    assert example_shc._items == []
    assert example_shc._employee_discount == 50

def test_cash_register_decorator_methods():
    example_shc = ShoppingCart(50)
    assert example_shc.items == []
    assert example_shc.employee_discount == 50
    example_shc.total = 40
    example_shc.items = [{"name": "ice cream", "price": 5.00}]
    example_shc.employee_discount = 10
    assert example_shc.total == 40
    assert example_shc.items == [{"name": "ice cream", "price": 5.00}]
    assert example_shc._employee_discount == 10

def test_add_item_method():
    example_shc = ShoppingCart()
    assert example_shc.add_item("ice cream", 5.00) == 5.00
    assert example_shc.items == [{"name": "ice cream", "price": 5.00}]

def test_mean_item_price_method():
    example_shc = ShoppingCart()
    example_shc.add_item("ice cream", 5.00)
    example_shc.add_item("cereal", 10.00)
    example_shc.add_item("OJ", 4.00, 3)
    assert example_shc.mean_item_price() == 5.40

def test_median_item_price_odd_count_method():
    example_shc = ShoppingCart()
    example_shc.add_item("ice cream", 5.00)
    example_shc.add_item("cereal", 10.00)
    example_shc.add_item("OJ", 4.00, 3)
    assert example_shc.median_item_price() == 4.00

def test_median_item_price_even_count_method():
    example_shc_even_item_count = ShoppingCart()
    example_shc_even_item_count.add_item("ice cream", 5.00)
    example_shc_even_item_count.add_item("cereal", 10.00)
    example_shc_even_item_count.add_item("OJ", 4.00, 2)
    assert example_shc_even_item_count.median_item_price() == 4.50

def test_item_names_method():
    example_shc = ShoppingCart()
    example_shc.add_item("ice cream", 5.00)
    example_shc.add_item("cereal", 10.00)
    example_shc.add_item("OJ", 4.00, 3)
    assert example_shc.item_names() == ["ice cream", "cereal", "OJ", "OJ", "OJ"]

def test_apply_discount_method():
    example_shc = ShoppingCart(20)
    example_shc.total = 100
    assert example_shc.apply_discount() == 80
    assert example_shc.total == 100

def test_void_last_item_method():
    example_shc_void_last_item = ShoppingCart()
    example_shc_void_last_item.add_item("ice cream", 5.00)
    example_shc_void_last_item.add_item("cereal", 10.00)
    example_shc_void_last_item.add_item("OJ", 4.00, 2)
    example_shc_void_last_item.void_last_item()
    assert len(example_shc_void_last_item.items) == 3
    assert example_shc_void_last_item.total == 19.0
    while example_shc_void_last_item.items:
        example_shc_void_last_item.void_last_item()
    assert example_shc_void_last_item.void_last_item() == "There are no items in your cart!"
