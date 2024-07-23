
def famosos():
    for i in range(1,100):
        multiplo = ("fizz" if i % 3 == 0 else "") + ("buzz" if i % 5 == 0  else "")
        print(multiplo or i)


famosos()