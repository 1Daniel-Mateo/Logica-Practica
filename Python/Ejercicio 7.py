# Casas de Harry Potter

def howarst(h):
    # Pregutas con relacion a los animales
    resultado = sum(h)
    g = 10
    s = 15
    r = 20
    if resultado <=  g:
        house = "Gryffindor"
    elif resultado <= s:
        house = "Slytherin"
    elif resultado <= r:
        house = "Ravenclaw"
    else:
        house = "Hufflepuff"
    return f"Tu casa es {house}"

print("Soy el sombrero seleccionador  de Hogwarts, yo te dire cual es tu casa seleciona las opciones que te gusten: \n")
inicio = input("Escribe si para empezar \n")
datos = []

while inicio == "si":
    
    print("""Las respuestas son de a, b, c y d y cada una sumaran los puntos que determinaran tu casa:       
          
    ¿Cuánto valor te define?
    a. Soy valiente y me gusta correr riesgos
    b. Soy astuto y aprobecho mis recursos para lograr lo que quiero
    c. Soy inteligente y resolutivo
    d. Soy leal y me encanta trabajar en equipo""")
    respuesta = input(": ")
    if respuesta == "a":
        datos.append(4)
    elif respuesta == "b":
        datos.append(2)
    elif respuesta == "c":
        datos.append(3)
    elif respuesta == "d":
        datos.append(1)
    
    
    print("""¿Cual es tu cualidad mas destacada? 
    a.  Mi recilencia me permite resolver problemas complejos
    b.  Mi honor  me hace ser valiente y correr riesgos
    c.  Mi ambicion  me hace ser astuto y alcanzar  mis metas)
    d.  Mi horradez  me hace ser leal y trabajar en equipo""")
    respuesta = input(": ")
    if respuesta == "a":
        datos.append(1)
    elif respuesta == "b":
        datos.append(3)
    elif respuesta == "c":
        datos.append(2)
    elif respuesta == "d":
        datos.append(4)
        
    print("""¿Cual es tu aptitud mas destacada?
     a.  Mi habilidad para magia marcial
     b.  Mi habilidad en la creación de posiones
     c.  Mi habilidad de leer el futuro es un don unico
     d.  Mi habilidad como metamofomago es inigualable""")
    respuesta = input(": ")
    if respuesta == "a":
        datos.append(4)
    elif respuesta == "b":
        datos.append(2)
    elif respuesta == "c":
        datos.append(1)
    elif respuesta == "d":
        datos.append(3)
        

    print("""¿Cual es tu mayor miedo?
    a.   Mi mayor miedo es perder a mi familia
    b.   Mi mayor miedo es perder mi libertad
    c.   Mi mayor miedo es fracasar en mis objetivos
    d.   Mi mayor miedo es perder mi vida
    """)
    respuesta = input(": ")
    if respuesta == "a":
        datos.append(3)
    elif respuesta == "b":
        datos.append(2)
    elif respuesta == "c":
        datos.append(1)
    elif respuesta == "d":
        datos.append(4)
    
    print("""¿Que animal de estas casas se relaciona mas contigo?
    a.   El leon, un animal de poder y fuerza,  pero tambien de orgulloso y soberbio.
    b.   La serpiente,  un animal de astucia y habilidad, pero tambien de miedo y desconfian.
    c.   El halcon,  un animal de libertad y aventura, pero tambien agresiva  y despiadada.
    d.   El tejon,  un animal de coraje y curioso, pero tambien solitario y inquieto.
          """)
    respuesta = input(": ")
    if respuesta == "a":
        datos.append(1)
    elif respuesta == "b":
        datos.append(2)
    elif respuesta == "c":
        datos.append(4)
    elif respuesta == "d":
        datos.append(3)
    
    
    print(howarst(datos))
    
    inicio = input("Escribe si para volver a empezar o no para terminar \n")
    

    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    