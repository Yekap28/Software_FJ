
from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, identificador, nombre, precio):
        self.identificador = identificador
        self.nombre = nombre

        # Validar que el precio sea un número mayor que cero

        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio <= 0:
            raise ValueError("El precio debe ser un número mayor que cero.")

        self.precio = precio

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass


class ReservaSala(Servicio):

    def calcular_costo(self, duracion, descuento=0):
        self.validar_parametros(duracion)

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        subtotal = self.precio * duracion
        valor_descuento = subtotal * descuento / 100
        total = subtotal - valor_descuento

        return total

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}"

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ValueError("La duración debe ser un número mayor que cero.")


class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion, descuento=0):
        self.validar_parametros(duracion)

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        subtotal = self.precio * duracion
        valor_descuento = subtotal * descuento / 100
        total = subtotal - valor_descuento

        return total

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}"

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ValueError("La duración debe ser un número mayor que cero.")


class Asesoria(Servicio):

    def calcular_costo(self, duracion, descuento=0):
        self.validar_parametros(duracion)

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or descuento < 0 or descuento > 100:
            raise ValueError("El descuento debe estar entre 0 y 100.")

        subtotal = self.precio * duracion
        valor_descuento = subtotal * descuento / 100
        total = subtotal - valor_descuento

        return total

    def describir_servicio(self):
        return f"Asesoría especializada: {self.nombre}"

    def validar_parametros(self, duracion):
        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ValueError("La duración debe ser un número mayor que cero.")
