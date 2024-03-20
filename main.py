from funciones_calculadora import sumar_n_numeros
from funciones_calculadora import multiplicacion_n_numeros
from funciones_calculadora import division_2_numeros


while True:
  print('''
  Bievenido a mi calculadora, por favor ingresa la opción que desees.
  --------------------------------------------------------------------
        
  1) Hacer una suma de N números.
  2) Hacer una multiplicación de N números
  3) Hacer una divisón de 2 números.
        
  0) Salir del programa.       
  ''')

  opcion = int(input('> '))

  if opcion == 0:
    break

  elif opcion == 1:
    resultado = sumar_n_numeros()
    print(f'El resultado de tu suma es {resultado}')
  
  elif opcion == 2:
    resultado = multiplicacion_n_numeros()
    print(f'El resultado es: {resultado}')

  elif opcion == 3:
    resultado = division_2_numeros()
    print(f'El resultado es: {resultado}')
  
  else:
    print('Ejecuta una opción válida :(')

  
print('Bye, gracias por usar mi calculadora')
