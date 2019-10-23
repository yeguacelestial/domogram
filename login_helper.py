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
        
        else:
            admin_bot.sendMessage(id_chat, "Comando no reconocido.")

    else:
        admin_bot.sendMessage(id_chat, 'Soy listo, pero no más que tu. :-c')

    #DB
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS login" \
        "(nombre VARCHAR(100), pin INTEGER)")

    conexion.commit()
    conexion.close()

admin_bot.message_loop(gestion)

while 1:
     time.sleep(100)