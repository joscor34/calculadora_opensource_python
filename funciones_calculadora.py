def sumar_n_numeros():
  numeros_a_sumar = int(input('Cuantos números quieres sumar: '))
  lista_numeros = []

  for numero in range(0, numeros_a_sumar):
    numero_a_sumar = float(input(f'Ingresa el numero {numero + 1} a sumar: '))
    lista_numeros.append(numero_a_sumar)
  
  return sum(lista_numeros)


def multiplicacion_n_numeros():
  resultado = 1
  numeros_a_multiplicar = int(input('Cuantos números quieres multiplicar: '))
  for numero in range (0, numeros_a_multiplicar):
    numeros_a_multiplicar = float(input(f'Ingresa el {numero + 1} a multiplicar: '))
    resultado *= numeros_a_multiplicar

  return resultado


def division_2_numeros():
  numerador = float(input('Ingresa el numerador: '))
  denominador = float(input('Ingresa el denominador: '))
  if denominador == 0:
    print('No puedes dividir entre 0')
    return None
  
  return numerador/denominador