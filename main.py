from generador.model import Model
from generador.tipos_de_datos import (
    primer_nombre, apellido, direccion,
    cedula, fecha_de_nacimiento
)

if __name__ == "__main__":
    mi_modelo = Model()
    mi_modelo.agregar_atributos({
        "nombre": (primer_nombre, None),
        "apellido": (apellido, None),
        "cedula": (cedula, None),
        "direccion": (direccion, None),
        "fecha_de_nacimiento": (fecha_de_nacimiento, {
            "minimum_age": 18,
            "maximum_age": 20
        })
    })
    for _ in range(10):
        print(mi_modelo.generar_modelo())
