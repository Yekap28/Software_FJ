
from datetime import datetime


def registrar_evento(mensaje):

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open("registro.log", "a", encoding="utf-8") as archivo:
            archivo.write(f"{fecha} - EVENTO: {mensaje}\n")

    except OSError as error:
        print(f"No se pudo guardar el evento: {error}")

    else:
        print("Evento registrado correctamente.")

    finally:
        print("Finalizó el intento de registro.")


def registrar_error(mensaje):

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        with open("registro.log", "a", encoding="utf-8") as archivo:
            archivo.write(f"{fecha} - ERROR: {mensaje}\n")

    except OSError as error:
        print(f"No se pudo guardar el error: {error}")

    else:
        print("Error guardado en el registro.")

    finally:
        print("Finalizó el intento de registro del error.")
