import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

# actualizar una persona existente

cursor = personas_db.cursor()
sql = "UPDATE personas SET nombre = %s, apellido = %s, edad = %s WHERE id = %s"

valores = ("Victoria", "Flores", 45, 4)  # actualizar la persona con id = 4
cursor.execute(sql, valores)
personas_db.commit()  # confirmar los cambios en la base de datos

print(f'Se ha actualizado el registro en la bd: {valores}')
cursor.close()
personas_db.close()