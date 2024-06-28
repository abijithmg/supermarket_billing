import pytest

from python.assignments.agrichain_assignment_abijithmg.app import Checkout

def test_scan_single_item():
    checkout = Checkout()
    checkout.scan('A')
    assert checkout.cart_items == {'A': 1}

def test_scan_multiple_items():
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('B')
    checkout.scan('A')
    assert checkout.cart_items == {'A': 2, 'B': 1}

def test_calculate_total_no_discount():
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('B')
    checkout.scan('C')
    total = checkout.calculate_total()
    assert total == 100

def test_calculate_total_with_discount():
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('A')
    checkout.scan('A')
    total = checkout.calculate_total()
    assert total == 130

def test_calculate_total_with_bulk_discount():
    checkout = Checkout()
    checkout.scan('B')
    checkout.scan('B')
    checkout.scan('B')
    total = checkout.calculate_total()
    assert total == 75

def test_calculate_total_with_mixed_items():
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('B')
    checkout.scan('A')
    checkout.scan('C')
    checkout.scan('B')
    total = checkout.calculate_total()
    assert total == 175

def test_calculate_total_with_empty_cart():
    checkout = Checkout()
    total = checkout.calculate_total()
    assert total == 0
