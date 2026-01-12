import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="personas_db"
)

# ejecutar una consulta para seleccionar todas las personas

cursor = personas_db.cursor()
cursor.execute("SELECT * FROM personas")
resultado = cursor.fetchall()

for fila in resultado:
    print(fila)

cursor.close()
personas_db.close()