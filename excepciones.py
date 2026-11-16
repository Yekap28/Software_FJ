
class ErrorSistema(Exception):
    """Excepción general del sistema."""


class DatoInvalidoError(ErrorSistema):
    """Se utiliza cuando un dato ingresado no es válido."""


class EstadoReservaError(ErrorSistema):
    """Se utiliza cuando una reserva no permite realizar una operación."""
