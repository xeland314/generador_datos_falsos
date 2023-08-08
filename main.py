import os
from dotenv import load_dotenv
import requests

from models import Empresa, Funcionalidad, Suscripcion, User

load_dotenv()
URL = os.getenv('URL')

class NoTokenException(Exception):
    """Raises if there's not a token from  the api"""

def get_token() -> str:
    """
    Generate an authentication token by sending a POST request
    to the specified URL with the provided username and password credentials.

    Returns:
    - A string representing the authentication token.
    """
    values = {
        'username': os.getenv('USERNAME'),
        'password': os.getenv('PASSWORD')
    }
    try:
        resp = requests.post(
            f"{URL}/api_generate_token/",
            data=values,
            timeout=5
        )
    except requests.exceptions.RequestException as exception:
        print("Error: ", exception)
    if resp.status_code == 200:
        return resp.json()['token']
    raise NoTokenException('Failed to generate token')

def generar_empresas(n: int, headers):
    for _ in range(n):
        data = Empresa.generar_modelo()
        response = requests.post(
            f"{URL}/empresas/api/v1/empresas/",
            headers=headers,
            data=data,
            timeout=5
        )
        if response.status_code == 201:
            print(data)

def generar_suscripciones(n: int, headers):
    for _ in range(n):
        data = Suscripcion.generar_modelo()
        response = requests.post(
            f"{URL}/empresas/api/v1/suscripciones/",
            headers=headers,
            data=data,
            timeout=5
        )
        if response.status_code == 201:
            print(data)

def generar_funcionalidades(n: int, headers):
    for _ in range(n):
        data = Funcionalidad.generar_modelo()
        response = requests.post(
            f"{URL}/api/v1/funcionalidades/",
            headers=headers,
            data=data,
            timeout=5
        )
        if response.status_code == 201:
            print(data)

def generar_usuarios(n: int, headers):
    for _ in range(n):
        data = User.generar_modelo()
        response = requests.post(
            f"{URL}/usuarios/api/v1/perfiles/",
            headers=headers,
            data=data,
            timeout=5
        )
        if response.status_code == 201:
            print(data)

if __name__ == "__main__":
    HEADERS = {'Authorization': f"Token {get_token()}"}
    generar_funcionalidades(20, HEADERS)
