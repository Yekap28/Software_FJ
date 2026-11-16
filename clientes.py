
from entidades import Entidad


class Cliente(Entidad):

    def __init__(self, identificador, nombre, documento, correo):

        super().__init__(identificador)

        if not nombre.strip():
            raise ValueError("El nombre es obligatorio.")

        if not documento.strip():
            raise ValueError("El documento es obligatorio.")

        if "@" not in correo or "." not in correo:
            raise ValueError("El correo no es válido.")

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    @property
    def correo(self):
        return self.__correo

    def mostrar_informacion(self):

        return (
            f"ID: {self.identificador} | "
            f"Nombre: {self.nombre} | "
            f"Documento: {self.documento} | "
            f"Correo: {self.correo}"
        )
