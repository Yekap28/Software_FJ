
from entidades import Entidad
from excepciones import DatoInvalidoError, EstadoReservaError, ErrorSistema


class Reserva(Entidad):

    def __init__(self, identificador, cliente, servicio, duracion):

        super().__init__(identificador)

        if duracion <= 0:
            raise DatoInvalidoError(
                "La duración debe ser mayor que cero."
            )

        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    def confirmar(self):

        if self.__estado != "Pendiente":
            raise EstadoReservaError(
                "La reserva no se puede confirmar."
            )

        self.__estado = "Confirmada"

    def cancelar(self):

        if self.__estado == "Cancelada":
            raise EstadoReservaError(
                "La reserva ya está cancelada."
            )

        self.__estado = "Cancelada"

    def procesar(self):

        if self.__estado != "Confirmada":
            raise EstadoReservaError(
                "La reserva debe estar confirmada."
            )

        try:
            return self.__servicio.calcular_costo(self.__duracion)

        except Exception as error:
            raise ErrorSistema(
            "No fue posible calcular el costo de la reserva."
        ) from error



    def mostrar_informacion(self):

        return (
            f"Reserva: {self.identificador} | "
            f"Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )
