import pytest #Importa la librería de pytest

from calculadora import sumar, dividir #Importa las funciones sumar y dividir del archivo calculadora

def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-2, -3) == -5

def test_dividir_exactamente():
    assert dividir(10, 2) == 5

def test_dividir_decimal():
    assert dividir(7, 2) == 3.5

def test_dividir_entre_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
