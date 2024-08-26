def number_ramdom(a,c,m,s):
    x = s
    while True:
        x = (a * x + c) % m
        yield x
        
a = 1664525
c = 1013904223
m = 100
s = 123456789 


generador  = number_ramdom(a,c,m,s)

for i in range(0,100):
    print(next(generador))

