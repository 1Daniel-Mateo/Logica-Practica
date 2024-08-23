import random

def  almuerzos_semana(n):
     return random.sample(n,5)
    
lista_almuerzo = [input(f"{i+1}. Ingresa almuerzo: ")for i in range(10)]

    
print(almuerzos_semana(lista_almuerzo))


