import random

def elegir_palabra():
    palabras = ['python', 'programacion', 'codigo', 'ahorcado', 'juego', 'desarrollador']
    return random.choice(palabras)

def mostrar_estado(palabra, letras_adivinadas):
    estado = ''.join([letra if letra in letras_adivinadas else '_' for letra in palabra])
    return estado

def jugar_ahorcado():
    palabra = elegir_palabra()
    letras_adivinadas = []
    intentos = 6
    
    print("¡Bienvenido al juego del Ahorcado!")
    print(mostrar_estado(palabra, letras_adivinadas))
    
    while intentos > 0:
        letra = input("Adivina una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue
        
        letras_adivinadas.append(letra)
        
        if letra in palabra:
            print("¡Correcto!")
        else:
            intentos -= 1
            print(f"Incorrecto. Te quedan {intentos} intentos.")
        
        estado = mostrar_estado(palabra, letras_adivinadas)
        print(estado)
        
        if '_' not in estado:
            print("¡Felicidades! Has adivinado la palabra.")
            break
    else:
        print(f"Lo siento, has perdido. La palabra era '{palabra}'.")

if __name__ == "__main__":
    jugar_ahorcado()
