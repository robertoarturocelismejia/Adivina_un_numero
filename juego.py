# juego.py
from utils import generar_numero_aleatorio
def jugar():
 print("Estoy pensando en un número del 1 al 10. ¿Puedes adivinarlo? te reto!")
 numero_secreto = generar_numero_aleatorio(1, 10)
 intentos = 0
 while True:
 respuesta = input("Ingresa tu número por favor: ")
 if not respuesta.isdigit():
 print("Por favor, ingresa cualquier valor numérico.")
 continue
 numero_ingresado = int(respuesta)
 intentos += 1
 if numero_ingresado < numero_secreto:
 print("Demasiado bajo, intenta de nuevo por favor.\n")
 elif numero_ingresado > numero_secreto:
 print("Demasiado alto, intenta de nuevo por favor.\n")
 else:
 print(f"¡Felicidades! Adivinaste el número en {intentos} # de intento(s).")
 break
def despedida():
 print("\nGracias por jugar. ¡Hasta la próxima!")
