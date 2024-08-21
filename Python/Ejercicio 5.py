def primo(p):
    if  p <= 1:
        return False
    for i in range(2, int(p**0.5) + 1):
        if p % i == 0:
            return False
    return True  

def fibunochi(f):
    a,b  = 0,1
    while  b < f:
        a,b = a+b,a
    return b == f
 
def par(n):
    return n % 2 == 0



def verficar(v):
    return primo(v) and fibunochi(v) and par(v)


numero =  int(input('Digite um número: '))

if verficar(numero):
    print(f'{numero} es un número primo, fibonacci y es par')
else:
    print(f'{numero} no es primo, no es fibonacci y es impar')















