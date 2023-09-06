import pytest
from main import adicionar_livro, remover_livro, listar_livros


def test_ver_livro():
  livro = "senhor dos aneis"
  adicionar_livro(livro)
  
  assert listar_livros() == [livro]
  remover_livro(livro)
  assert listar_livros() == []