
from clientes import Cliente
from servicios import Servicio
from reservas import Reserva
from registro import registrar_evento, registrar_error


class SistemaGestion:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):

        try:
            if not isinstance(cliente, Cliente):
                raise TypeError("El objeto debe ser un cliente.")

            self.clientes.append(cliente)
            registrar_evento("Cliente registrado correctamente.")

        except Exception as error:
            registrar_error(f"Error al registrar cliente: {error}")
            raise

    def registrar_servicio(self, servicio):

        try:
            if not isinstance(servicio, Servicio):
                raise TypeError("El objeto debe ser un servicio.")

            self.servicios.append(servicio)
            registrar_evento("Servicio registrado correctamente.")

        except Exception as error:
            registrar_error(f"Error al registrar servicio: {error}")
            raise

    def registrar_reserva(self, reserva):

        try:
            if not isinstance(reserva, Reserva):
                raise TypeError("El objeto debe ser una reserva.")

            self.reservas.append(reserva)
            registrar_evento("Reserva registrada correctamente.")

        except Exception as error:
            registrar_error(f"Error al registrar reserva: {error}")
            raise
