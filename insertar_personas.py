import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

# ejecutar una consulta para insertar una nueva persona

cursor = personas_db.cursor()
sql = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"

valores = ("Juan", "Pérez", 30)

cursor.execute(sql, valores)
personas_db.commit() # confirmar los cambios en la base de datos

print(f'Se ha agregado el nuevo registro en la bd: {valores}')
cursor.close()
personas_db.close()
