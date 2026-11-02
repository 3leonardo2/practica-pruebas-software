import pytest
from calculadora import sumar, restar, multiplicar, dividir

def test_sumar_positivos():
    assert sumar(2, 3) == 5

def test_sumar_negativos():
    assert sumar(-2, -3) == -5

def test_restar_positivos():
    assert restar(10, 4) == 6

def test_restar_con_resultado_negativo():
    assert restar(3, 8) == -5

def test_restar_con_cero():
    assert restar(7, 0) == 7

def test_multiplicar_positivo_por_negativo():
    assert multiplicar(5, -3) == -15

def test_multiplicar_dos_negativos():
    assert multiplicar(-4, -2) == 8

def test_multiplicar_por_cero():
    assert multiplicar(-6, 0) == 0

def test_dividir_cero_entre_numero():
    assert dividir(0, 5) == 0

def test_dividir_cero_entre_negativo():
    assert dividir(0, -5) == 0

@pytest.mark.parametrize("a, b", [
    ("a", 2),
    (2, "b"),
    ("#", "@"),
    (None, 3),
    ([1], 2),
])

def test_entradas_no_numericas_lanzan_error(a, b):
    with pytest.raises(TypeError):
        sumar(a, b)
    with pytest.raises(TypeError):
        restar(a, b)
    with pytest.raises(TypeError):
        multiplicar(a, b)
    with pytest.raises(TypeError):
        dividir(a, b)

def test_mensaje_de_error_en_validacion():
    with pytest.raises(TypeError, match="Solo se permiten números"):
        sumar("x", 1)
