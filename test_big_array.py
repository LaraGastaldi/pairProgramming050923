import pytest
from main import big_array


def test_big_array_20000():
  assert len(big_array(20000)) == 20000

def test_big_array_100():
  assert len(big_array(100)) == 100