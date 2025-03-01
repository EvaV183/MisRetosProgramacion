"""
/*
Dificultad: Fácil
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""

def fizzbuzz():
   
  print("NÚMEROS DEL 1 AL 100")
  print("---------------------")

  for number in range(1, 101):
      if number % 3 == 0 and number % 5 == 0: #debe ir primero por ambos porque si no entraria en los multiplos de 3 o de 5
        print("fizzbuzz")
      elif number % 3 == 0:
        print("fizz")
      elif number % 5 == 0:
        print("buzz")
      else:
        print(number)

fizzbuzz()
