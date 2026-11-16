from clientes import Cliente
from sistema import SistemaGestion
from registro import registrar_evento, registrar_error
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import ErrorSistema

import tkinter as tk
from tkinter import messagebox


class Aplicacion:

    def __init__(self, ventana):
        self.sistema= SistemaGestion()

        self.ventana = ventana

        self.ventana.title("Software FJ - Gestión de Reservas")
        self.ventana.geometry("600x400")
        self.ventana.resizable(False, False)

        titulo = tk.Label(
            self.ventana,
            text="SOFTWARE FJ",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)

        subtitulo = tk.Label(
            self.ventana,
            text="Sistema de Gestión de Clientes, Servicios y Reservas",
            font=("Arial", 11)
        )
        subtitulo.pack(pady=10)

        boton_clientes = tk.Button(
            self.ventana,
            text="GESTIÓN DE CLIENTES",
            width=30,
            command=self.mostrar_clientes
        )
        boton_clientes.pack(pady=10)

        boton_servicios = tk.Button(
            self.ventana,
            text="GESTIÓN DE SERVICIOS",
            width=30,
            command=self.mostrar_servicios
        )
        boton_servicios.pack(pady=10)

        boton_reservas = tk.Button(
            self.ventana,
            text="GESTIÓN DE RESERVAS",
            width=30,
            command=self.mostrar_reservas
        )
        boton_reservas.pack(pady=10)

    
    def mostrar_clientes(self):

        ventana_clientes = tk.Toplevel(self.ventana)
        ventana_clientes.title("Gestión de Clientes")
        ventana_clientes.geometry("400x350")

        tk.Label(
            ventana_clientes,
            text="REGISTRO DE CLIENTES",
            font=("Arial", 14, "bold")
        ).pack(pady=15)

        tk.Label(ventana_clientes, text="Nombre completo:").pack()
        entrada_nombre = tk.Entry(ventana_clientes, width=35)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_clientes, text="Documento:").pack()
        entrada_documento = tk.Entry(ventana_clientes, width=35)
        entrada_documento.pack(pady=5)

        tk.Label(ventana_clientes, text="Correo electrónico:").pack()
        entrada_correo = tk.Entry(ventana_clientes, width=35)
        entrada_correo.pack(pady=5)

        tk.Button(
            ventana_clientes,
            text="REGISTRAR CLIENTE",
            command=lambda: self.guardar_cliente(
                entrada_nombre.get(),
                entrada_documento.get(),
                entrada_correo.get()
            )
        ).pack(pady=15)

        tk.Button(
            ventana_clientes,
            text="CONSULTAR CLIENTES",
            command=self.consultar_clientes
        ).pack(pady=5)



    
    def guardar_cliente(self, nombre, documento, correo):

        if not nombre or not documento or not correo:
            messagebox.showerror(
                "Error",
                "Todos los campos son obligatorios."
            )
            return

        try:
            identificador = len(self.sistema.clientes) + 1

            cliente = Cliente(
                identificador,
                nombre,
                documento,
                correo
            )

            self.sistema.registrar_cliente(cliente)

            registrar_evento(
                f"Cliente registrado: {nombre}"
            )

            messagebox.showinfo(
                "Registro",
                "Cliente registrado correctamente."
            )

        except Exception as error:
            registrar_error(f"Error al registrar cliente: {error}")
            messagebox.showerror("Error", str(error))
            

    def consultar_clientes(self):

        if not self.sistema.clientes:
            messagebox.showinfo(
                "Clientes",
                "No hay clientes registrados."
            )
            return

        informacion = ""

        for cliente in self.sistema.clientes:
            informacion += cliente.mostrar_informacion() + "\n"

        messagebox.showinfo(
            "Clientes registrados",
            informacion
        )


    def guardar_servicio(self, tipo, nombre, precio):

        if not nombre or not precio:
            messagebox.showerror(
                "Error",
                "Todos los campos son obligatorios."
            )
            return

        try:
            precio = float(precio)

            identificador = len(self.sistema.servicios) + 1

            if tipo == "Sala":
                servicio = ReservaSala(
                    identificador,
                    nombre,
                    precio
                )

            elif tipo == "Equipo":
                servicio = AlquilerEquipo(
                    identificador,
                    nombre,
                    precio
                )

            else:
                servicio = Asesoria(
                    identificador,
                    nombre,
                    precio
                )

            self.sistema.registrar_servicio(servicio)

            registrar_evento(
                f"Servicio registrado: {nombre}"
            )

            messagebox.showinfo(
                "Registro",
                "Servicio registrado correctamente."
            )

        except ValueError as error:
            registrar_error(f"Error al registrar servicio: {error}")
            messagebox.showerror("Error", str(error))
        

    
    def consultar_servicios(self):

        if not self.sistema.servicios:
            messagebox.showinfo(
                "Servicios",
                "No hay servicios registrados."
            )
            return

        informacion = ""

        for servicio in self.sistema.servicios:
            informacion += (
                f"{servicio.identificador} | "
                f"{servicio.describir_servicio()} | "
                f"Precio por hora: ${servicio.precio:,.0f}\n"
            )

        messagebox.showinfo(
            "Servicios registrados",
            informacion
        )

    
    def guardar_reserva(self, cliente, servicio, duracion):

        if not cliente or not servicio or not duracion:
            messagebox.showerror(
                "Error",
                "Todos los campos son obligatorios."
            )
            return

        try:
            identificador_cliente = int(cliente.split(" - ")[0])
            identificador_servicio = int(servicio.split(" - ")[0])
            duracion = float(duracion)

            cliente_encontrado = None
            servicio_encontrado = None

            for c in self.sistema.clientes:
                if c.identificador == identificador_cliente:
                    cliente_encontrado = c

            for s in self.sistema.servicios:
                if s.identificador == identificador_servicio:
                    servicio_encontrado = s

            if cliente_encontrado is None or servicio_encontrado is None:
                raise ValueError("Cliente o servicio no encontrado.")

            identificador = len(self.sistema.reservas) + 1

            reserva = Reserva(
                identificador,
                cliente_encontrado,
                servicio_encontrado,
                duracion
            )

            self.sistema.registrar_reserva(reserva)

            registrar_evento(
                f"Reserva registrada: {identificador}"
            )

            messagebox.showinfo(
                "Registro",
                "Reserva registrada correctamente."
            )

        except (ValueError, ErrorSistema) as error:
            registrar_error(f"Error al registrar reserva: {error}")
            messagebox.showerror("Error", str(error))

    
    def consultar_reservas(self):

        if not self.sistema.reservas:
            messagebox.showinfo(
                "Reservas",
                "No hay reservas registradas."
            )
            return

        informacion = ""

        for reserva in self.sistema.reservas:
            informacion += (
                f"{reserva.mostrar_informacion()}\n"
            )

        messagebox.showinfo(
            "Reservas registradas",
            informacion
        )
        
        
    
    def mostrar_servicios(self):

        ventana_servicios = tk.Toplevel(self.ventana)
        ventana_servicios.title("Gestión de Servicios")
        ventana_servicios.geometry("400x400")

        tk.Label(
            ventana_servicios,
            text="REGISTRO DE SERVICIOS",
            font=("Arial", 14, "bold")
        ).pack(pady=15)

        tk.Label(ventana_servicios, text="Tipo de servicio:").pack()

        tipo_servicio = tk.StringVar()
        tipo_servicio.set("Sala")

        opciones = tk.OptionMenu(
            ventana_servicios,
            tipo_servicio,
            "Sala",
            "Equipo",
            "Asesoría"
        )
        opciones.pack(pady=5)

        tk.Label(ventana_servicios, text="Nombre del servicio:").pack()
        entrada_nombre = tk.Entry(ventana_servicios, width=35)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_servicios, text="Precio por hora:").pack()
        entrada_precio = tk.Entry(ventana_servicios, width=35)
        entrada_precio.pack(pady=5)

        tk.Button(
            ventana_servicios,
            text="REGISTRAR SERVICIO",
            command=lambda: self.guardar_servicio(
                tipo_servicio.get(),
                entrada_nombre.get(),
                entrada_precio.get()
            )
        ).pack(pady=10)

        tk.Button(
            ventana_servicios,
            text="CONSULTAR SERVICIOS",
            command=self.consultar_servicios
        ).pack(pady=5)

    
    
    def mostrar_reservas(self):

        ventana_reservas = tk.Toplevel(self.ventana)
        ventana_reservas.title("Gestión de Reservas")
        ventana_reservas.geometry("450x550")

        tk.Label(
            ventana_reservas,
            text="REGISTRO DE RESERVAS",
            font=("Arial", 14, "bold")
        ).pack(pady=15)

        # Seleccionar cliente
        tk.Label(
            ventana_reservas,
            text="Cliente:"
        ).pack()

        cliente_seleccionado = tk.StringVar()

        lista_clientes = [
            f"{cliente.identificador} - {cliente.nombre}"
            for cliente in self.sistema.clientes
        ]

        if lista_clientes:
            cliente_seleccionado.set(lista_clientes[0])
        else:
            lista_clientes = ["No hay clientes registrados"]
            cliente_seleccionado.set(lista_clientes[0])

        tk.OptionMenu(
            ventana_reservas,
            cliente_seleccionado,
            *lista_clientes
        ).pack(pady=5)

        # Seleccionar servicio
        tk.Label(
            ventana_reservas,
            text="Servicio:"
        ).pack()

        servicio_seleccionado = tk.StringVar()

        lista_servicios = [
            f"{servicio.identificador} - {servicio.nombre}"
            for servicio in self.sistema.servicios
        ]

        if lista_servicios:
            servicio_seleccionado.set(lista_servicios[0])
        else:
            lista_servicios = ["No hay servicios registrados"]
            servicio_seleccionado.set(lista_servicios[0])

        tk.OptionMenu(
            ventana_reservas,
            servicio_seleccionado,
            *lista_servicios
        ).pack(pady=5)

        # Duración de la reserva
        tk.Label(
            ventana_reservas,
            text="Duración en horas:"
        ).pack()

        entrada_duracion = tk.Entry(
            ventana_reservas,
            width=30
        )
        entrada_duracion.pack(pady=5)

        # Registrar reserva
        tk.Button(
            ventana_reservas,
            text="REGISTRAR RESERVA",
            command=lambda: self.guardar_reserva(
                cliente_seleccionado.get(),
                servicio_seleccionado.get(),
                entrada_duracion.get()
            )
        ).pack(pady=10)

        # Consultar reservas
        tk.Button(
            ventana_reservas,
            text="CONSULTAR RESERVAS",
            command=self.consultar_reservas
        ).pack(pady=5)

        # Administrar reserva
        tk.Label(
            ventana_reservas,
            text="Administrar reserva",
            font=("Arial", 12, "bold")
        ).pack(pady=15)

        tk.Label(
            ventana_reservas,
            text="Número de reserva:"
        ).pack()

        entrada_reserva = tk.Entry(
            ventana_reservas,
            width=20
        )
        entrada_reserva.pack(pady=5)

        # Confirmar reserva
        tk.Button(
            ventana_reservas,
            text="CONFIRMAR RESERVA",
            command=lambda: self.confirmar_reserva(
                entrada_reserva.get()
            )
        ).pack(pady=5)

        # Cancelar reserva
        tk.Button(
            ventana_reservas,
            text="CANCELAR RESERVA",
            command=lambda: self.cancelar_reserva(
                entrada_reserva.get()
            )
        ).pack(pady=5)

        # Procesar reserva
        tk.Button(
            ventana_reservas,
            text="PROCESAR RESERVA",
            command=lambda: self.procesar_reserva(
                entrada_reserva.get()
            )
        ).pack(pady=5)

    def buscar_reserva(self, identificador):

        if not identificador:
            raise ValueError("Ingresa el número de reserva.")

        identificador = int(identificador)

        for reserva in self.sistema.reservas:
            if reserva.identificador == identificador:
                return reserva

        raise ValueError("Reserva no encontrada.")

    
    def confirmar_reserva(self, identificador):

        try:
            reserva = self.buscar_reserva(identificador)
            reserva.confirmar()

            registrar_evento("Reserva confirmada correctamente.")

            messagebox.showinfo(
                "Reserva",
                "Reserva confirmada correctamente."
            )

        except (ValueError, ErrorSistema) as error:
            registrar_error(f"Error al confirmar reserva: {error}")
            messagebox.showerror("Error", str(error))

    def cancelar_reserva(self, identificador):

        try:
            reserva = self.buscar_reserva(identificador)
            reserva.cancelar()

            registrar_evento("Reserva cancelada correctamente.")

            messagebox.showinfo(
                "Reserva",
                "Reserva cancelada correctamente."
            )

        except (ValueError, ErrorSistema) as error:
            registrar_error(f"Error al cancelar reserva: {error}")
            messagebox.showerror("Error", str(error))

    def procesar_reserva(self, identificador):

        try:
            reserva = self.buscar_reserva(identificador)
            costo = reserva.procesar()

            registrar_evento("Reserva procesada correctamente.")

            messagebox.showinfo(
                "Reserva procesada",
                f"Reserva procesada correctamente.\n"
                f"Costo total: ${costo:,.2f}"
            )

        except (ValueError, ErrorSistema) as error:
            registrar_error(f"Error al procesar reserva: {error}")
            messagebox.showerror("Error", str(error))


ventana = tk.Tk()

app = Aplicacion(ventana)

ventana.mainloop()