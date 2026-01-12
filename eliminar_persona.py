import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

# eliminar una persona existente

cursor = personas_db.cursor()
sql = "DELETE FROM personas WHERE id = %s"

valores = (4,)  # eliminar la persona con id = 4
print(f'Se va a eliminar el registro con id: {valores[0]}')

cursor.execute(sql, valores)
personas_db.commit()  # confirmar los cambios en la base de datos