from random import randint
from generador.model import Model
from generador.tipos_de_datos import (
    primer_nombre, apellido, direccion,
    cedula, fecha_de_nacimiento, roles,
    estado_civil, nivel_educacion, contrasena, email, celular,
    nombre_de_empresa, ruc, faker
)

User = Model()
User.agregar_atributos({
    "nombres": (primer_nombre, None),
    "apellidos": (apellido, None),
    "empresa": (randint, {"a":1, "b":100}),
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
User.copy_attribute("password_validator", "password")

Funcionalidad = Model()
Funcionalidad.agregar_atributos({
    "nombre": (faker.company, None),
    "descripcion": (faker.text, None)
})

Suscripcion = Model()
Suscripcion.agregar_atributos({
    "tipo": (faker.word, None),
    "fecha_emision": (faker.date_between, {
        "start_date": "-1y",
        "end_date": "today"
    }),
    "fecha_caducidad": (faker.date_between, {
        "start_date": "+1d",
        "end_date": "+1y"
    }),
    "precio": (faker.pydecimal, {
        "left_digits": 3,
        "right_digits":2,
        "positive":True
    })
})

Empresa = Model()
Empresa.agregar_atributos({
    "suscripcion": (randint, {"a":1, "b":100}),
    "nombre_comercial": (nombre_de_empresa, None),
    "ruc": (ruc, None),
    "direccion": (direccion, None),
    "telefono": (celular, None),
    "correo": (email, None),
})
