import random
import json


def factorial(n):
  return 1 if n == 0 else n * factorial(n - 1)


def big_array(size):
  to_return = []
  for _ in range(size):
    to_return.append(random.randrange(-999999, 999999))

  return to_return


def bubble_sort(arr):
  for i in range(0, len(arr) - 1):
    for j in range(len(arr) - 1):
      if arr[j] > arr[j + 1]:
        aux = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = aux

  return arr


def converter_massa_lunar(x):
  massa_lua = 6
  return x / massa_lua


def converter_massa_marcial(x):
  grav_terra = 9.81
  grav_marte = 3.71
  return (grav_terra / grav_marte) * x


def adicionar_livro(titulo):
  with open('biblioteca.json', 'r') as openfile:

    # Reading from json file
    livros = json.load(openfile)

  with open('biblioteca.json', 'w') as openfile:

    livros.append(titulo)
    json.dump(livros, openfile)


def remover_livro(titulo):
  with open('biblioteca.json', 'r') as openfile:

    # Reading from json file
    livros = json.load(openfile)

  with open('biblioteca.json', 'w') as openfile:
    livros.remove(titulo)
    json.dump(livros, openfile)


def listar_livros():
  with open('biblioteca.json', 'r') as openfile:

    # Reading from json file
    livros = json.load(openfile)
  return livros
