from backend.app import calculate
from backend.operators import add, subtract, divide, multiply
from pytest import raises

def test_add():
    """
    Ce test vérifie l'addition de deux nombres.
    :return:None
    """
    assert add(5, 4) == 9

def test_subtract():
    """
    Ce test vérifie la soustraction de deux nombres.
    :return: None
    """
    assert subtract(5, 4) == 1

def test_multiply():
    """
    Ce test vérifie la multiplication de deux nombres.
    :return: None
    """
    assert multiply(5, 4) == 20

def test_divide():
    """
    Ce test vérifie la division classique de deux nombres.
    :return: None
    """
    assert divide(5, 4) == 1.25

def test_divide_by_zero():
    """
    Vérifie que la division par zéro lève bien une exception ValueError.
    :return: None
    """
    with raises(ValueError):
        divide(0, 69)

def test_addition_negative_with_positive():
    """
    Vérifie le calcul d'une expression commençant par un nombre négatif via la fonction calculate.
    :return: None
    """
    assert calculate("-420 + 69") == -351.0

def test_calculate_invalid_format():
    """
    Vérifie que calculate lève une ValueError pour des formats d'expressions totalement invalides.
    :return: None
    """
    with raises(ValueError):
        calculate("+++10+ - 90 -")
