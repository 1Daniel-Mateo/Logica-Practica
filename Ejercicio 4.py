import random
import secrets
import string


character = string.ascii_letters + string.digits + string.punctuation

passR = [
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(string.digits),
    random.choice(string.punctuation)
]

while len(passR) < 8:
    passR.append(secrets.choice(character))

if  len(passR) > 16:
    passR[:16]
    
    

random.shuffle(passR)
result = "".join(passR)
print("Contraseña Generada", result)


