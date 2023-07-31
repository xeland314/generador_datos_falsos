import os
from dotenv import load_dotenv
import requests

from generador.model import Model
from generador.tipos_de_datos import (
    primer_nombre, apellido, direccion,
    cedula, fecha_de_nacimiento, roles,
    estado_civil, nivel_educacion, contrasena, email, celular
)

load_dotenv()
URL = os.getenv('URL')
TOKEN = os.getenv('TOKEN')

if __name__ == "__main__":
    mi_modelo = Model()
    mi_modelo.agregar_atributos({
        "nombres": (primer_nombre, None),
        "apellidos": (apellido, None),
        "empresa": (lambda: 1, None),
        "role": (roles, None),
        "cedula": (cedula, None),
        "email": (email, None),
        "direccion": (direccion, None),
        "telefono": (celular, None),
        "fecha_nacimiento": (fecha_de_nacimiento, {
            "minimum_age": 18,
            "maximum_age": 40
        }),
        "estado_civil": (estado_civil, None),
        "nivel_educacion": (nivel_educacion, None),
        "password": (contrasena, {"length": 10}),
    })
    mi_modelo.copy_attribute("password_validator", "password")

    headers = {'Authorization': TOKEN}
    for _ in range(5000):
        data = mi_modelo.generar_modelo()
        response = requests.post(URL, headers=headers, data=data)
        print(data)
