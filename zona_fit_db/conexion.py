from mysql.connector import pooling, Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    HOST = 'localhost'
    DB_PORT = '3306'
    POOL_SIZE = 5
    POLL_NAME = 'zona_fit_pool'
    poll = None

    @classmethod
    def obtener_pool(cls):
        if cls.poll is None: # Se crea el pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POLL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    database=cls.DATABASE,
                    port=cls.DB_PORT
                )
                return cls.pool
            except Error as e:
                print(f'Error al crear el pool de conexiones: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


if __name__ == '__main__':
    # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(pool)

    # Obtenemos una conexion del pool
    conexion1 = pool.get_connection()
    print(conexion1)

    #Liberar la conexion
    Conexion.liberar_conexion(conexion1)
    print(f'Se ha liberado el objeto conexion 1')