import random

def validar_cedula_ecuatoriana(id_number: str) -> bool:
    """
    Based on: https://publiblog-ec.blogspot.com/2019/01/verificador-cedula-ciudadania.html
    """
    # Check if the id_number has 10 digits
    if len(id_number) != 10:
        return False

    # Check if the first two digits are between 0 and 24 or equal to 30
    province_code = int(id_number[:2])
    if not (0 <= province_code <= 24 or province_code == 30):
        return False

    # Check if the third digit is less than or equal to 6
    third_digit = int(id_number[2])
    if third_digit > 6:
        return False

    # Calculate the verification digit using the Module 10 algorithm
    coefficients = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    verification_digit = int(id_number[9])
    total = 0
    for i in range(9):
        product = int(id_number[i]) * coefficients[i]
        if product >= 10:
            product -= 9
        total += product
    calculated_verification_digit = (total % 10 != 0) * (10 - total % 10)

    # Check if the calculated verification digit matches the given verification digit
    return calculated_verification_digit == verification_digit

def generar_cedula_ecuatoriana() -> str:
    """
    Based on: https://publiblog-ec.blogspot.com/2019/01/verificador-cedula-ciudadania.html
    """
    # Generate the first two digits (province code)
    province_code = random.randint(0, 24)
    if province_code == 0:
        province_code = 30
    id_number = str(province_code).zfill(2)

    # Generate the third digit
    third_digit = random.randint(0, 6)
    id_number += str(third_digit)

    # Generate the next six digits
    for _ in range(6):
        id_number += str(random.randint(0, 9))

    # Calculate the verification digit using the Module 10 algorithm
    coefficients = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    for i in range(9):
        product = int(id_number[i]) * coefficients[i]
        if product >= 10:
            product -= 9
        total += product
    verification_digit = (total % 10 != 0) * (10 - total % 10)

    # Add the verification digit to the id_number
    id_number += str(verification_digit)

    return id_number
