import pytest
from main import bubble_sort, big_array

def auxiliar(valores):
  valores_ordenados = valores.copy()
  valores_ordenados.sort()
  return valores_ordenados

def test_ordena_5():
  valores = [5, 3, 4, 1, 2]
  valores_ordenados = valores.copy()
  valores_ordenados.sort()
  assert bubble_sort(valores) == valores_ordenados

def test_ordena_big_array():
  valores = big_array(20)
  ordenados = auxiliar(valores)
  assert bubble_sort(valores) == ordenados