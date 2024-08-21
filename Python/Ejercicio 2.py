def sonAnagramas(p1,p2):
    # Convertir a minúsculas y ordenar las palabras
    p1 = "".join(sorted(p1.lower()));
    p2 = "".join(sorted(p2.lower()));
    # Devolver True si son anagramas, False en caso contrario
    resultado = ("Si son anagramas" if p1 == p2 and p1 != p2 else "Boll")
    print(resultado)

palabra1= input('Ingresa una palabra')
palabra2= input('Ingresa otra palabra')

sonAnagramas(palabra1,palabra2)