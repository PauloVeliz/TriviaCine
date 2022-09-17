# Importa la librería 'random'
import random

# Importa la librería 'time'
import time

# Declara constantes para colores de texto
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# Inicio Trivia en True y variable que almacenará el número de intentos que el usuario juege la Trivia
inicia_Trivia = True
intentos = 0

# Texto de bienvenida
print("Bienvenido a mi trivia Cine")
print("¿Te consideras un amante del cine?")

time.sleep(1) # Espera 1 segundo

# Solicita nombre del participante
nombre = input("\nIngresa tu nombre: ")

# Mientras el valor de inicia_Trivia = True, se repetirá.
while inicia_Trivia == True:

  # Cuantifica los intentos que se juega la Trivia
  intentos += 1

  # Inicia variable puntaje
  puntaje = random.randint(0, 10)

  print(f"\n{nombre}, comenzarás con",puntaje,"puntos.")
  time.sleep(1) # Espera 1 segundo

  if intentos <= 1:
    # Instrucciones sobre como jugar
    # Uso de la cadena f para usar una variable y mostrar el texto dentro de esta variable, además no tener el problema de tener un spacio después del nombre y antes de la coma.
    print(f"\nHola {nombre}, responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:")
    time.sleep(2)
  else:
    print(f"Es estupendo que te estés divirtiendo!")

  Preguntas = ["¿Quién dijo: 'Hitler me ha copiado el bigote'?", "¿En Cuántas películas habladas actuó Charlie Chaplin?", "¿En qué país pasó sus últimos años de vida Charlie Chaplin?"]
  
  LetrasAlter = ["a","b","c","d","p"]
  
  Alternativas = [["Cantinflas","Charlie Chaplin", "Eugenio Dérbez", "Roberto Gomez Bolaños"],["5", "6", "10", "50"],["Alemania", "Inglaterra", "Suecia", "Suiza"]]
  
  Respuestas = ["b","a","d"]

  Infadc = [["Cantinflas ganó el Globo de Oro a mejor actor de comedia en 1956.","b", "Su mayor éxito de Eugenio Dérbez es: No se aceptan devoluciones.", "Roberto Gomez Bolaños produjo el muy conocido: 'El Chavo del 8'"],["a", "Estuviste muy cera.", "Buen intento.", "¿Estás bromeando?"],["Su castillo más famoso de Alemania es el Castillo de Neuschwanstein", "Trájica noticia para Inglaterra, el fallecimiento de la Reina Isabel II.", "A los suecos les encanta el McDonalds.", "d"]]

  Operador = [[1,"b",3,2],["a",1,2,3],[3,2,1,"d"]]

  Rpta = ["","",""]
  
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")

  for i in range(len(Preguntas)):
    
    print("\n" + str(i+1) + ")" + Preguntas[i])
    for j in range(4):
      print(LetrasAlter[j] + ")" + Alternativas[i][j])

    Rpta[i] = input("\nTu respuesta: ")

    # Valida si la respuesta está dentro de las alternativas 
    while Rpta[i] not in LetrasAlter:
      print(MAGENTA + "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: " + RESET)
      Rpta[i] = input()

    # Verifica respuesta para asignar puntaje
    if Rpta[i] == LetrasAlter[-1]:
      puntaje += 100
      print(YELLOW + "\n" + nombre + " haz hallado el mensaje secreto! \nRecibes una bonificación de 100 puntos." + RESET)
    elif Rpta[i] == Respuestas[i]:
      puntaje += 10
      print(f"{GREEN}\nRespuesta correcta {nombre}!{RESET}")
    else:
      n = LetrasAlter.index(Rpta[i])
      
      if Operador[i][n] == 1:
        puntaje += 5
      elif Operador[i][n] == 2:
        puntaje -= 5
      elif Operador[i][n] == 3:
        puntaje /= 2
      
      print(f"{RED}\nIncorrecto {nombre}!{RESET}")
      print(CYAN + Infadc[i][n])

    if i < len(Preguntas)-1:
      print(BLUE + "Tu puntaje actual es: " + str(puntaje) + RESET)

  print(GREEN,"\nGracias",nombre,"por jugar mi trivia, alcanzaste",puntaje,"puntos.",RESET)

  time.sleep(1)

  print(YELLOW + "\n¿Deseas intentar la trivia nuevamente?" + RESET)
  repetir_Trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  time.sleep(2)

  if repetir_Trivia != "si":  # != significa "distinto"
    print(f"\n{nombre}, espero que lo hayas pasado bien, hasta pronto!")
    inicia_Trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.