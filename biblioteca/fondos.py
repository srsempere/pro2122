"""
fondos.py: Módulo que implementa los fondos de la biblioteca.
copyright: (c) 2022 Ricardo Pérez <ricardo@iesdonana.org>
licencia: GPL-3 <https://www.gnu.org/licenses/gpl-3.0.txt>
"""

from abc import ABC, abstractmethod

class Fondo(ABC):
    __fondos = {}

    @staticmethod
    def _insertar(fondo):
        Fondo.__fondos[fondo.get_numero()] = fondo

    @staticmethod
    def _buscar(numero):
        return Fondo.__fondos.get(numero)

    @staticmethod
    def _borrar(fondo):
        del Fondo.__fondos[fondo.get_numero()]

    @staticmethod
    def _siguiente_numero_libre():
        return 1 if len(Fondo.__fondos) == 0 else \
               max(Fondo.__fondos) + 1

    @abstractmethod
    def es_prestable(self):
        ...

    def __init__(self):
        self.__numero = Fondo._siguiente_numero_libre()

    def get_numero(self):
        return self.__numero


class Prestable(Fondo, ABC):
    def es_prestable(self):
        return True

    @abstractmethod
    def plazo_devolucion(self):
        ...

    def __init__(self):
        super().__init__()
        self.__disponible = True

    def get_disponible(self):
        return self.__disponible

    def set_disponible(self, disponible):
        self.__disponible = disponible


class Libro(Prestable):
    def __init__(self, signatura, titulo, autor, num_paginas):
        super().__init__()
        self.set_signatura(signatura)
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_num_paginas(num_paginas)

    def plazo_devolucion(self):
        return 15

    def get_signatura(self):
        return self.__signatura

    def set_signatura(self, signatura):
        self.__signatura = signatura

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_num_paginas(self):
        return self.__num_paginas

    def set_num_paginas(self, num_paginas):
        self.__num_paginas = num_paginas


class Multimedia(Prestable):
    def __init__(self, titulo, formato):
        super().__init__()
        self.set_titulo(titulo)
        self.set_formato(formato)

    def plazo_devolucion(self):
        return 7

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_formato(self):
        return self.__formato

    def set_formato(self, formato):
        self.__formato = formato


class NoPrestable(Fondo, ABC):
    def es_prestable(self):
        return False


class Enciclopedia(NoPrestable):
    def __init__(self, signatura, titulo, autor, num_paginas):
        super().__init__()
        self.set_signatura(signatura)
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_num_paginas(num_paginas)

    def get_signatura(self):
        return self.__signatura

    def set_signatura(self, signatura):
        self.__signatura = signatura

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_num_paginas(self):
        return self.__num_paginas

    def set_num_paginas(self, num_paginas):
        self.__num_paginas = num_paginas
