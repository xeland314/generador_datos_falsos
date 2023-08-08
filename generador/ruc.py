import random

def generate_ruc():
    first_part = str(random.randint(1000000000, 9999999999))
    second_part = str(random.randint(0, 999)).zfill(3)
    return first_part + second_part
