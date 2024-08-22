import random

lista_almuerzo = []

for i in range(10):
  ingreso = input("Ingresa almuerzo: ")
  lista_almuerzo.append(ingreso)  
  print(lista_almuerzo)


def  almuerzos_semana(n):
    random.shuffle(n)
    almuerzo = n[:5]
    print(almuerzo)
    
    
almuerzos_semana(lista_almuerzo)


