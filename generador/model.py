"""
Módulo model.py

Este módulo tiene la finalidad de crear una clase base
a la cual se le puede añadir cierta cantidad de atributos para generar
un diccionario con esos atributos.
"""

from typing import Callable, Dict, Optional, Tuple

class Model:
    """Una clase para generar modelos con atributos definidos por el usuario.

    Los atributos se pueden agregar al modelo utilizando el método `agregar_atributo`.
    Cada atributo está asociado con un objeto callable (por ejemplo, una función)
    que genera el valor para ese atributo. El método `generar_modelo` se puede
    utilizar para generar un diccionario que represente una instancia del modelo,
    donde las claves son los nombres de los
    atributos y los valores se generan llamando a los objetos callable asociados.
    """

    def __init__(self) -> None:
        """Inicializa una nueva instancia de Model."""
        self.__atributos = {}
        self.__argumentos = {}

    def agregar_atributo(
        self, nombre: str, generador: Callable, config: Optional[dict] = None
    ) -> None:
        """Agrega un atributo al modelo.

        Args:
            nombre: El nombre del atributo.
            generador: Un objeto callable que genera el valor para el atributo.
            config: Un diccionario opcional de argumentos de palabras clave
                para pasar al objeto callable al generar el valor del atributo.
        """
        self.__atributos[nombre] = generador
        if config is not None:
            self.__argumentos[nombre] = config

    def agregar_atributos(
        self, atributos: Dict[str, Tuple[Callable, Optional[Dict]]]
    ) -> None:
        """Agrega múltiples atributos al modelo.

        Args:
            atributos: Un diccionario donde las claves son los nombres
                de los atributos y los valores son tuplas que
                contienen el objeto callable y el diccionario
                de configuración para cada atributo.
        """
        for nombre, (generador, config) in atributos.items():
            self.agregar_atributo(nombre, generador, config)

    def generar_modelo(self) -> dict:
        """Genera un diccionario que representa una instancia del modelo.

        Las claves en el diccionario son los nombres de los atributos
        y los valores se generan llamando a los objetos callable asociados.

        Returns:
            Un diccionario que representa una instancia del modelo.
        """
        resultado = {}

        for key, generador in self.__atributos.items():
            args = self.__argumentos.get(key)
            resultado[key] = generador() if args is None else generador(**args)
        return resultado
