from zona_fit_db.cliente import Cliente
from zona_fit_db.cliente_dao import ClienteDAO

print("*** Clientes Zona Fit ***")
opcion = None

while opcion != 5:
    print(f'''
    1. Listar clientes
    2. Agregar cliente
    3. Actualizar cliente
    4. Eliminar cliente
    5. Salir
''')
    opcion = int(input("Ingrese una opcion(1-5): "))

    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print ('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)

    elif opcion == 2:
        print('\n*** Agregar Cliente ***')
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        membresia = input("Ingrese la membresia: ")
        cliente = Cliente(nombre = nombre, apellido = apellido, membresia = membresia)
        nuevo_cliente = ClienteDAO.insertar(cliente)
        print(f'Se ha agregado el cliente, registros afectados: {nuevo_cliente}')

    elif opcion == 3:
        print('\n*** Actualizar Cliente ***')
        id = int(input("Ingrese el id del cliente a actualizar: "))
        nombre = input("Ingrese el nuevo nombre: ")
        apellido = input("Ingrese el nuevo apellido: ")
        membresia = input("Ingrese la nueva membresia: ")
        cliente = Cliente(id = id, nombre = nombre, apellido = apellido, membresia = membresia)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f'Se ha actualizado el cliente, registros afectados: {clientes_actualizados}')

    elif opcion == 4:
        print('\n*** Eliminar Cliente ***')
        id = int(input("Ingrese el id del cliente a eliminar: "))
        cliente = Cliente(id = id)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f'Se ha eliminado el cliente, registros afectados: {clientes_eliminados}')