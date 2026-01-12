from zona_fit_db.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente (nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls, cursor):
        conexion = None
        try:
            conexion = Conexion().obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Error al seleccionar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion().obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al insertar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion().obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al actualizar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion().obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Error al eliminar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':

    # Insertar un nuevo cliente
    #cliente1 = Cliente(nombre='Alejandra', apellido='Tellez', membresia='300')
    #clientes_insertados = ClienteDAO.insertar(cliente1)
    #print(f'Clientes_insertados: {clientes_insertados}')

    # Actualizar un cliente existente
    #cliente_actualizar = Cliente(id=5, nombre='Alexa', apellido='Tellez', membresia='400')
    #clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
    #print(f'Clientes_actualizados: {clientes_actualizados}')

    # Eliminar un cliente existente
    cliente_eliminar = Cliente(id=6)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'Clientes_eliminados: {clientes_eliminados}')

    # Seleccionar Clientes
    clientes = ClienteDAO.seleccionar(None)
    for cliente in clientes:
        print(cliente)