import random
import string

letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
