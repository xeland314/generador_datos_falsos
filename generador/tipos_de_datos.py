"""
Módulo para crear los siguientes tipos de datos:
    - nombres
    - cedulas
    - RUCs
    - direcciones
"""

from faker import Faker
from generador.cedula import generar_cedula_ecuatoriana

faker = Faker(
    ["es", "es_CO"]
)

nombres = faker.name
primer_nombre = faker.first_name
apellido = faker.last_name
direccion = faker.address
cedula = generar_cedula_ecuatoriana
fecha_de_nacimiento = faker.date_of_birth
