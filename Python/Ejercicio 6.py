import random

def  almuerzos_semana(n):
     almuerzo = random.sample(n,5)
     return print(almuerzo)
    
lista_almuerzo = [input(f"{i+1}. Ingresa almuerzo: ")for i in range(10)]

    
almuerzos_semana(lista_almuerzo)


