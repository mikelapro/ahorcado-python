from random import choice
import os
import dibujos
import palabras

palabra: str = ""
vidas = 0
MAX_VIDAS = 6
letras_ingresadas: list[str] = []
letras_correctas: list[str] = []
lista_resultado: str = ""


def obtener_palabra(lista_palabras: list[str]) -> str:
    """
    Obtiene una palabra al azar tomada de la lista de palabras especificada.

    Args:
        lista_palabras (str): Lista de palabras posibles.

    Returns:
        str: Una palabra al azar.
    """
    palabra_random: str = choice(lista_palabras)

    return palabra_random


def pedir_letra() -> str:
    """
    Pide una letra al usuario.

    Returns:
        str: La letra ingresada por el usuario.
    """
    letra: str = input("Ingrese una letra: ")
    letra = letra[0]

    return letra


def controlar_letra(letra_usuario: str) -> None:
    """
    Controla la letra ingresada por el usuario.

    Args:
        letra_usuario (str): La letra a controlar.
    """
    global vidas

    # Si repitió esta letra, descontar vida (no agregar a la lista de seleccionadas).
    if letra_usuario in letras_ingresadas:
        vidas -= 1
    else:
        # Agrega la letra ingresada en la lista de letras ingresadas (esto nos permite
        # verificar si repite la letra).
        letras_ingresadas.append(letra_usuario)

        # Controla que la letra esté en la palabra.
        if letra_usuario in palabra:
            letras_correctas.append(letra_usuario)
        else:
            vidas -= 1


def mostrar_resultado() -> None:
    """
    Muestra el dibujo del muñeco y el estado del juego.
    """
    # Limpia la consola.
    os.system("cls")

    # Dibujo.
    print(dibujos.get_dibujo(vidas))
    # print(f"Palabra:{palabra}")
    print(lista_resultado)

    print(f"Vidas: {vidas}.")
    print("")
    print(f"Letras ingresadas: {letras_ingresadas}.")
    print(f"Letras correctas: {letras_correctas}.")


def check_gano() -> bool:
    """
    Controla si ganó el juego.

    Returns:
        bool: True, si el usuario ya encontró todas las letras. De lo contrario, False.
    """
    global lista_resultado
    letras: list[str] = list(palabra)

    resultado: list[str] = [
        letra_resul if letra_resul in letras_correctas else "_"
        for letra_resul in letras
    ]

    lista_resultado = "".join(resultado)

    print(resultado)
    if "".join(resultado) == palabra:
        print("Ganaste >:C!")
        return True
    else:
        return False


def check_perdio() -> bool:
    """
    Controla si perdió el juego.

    Returns:
        bool: True, si el usuario se quedó sin vidas. De lo contrario, False.
    """
    if vidas == 0:
        print("Perdiste :D!")
        print(f"La palabra correcta era {palabra}")

        return True
    else:
        return False


def flujo_principal() -> None:
    """
    Controla el flujo principal del programa.
    """
    global vidas, palabra
    print("Andando.")
    vidas = MAX_VIDAS

    # Obtiene una palabra al azar tomada de la lista de palabras especificada.
    palabra = obtener_palabra(palabras.obtener_palabras())
    print(f"Palabra a descubrir: {palabra}.")

    #         true                 false
    while not check_gano() and not check_perdio():
        mostrar_resultado()

        # Le pide una letra al usuario.
        letra: str = pedir_letra()

        controlar_letra(letra)

        mostrar_resultado()


flujo_principal()
