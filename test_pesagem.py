import pytest
from main import converter_massa_lunar, converter_massa_marcial

def test_peso_lua_10():
  assert converter_massa_lunar(10) == 10/6

def test_peso_marte_10():
  grav_terra = 9.81
  grav_marte = 3.71
  assert converter_massa_marcial(10) == (grav_terra/grav_marte) * 10
  






  