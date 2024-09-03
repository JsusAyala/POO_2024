import tkinter as tk
from tkinter import messagebox
from Clases.funciones import *  # Importamos las funciones y clases necesarias

class MotoApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Motos El Durango")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de bienvenida
        label_title = tk.Label(self, text="..::Motos El Durango::..", font=("Arial", 16))
        label_title.pack(pady=10)

        # Botones para cada opción del menú
        btn_motos = tk.Button(self, text="1. Motos", command=self.menu_motos)
        btn_motos.pack(pady=5)

        btn_clientes = tk.Button(self, text="2. Clientes", command=self.menu_clientes)
        btn_clientes.pack(pady=5)

        btn_empleados = tk.Button(self, text="3. Empleados", command=self.menu_empleados)
        btn_empleados.pack(pady=5)

        btn_ventas = tk.Button(self, text="4. Ventas", command=self.menu_ventas)
        btn_ventas.pack(pady=5)

        btn_tickets = tk.Button(self, text="5. Ticket de Ventas", command=self.menu_tickets)
        btn_tickets.pack(pady=5)

        btn_salir = tk.Button(self, text="6. Salir del programa", command=self.quit)
        btn_salir.pack(pady=20)

    # ========================== Menús principales ==========================
    def menu_motos(self):
        self.clear_window()
        label_motos = tk.Label(self, text="..::Motos::..", font=("Arial", 14))
        label_motos.pack(pady=10)

        btn_aniadir_moto = tk.Button(self, text="1. Añadir una moto", command=self.aniadir_moto)
        btn_aniadir_moto.pack(pady=5)

        btn_mostrar_catalogo = tk.Button(self, text="2. Mostrar el catálogo", command=self.mostrar_catalogo)
        btn_mostrar_catalogo.pack(pady=5)

        btn_actualizar_moto = tk.Button(self, text="3. Actualizar una moto", command=self.actualizar_moto)
        btn_actualizar_moto.pack(pady=5)

        btn_atras = tk.Button(self, text="4. Atrás", command=self.create_widgets)
        btn_atras.pack(pady=20)

    def menu_clientes(self):
        self.clear_window()
        label_clientes = tk.Label(self, text="..::Clientes::..", font=("Arial", 14))
        label_clientes.pack(pady=10)

        btn_aniadir_cliente = tk.Button(self, text="1. Añadir un cliente", command=self.aniadir_cliente)
        btn_aniadir_cliente.pack(pady=5)

        btn_mostrar_clientes = tk.Button(self, text="2. Mostrar clientes", command=self.mostrar_clientes)
        btn_mostrar_clientes.pack(pady=5)

        btn_actualizar_cliente = tk.Button(self, text="3. Actualizar cliente", command=self.actualizar_cliente)
        btn_actualizar_cliente.pack(pady=5)

        btn_atras = tk.Button(self, text="4. Atrás", command=self.create_widgets)
        btn_atras.pack(pady=20)

    # ========================== Menús de empleados, ventas y tickets ==========================
    def menu_empleados(self):
        self.clear_window()
        label_empleados = tk.Label(self, text="..::Empleados::..", font=("Arial", 14))
        label_empleados.pack(pady=10)

        btn_aniadir_empleado = tk.Button(self, text="1. Añadir un empleado", command=self.aniadir_empleado)
        btn_aniadir_empleado.pack(pady=5)

        btn_mostrar_empleados = tk.Button(self, text="2. Mostrar empleados", command=self.mostrar_empleados)
        btn_mostrar_empleados.pack(pady=5)

        btn_actualizar_empleado = tk.Button(self, text="3. Actualizar empleado", command=self.actualizar_empleado)
        btn_actualizar_empleado.pack(pady=5)

        btn_atras = tk.Button(self, text="4. Atrás", command=self.create_widgets)
        btn_atras.pack(pady=20)

    def menu_ventas(self):
        self.clear_window()
        label_ventas = tk.Label(self, text="..::Ventas::..", font=("Arial", 14))
        label_ventas.pack(pady=10)

        btn_registrar_venta = tk.Button(self, text="1. Registrar una venta", command=self.registrar_venta)
        btn_registrar_venta.pack(pady=5)

        btn_mostrar_ventas = tk.Button(self, text="2. Mostrar ventas", command=self.mostrar_ventas)
        btn_mostrar_ventas.pack(pady=5)

        btn_atras = tk.Button(self, text="3. Atrás", command=self.create_widgets)
        btn_atras.pack(pady=20)

    def menu_tickets(self):
        self.clear_window()
        label_tickets = tk.Label(self, text="..::Tickets de Ventas::..", font=("Arial", 14))
        label_tickets.pack(pady=10)

        btn_crear_ticket = tk.Button(self, text="1. Crear un ticket de venta", command=self.crear_ticket)
        btn_crear_ticket.pack(pady=5)

        btn_mostrar_tickets = tk.Button(self, text="2. Mostrar tickets de venta", command=self.mostrar_tickets)
        btn_mostrar_tickets.pack(pady=5)

        btn_atras = tk.Button(self, text="3. Atrás", command=self.create_widgets)
        btn_atras.pack(pady=20)

    # ========================== Funciones del menú de Motos ==========================
    def aniadir_moto(self):
        self.clear_window()
        label = tk.Label(self, text="Añadir una moto al sistema")
        label.pack(pady=10)

        marca_label = tk.Label(self, text="Marca")
        marca_label.pack()
        marca_entry = tk.Entry(self)
        marca_entry.pack()

        modelo_label = tk.Label(self, text="Modelo")
        modelo_label.pack()
        modelo_entry = tk.Entry(self)
        modelo_entry.pack()

        anio_label = tk.Label(self, text="Año")
        anio_label.pack()
        anio_entry = tk.Entry(self)
        anio_entry.pack()

        # Similarmente se pueden agregar más campos como cilindrada, precio, etc.
        btn_guardar = tk.Button(self, text="Guardar", command=lambda: self.guardar_moto(marca_entry.get(), modelo_entry.get(), anio_entry.get()))
        btn_guardar.pack(pady=10)

        btn_atras = tk.Button(self, text="Atrás", command=self.menu_motos)
        btn_atras.pack(pady=20)

    def guardar_moto(self, marca, modelo, anio):
        nueva_moto = Moto(id, marca, modelo, anio, 10000, "tipo", "200cc", "100hp", "Rojo", 5)
        nueva_moto.crear()
        messagebox.showinfo("Éxito", "Moto añadida correctamente")

    def mostrar_catalogo(self):
        self.clear_window()
        label = tk.Label(self, text="Mostrar Catálogo")
        label.pack(pady=10)

        # Etiqueta y campo de entrada para buscar por ID
        label_buscar = tk.Label(self, text="Buscar por ID:")
        label_buscar.pack(pady=5)
        entry_buscar = tk.Entry(self)
        entry_buscar.pack(pady=5)

        # Función para realizar la búsqueda
        def buscar_moto():
            moto_id = entry_buscar.get()  # Obtiene el ID ingresado
            motos = Moto.mostrar()  # Obtiene el catálogo completo

            # Limpia los resultados anteriores
            for widget in frame_resultados.winfo_children():
                widget.destroy()

            if motos:
                moto_encontrada = False         
                for moto in motos:
                    if str(moto[0]) == moto_id:  # Compara el ID de la moto
                        label_moto = tk.Label(frame_resultados, text=f"ID: {moto[0]}, Marca: {moto[1]}, Modelo: {moto[2]}, Año: {moto[3]}")
                        label_moto.pack()
                        moto_encontrada = True
                        break
            
                if not moto_encontrada:
                    label_no_motos = tk.Label(frame_resultados, text="No se encontró ninguna moto con ese ID.")
                    label_no_motos.pack()
            else:
                label_no_motos = tk.Label(frame_resultados, text="No se encontraron motos en el catálogo.")
                label_no_motos.pack()

        # Botón para buscar la moto
        btn_buscar = tk.Button(self, text="Buscar", command=buscar_moto)
        btn_buscar.pack(pady=5)

        # Frame para mostrar los resultados
        frame_resultados = tk.Frame(self)
        frame_resultados.pack(pady=10)

        # Botón para regresar al menú anterior
        btn_atras = tk.Button(self, text="Atrás", command=self.menu_motos)
        btn_atras.pack(pady=20)
        btn_atras = tk.Button(self, text="Atrás", command=self.menu_motos)
        btn_atras.pack(pady=20)

    def actualizar_moto(self):
        self.clear_window()
        label = tk.Label(self, text="Actualizar Moto")
        label.pack(pady=10)

        # Campo para ingresar el ID de la moto a actualizar
        label_id = tk.Label(self, text="Ingrese el ID de la moto a actualizar:")
        label_id.pack(pady=5)
        entry_id = tk.Entry(self)
        entry_id.pack(pady=5)

        # Frame para los campos de actualización (se mostrarán después de buscar la moto)
        frame_actualizacion = tk.Frame(self)
        frame_actualizacion.pack(pady=10)

        def buscar_moto_para_actualizar():
            moto_id = entry_id.get()
            motos = Moto.mostrar()  # Obtener todas las motos
        
            for moto in motos:
                if str(moto[0]) == moto_id:  # Si el ID coincide
                    # Limpia el frame en caso de que ya haya mostrado algo antes
                    for widget in frame_actualizacion.winfo_children():
                        widget.destroy()

                    # Mostrar los datos actuales y campos para actualizar
                    label_marca = tk.Label(frame_actualizacion, text="Marca actual:")
                    label_marca.pack()
                    entry_marca = tk.Entry(frame_actualizacion)
                    entry_marca.pack(pady=5)
                    entry_marca.insert(0, moto[1])  # Mostrar la marca actual

                    label_modelo = tk.Label(frame_actualizacion, text="Modelo actual:")
                    label_modelo.pack()
                    entry_modelo = tk.Entry(frame_actualizacion)
                    entry_modelo.pack(pady=5)
                    entry_modelo.insert(0, moto[2])  # Mostrar el modelo actual

                    label_anio = tk.Label(frame_actualizacion, text="Año actual:")
                    label_anio.pack()
                    entry_anio = tk.Entry(frame_actualizacion)
                    entry_anio.pack(pady=5)
                    entry_anio.insert(0, moto[3])  # Mostrar el año actual

                    # Botón para guardar las actualizaciones
                    btn_guardar = tk.Button(frame_actualizacion, text="Guardar cambios", 
                                         command=lambda: guardar_actualizaciones(moto_id, entry_marca.get(), entry_modelo.get(), entry_anio.get()))
                    btn_guardar.pack(pady=10)

                    break
            else:
                # Si no se encuentra la moto, se muestra un mensaje
                messagebox.showerror("Error", "No se encontró ninguna moto con ese ID.")
    
        def guardar_actualizaciones(moto_id, nueva_marca, nuevo_modelo, nuevo_anio):
            # Aquí podrías actualizar los datos de la moto en la base de datos o archivo
            moto_actualizada = Moto(moto_id, nueva_marca, nuevo_modelo, nuevo_anio, 10000, "tipo", "200cc", "100hp", "Rojo", 5)
            moto_actualizada.actualizar()  # Suponiendo que hay un método actualizar en la clase Moto
            messagebox.showinfo("Éxito", "Moto actualizada correctamente")
            self.menu_motos()  # Volver al menú de motos

        # Botón para buscar la moto
        btn_buscar = tk.Button(self, text="Buscar moto", command=buscar_moto_para_actualizar)
        btn_buscar.pack(pady=5)

        # Botón para regresar al menú anterior
        btn_atras = tk.Button(self, text="Atrás", command=self.menu_motos)
        btn_atras.pack(pady=20)


    # ========================== Funciones del menú de Clientes ==========================
    def aniadir_cliente(self):
        self.clear_window()

        label = tk.Label(self, text="Añadir un cliente al sistema")
        label.pack(pady=10)

        nombre_label = tk.Label(self, text="Nombre")
        nombre_label.pack()
        nombre_entry = tk.Entry(self)
        nombre_entry.pack()

        direccion_label = tk.Label(self, text="Dirección")
        direccion_label.pack()
        direccion_entry = tk.Entry(self)
        direccion_entry.pack()

        telefono_label = tk.Label(self, text="Teléfono")
        telefono_label.pack()
        telefono_entry = tk.Entry(self)
        telefono_entry.pack()

        # Botón para guardar el cliente
        btn_guardar = tk.Button(self, text="Guardar", command=lambda: self.guardar_cliente(nombre_entry.get(), direccion_entry.get(), telefono_entry.get()))
        btn_guardar.pack(pady=10)

        # Botón para regresar al menú anterior
        btn_atras = tk.Button(self, text="Atrás", command=self.menu_clientes)
        btn_atras.pack(pady=20)

    def guardar_cliente(self, nombre, direccion, telefono):
        nuevo_cliente = Cliente(id, nombre, direccion, telefono)  # Asume que la clase Cliente existe
        nuevo_cliente.crear()  # Método para guardar el cliente (debe estar definido en la clase Cliente)
        messagebox.showinfo("Éxito", "Cliente añadido correctamente")

    def aniadir_cliente(self):
        self.clear_window()

        label = tk.Label(self, text="Añadir un cliente al sistema")
        label.pack(pady=10)

        nombre_label = tk.Label(self, text="Nombre")
        nombre_label.pack()
        nombre_entry = tk.Entry(self)
        nombre_entry.pack()

        direccion_label = tk.Label(self, text="Dirección")
        direccion_label.pack()
        direccion_entry = tk.Entry(self)
        direccion_entry.pack()

        telefono_label = tk.Label(self, text="Teléfono")
        telefono_label.pack()
        telefono_entry = tk.Entry(self)
        telefono_entry.pack()

        #   Botón para guardar el cliente
        btn_guardar = tk.Button(self, text="Guardar", command=lambda: self.guardar_cliente(nombre_entry.get(), direccion_entry.get(), telefono_entry.get()))
        btn_guardar.pack(pady=10)

        # Botón para regresar al menú anterior
        btn_atras = tk.Button(self, text="Atrás", command=self.menu_clientes)
        btn_atras.pack(pady=20)

    def guardar_cliente(self, nombre, direccion, telefono):
        nuevo_cliente = Cliente(id, nombre, direccion, telefono)  # Asume que la clase Cliente existe
        nuevo_cliente.crear()  # Método para guardar el cliente (debe estar definido en la clase Cliente)
        messagebox.showinfo("Éxito", "Cliente añadido correctamente")

    def actualizar_cliente(self):
        self.clear_window()

        label = tk.Label(self, text="Actualizar un cliente")
        label.pack(pady=10)

        # Campo para ingresar el ID del cliente a actualizar
        id_label = tk.Label(self, text="ID del Cliente")
        id_label.pack()
        id_entry = tk.Entry(self)
        id_entry.pack()

        # Botón para buscar el cliente por ID
        btn_buscar = tk.Button(self, text="Buscar", command=lambda: self.buscar_cliente(id_entry.get()))
        btn_buscar.pack(pady=10)

        # Frame para mostrar los datos actuales del cliente
        self.frame_actualizar = tk.Frame(self)
        self.frame_actualizar.pack(pady=10)

        # Botón para regresar al menú anterior
        btn_atras = tk.Button(self, text="Atrás", command=self.menu_clientes)
        btn_atras.pack(pady=20)

    def buscar_cliente(self, cliente_id):
        cliente = Cliente.buscar_por_id(cliente_id)  # Se asume que existe este método en la clase Cliente
        if cliente:
            # Limpiar el frame antes de mostrar los datos del cliente
            for widget in self.frame_actualizar.winfo_children():
                widget.destroy()

            nombre_label = tk.Label(self.frame_actualizar, text="Nombre")
            nombre_label.pack()
            nombre_entry = tk.Entry(self.frame_actualizar)
            nombre_entry.insert(0, cliente[1])  # Insertar el nombre actual
            nombre_entry.pack()

            direccion_label = tk.Label(self.frame_actualizar, text="Dirección")
            direccion_label.pack()
            direccion_entry = tk.Entry(self.frame_actualizar)
            direccion_entry.insert(0, cliente[2])  # Insertar la dirección actual
            direccion_entry.pack()

            telefono_label = tk.Label(self.frame_actualizar, text="Teléfono")
            telefono_label.pack()
            telefono_entry = tk.Entry(self.frame_actualizar)
            telefono_entry.insert(0, cliente[3])  # Insertar el teléfono actual
            telefono_entry.pack()

            # Botón para actualizar los datos del cliente
            btn_actualizar = tk.Button(self.frame_actualizar, text="Actualizar", command=lambda: self.guardar_actualizacion(cliente_id, nombre_entry.get(), direccion_entry.get(), telefono_entry.get()))
            btn_actualizar.pack(pady=10)
        else:
            messagebox.showerror("Error", "Cliente no encontrado")

    def guardar_actualizacion(self, cliente_id, nombre, direccion, telefono):
        cliente.actualizar(cliente_id, nombre, direccion, telefono)  # Se asume que la clase Cliente tiene un método para actualizar
        messagebox.showinfo("Éxito", "Cliente actualizado correctamente")

    # ========================== Funciones del menú de Empleados ==========================
    def aniadir_empleado(self):
        messagebox.showinfo("Añadir Empleado", "Función de añadir empleado en desarrollo")

    def mostrar_empleados(self):
        messagebox.showinfo("Mostrar Empleados", "Función de mostrar empleados en desarrollo")

    def actualizar_empleado(self):
        messagebox.showinfo("Actualizar Empleado", "Función de actualizar empleado en desarrollo")

    # ========================== Funciones del menú de Ventas ==========================
    def registrar_venta(self):
        messagebox.showinfo("Registrar Venta", "Función de registrar venta en desarrollo")

    def mostrar_ventas(self):
        messagebox.showinfo("Mostrar Ventas", "Función de mostrar ventas en desarrollo")

    # ========================== Funciones del menú de Tickets ==========================
    def crear_ticket(self):
        messagebox.showinfo("Crear Ticket", "Función de crear ticket en desarrollo")

    def mostrar_tickets(self):
        messagebox.showinfo("Mostrar Tickets", "Función de mostrar tickets en desarrollo")

    # ========================== Métodos auxiliares ==========================
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = MotoApp()
    app.mainloop()
