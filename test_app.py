import pytest
from app import Checkout

def test_scan_single_item(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', open('/dev/null'))
    checkout = Checkout()
    checkout.scan('A')
    assert checkout.cart_items == {'A': 1}
    # import pdb; pdb.set_trace()
    captured = capsys.readouterr()
    assert captured.out == ''

def test_scan_multiple_items(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', open('/dev/null'))
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('B')
    checkout.scan('A')
    assert checkout.cart_items == {'A': 2, 'B': 1}
    captured = capsys.readouterr()
    # assert captured.out()

def test_calculate_total_no_discount(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', open('/dev/null'))
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('B')
    checkout.scan('C')
    total = checkout.calculate_total()
    assert total == 100
    captured = capsys.readouterr()
    assert captured.out.strip() == ''

def test_calculate_total_with_discount(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', open('/dev/null'))
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('A')
    checkout.scan('A')
    total = checkout.calculate_total()
    assert total == 130
    captured = capsys.readouterr()
    assert captured.out.strip() == ''

def test_calculate_total_with_bulk_discount(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', open('/dev/null'))
    checkout = Checkout()
    checkout.scan('B')
    checkout.scan('B')
    checkout.scan('B')
    total = checkout.calculate_total()
    assert total == 75
    captured = capsys.readouterr()
    assert captured.out.strip() == ''

def test_calculate_total_with_mixed_items(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', open('/dev/null'))
    checkout = Checkout()
    checkout.scan('A')
    checkout.scan('B')
    checkout.scan('A')
    checkout.scan('C')
    checkout.scan('B')
    total = checkout.calculate_total()
    assert total == 165
    captured = capsys.readouterr()
    assert captured.out.strip() == ''

def test_calculate_total_with_empty_cart(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', open('/dev/null'))
    checkout = Checkout()
    total = checkout.calculate_total()
    assert total == 0
    captured = capsys.readouterr()
    assert captured.out.strip() == ''