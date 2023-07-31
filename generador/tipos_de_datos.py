"""
Módulo para crear los siguientes tipos de datos:
    - nombres
    - cedulas
    - RUCs
    - direcciones
"""

from faker import Faker
from generador.cedula import generar_cedula_ecuatoriana
from generador.roles import EstadoCivil, NivelEducacion, Roles
from generador.celulares import generar_numero_celular_ecuatoriano_aleatorio
faker = Faker(
    ["es", "es_CO"]
)

nombres = faker.name
primer_nombre = faker.first_name
apellido = faker.last_name
direccion = faker.address
cedula = generar_cedula_ecuatoriana
fecha_de_nacimiento = faker.date_of_birth
roles = Roles.random
estado_civil = EstadoCivil.random
nivel_educacion = NivelEducacion.random
contrasena = faker.password
email = faker.email
celular = generar_numero_celular_ecuatoriano_aleatorio
