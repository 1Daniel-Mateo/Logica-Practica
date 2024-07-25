
#* Agregas los primeros valores de la sucesion de fibonaci que son 0 y 1
a1,b1 = 0,1

#? Agregas f permite formatear el contenido y trataria los datos como una cadena literal
print(f'{a1},{b1}', end=', ')

#* Uso de un for para que se repita en un rango de 50, se sume los datos y se almacenen sobre si mismo

#! Nota importante el (end=', ') para que se organize de manera horizontal
for i in range(50):
    a1,b1 = a1+b1,a1
    print(a1, end=', ')


