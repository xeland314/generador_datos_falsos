from random import randint

def generar_numero_celular_ecuatoriano_aleatorio() -> str:
    return f"09{randint(0, 99999999):08d}"
