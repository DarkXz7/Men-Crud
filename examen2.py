# Diccionario para almacenar clientes
clientes = {}

# Fcrear un nuevo cliente
def crearCliente():
    cedula = int(input("Ingrese la cédula del cliente: "))
    nombres = input("Ingrese los nombres del cliente: ")
    apellidos = input("Ingrese los apellidos del cliente: ")
    estado = input("Ingrese el estado del cliente (activo/inactivo): ")
    calificacion = float(input("Ingrese la calificación del cliente: "))

    clientes[cedula] = {
        'nombres': nombres,
        'apellidos': apellidos,
        'estado': estado,
        'calificacion': calificacion
    }
    print(f"Cliente con cédula {cedula} creado exitosamente.")

# leer un cliente por su cédula
def leerCliente():
    cedula = int(input("Ingrese la cédula del cliente que desea consultar: "))
    if cedula in clientes:
        print(f"Datos del cliente con cédula {cedula}:")
        print("Nombres:", clientes[cedula]['nombres'])
        print("Apellidos:", clientes[cedula]['apellidos'])
        print("Estado:", clientes[cedula]['estado'])
        print("Calificación:", clientes[cedula]['calificacion'])
    else:
        print(f"No se encontró cliente con cédula {cedula}.")

# actualizar los datos de un cliente por su cédula
def actualizarCliente():
    cedula = int(input("Ingrese la cédula del cliente que desea actualizar: "))
    if cedula in clientes:
        print(f"Ingrese los nuevos datos para el cliente con cédula {cedula}:")
        nuevos_nombres = input(f"Nombres ({clientes[cedula]['nombres']}): ")
        nuevos_apellidos = input(f"Apellidos ({clientes[cedula]['apellidos']}): ")
        nuevo_estado = input(f"Estado ({clientes[cedula]['estado']}): ")
        nueva_calificacion = float(input(f"Calificación ({clientes[cedula]['calificacion']}): "))

        nuevos_datos = {
            'nombres': nuevos_nombres if nuevos_nombres else clientes[cedula]['nombres'],
            'apellidos': nuevos_apellidos if nuevos_apellidos else clientes[cedula]['apellidos'],
            'estado': nuevo_estado if nuevo_estado else clientes[cedula]['estado'],
            'calificacion': nueva_calificacion if nueva_calificacion else clientes[cedula]['calificacion']
        }

        clientes[cedula].update(nuevos_datos)
        print(f"Datos del cliente con cédula {cedula} actualizados exitosamente.")
    else:
        print(f"No se encontró cliente con cédula {cedula}.")

# eliminar un cliente por su cédula
def eliminarCliente():
    cedula = int(input("Ingrese la cédula del cliente que desea eliminar: "))
    if cedula in clientes:
        del clientes[cedula]
        print(f"Cliente con cédula {cedula} eliminado correctamente.")
    else:
        print(f"No se encontró cliente con cédula {cedula}.")

def menu():
    while True:
        print("\n-- Menú Principal --")
        print("1. Crear Cliente")
        print("2. Leer Cliente")
        print("3. Actualizar Cliente")
        print("4. Eliminar Cliente")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            crearCliente()
        elif opcion == '2':
            leerCliente()
        elif opcion == '3':
            actualizarCliente()
        elif opcion == '4':
            eliminarCliente()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# darle candela
if  __name__ == "__main__":
    menu()



