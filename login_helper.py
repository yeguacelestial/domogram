import sqlite3

class DBlogin:
    conexion = sqlite3.connect("usuarios.db")

    cursor = conexion.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS login" \
        "(usuario VARCHAR(100), pin INTEGER)")

    conexion.commit()
    conexion.close()