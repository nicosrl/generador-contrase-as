import random
import string

print("¿Quieres generar una contraseña segura?")
respuesta = input("Responde si o no: ")

if respuesta.lower() == "si":

    print("generando contraseña...")

    longitud = int(input("¿De cuántos caracteres la querés?: "))

    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation

    todos = letras + numeros + simbolos

    contraseña = ''.join(random.choice(todos) for i in range(longitud))

    print("Tu contraseña es:", contraseña)

else:
    print("no se generó ninguna contraseña")
