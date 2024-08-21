import random
import secrets
import string

character = string.ascii_letters + string.digits + string.punctuation

passR = [
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(string.digits),
    random.choice(string.punctuation)
]+ [secrets.choice(character) for _ in range(8,16)]

random.shuffle(passR)
result = "".join(passR[:16])
print("Contraseña Generada", result)


