import sqlite3
import telepot
import sys
import os
import time
from dotenv import *

load_dotenv()

token_admin = os.getenv('TOKEN_ADMIN')
admin_bot = telepot.Bot(token_admin)

def gestion(msg):
    nombre = msg['from']['first_name']
    user_id = str(msg['from']['id'])
    tipo_contenido, tipo_chat, id_chat = telepot.glance(msg)

    if (tipo_contenido == 'text'):
        comando = msg['text']
        print("Comando: %s" % comando)

        if comando == '/start':
            admin_bot.sendMessage(id_chat, "Hola, " + nombre + "! Tu id es: " + user_id)
        
        elif comando == '/administradores':
            admin_bot.sendMessage(id_chat, "Usuarios administradores del bot:\n")
            conexion = sqlite3.connect("usuarios.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM admins")
            admins = cursor.fetchall()

            for admin in admins:
                admin_bot.sendMessage(id_chat, "NOMBRE: " + admin[0] + " - ID: " + str(admin[1]))

        else:
            admin_bot.sendMessage(id_chat, "Comando no reconocido.")

    else:
        admin_bot.sendMessage(id_chat, 'Soy listo, pero no más que tu. :-c')

#DB
conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

#Creacion de tablas y campos
#Usuarios del bot
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios" \
    "(nombre VARCHAR(100), id INTEGER)")

#Administradores
cursor.execute("CREATE TABLE IF NOT EXISTS admins" \
    "(nombre VARCHAR(100), id INTEGER)")

conexion.commit()
conexion.close()

admin_bot.message_loop(gestion)

while 1:
     time.sleep(100)