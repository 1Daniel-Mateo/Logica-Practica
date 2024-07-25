
#*Definimos la funcion llamada famosos
def famosos():
    #*Definimos un bucle for con los que sus valores van desde 1 a 50
    for i in range(1,100):
        #? Usamos una funcion ternaria pra genera las condiciones para  que se imprima el buzz si es multiplo de 5
        #? y el fizz si es multiplo de 3
        
        multiplo = ("fizz" if i % 3 == 0 else "") + ("buzz" if i % 5 == 0  else "")
        #* Imprimimos el valor de i y el valor de multiplo, asignamos or para que en caso si los multiplos son de ambos
        #* se imprima fizzbuzz
        
        print(multiplo or i)

#? Llamada de la función
famosos()