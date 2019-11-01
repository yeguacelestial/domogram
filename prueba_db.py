import sqlite3
import telepot
import os
from acceso_helper import TablasDB
import time
from dotenv import *

load_dotenv()
token_test = os.getenv('TOKEN_TEST')
testbot = telepot.Bot(token_test)

conexion = sqlite3.connect("testdb.db")
cursor = conexion.cursor()

#CREAR TABLAS
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios(
    nombre VARCHAR(100),
    id INTEGER
)
''')

#Fetch db
base = 'usuarios.db'
conexion = sqlite3.connect(base)
cursor = conexion.cursor()
admins_nombre = "SELECT nombre FROM admins"
usuarios_nombre = "SELECT nombre FROM usuarios"
cursor.execute(admins_nombre)
#print(cursor.fetchall()[0])
cursor.execute(usuarios_nombre)
#print(cursor.fetchall()[0])

def gestor(msg):
    tipo_contenido, tipo_chat, id_chat = telepot.glance(msg)
    nombre = msg['from']['first_name']

    #Grupos
    if tipo_chat == 'group':
        userinfo = testbot.getChat(id_chat)
        print("Tipo de chat: " + tipo_chat + "\n" + "ID: " + str(msg['from']['id']))

        if 'username' not in msg['from']:
            print("Nombre de usuario: No existe")

        else:
            print("Nombre de usuario: " + str(msg['from']['username']))

        print("Mensaje: " + str(msg['text']) + "\n")
            

    elif tipo_chat == 'private':
        print("Tipo de chat: " + tipo_chat + "\n" + "ID: " + str(msg['from']['id']))
        print("Nombre de usuario: " + str(msg['from']['username']))
        print ("Mensaje: " + msg['text'] + "\n")

    if tipo_contenido == 'text':
        comando = msg['text']

        if comando == '/start':
            testbot.sendMessage(id_chat, "Hola, " + nombre)
            conexion = sqlite3.connect("testdb.db")
            cursor = conexion.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios(
                nombre VARCHAR(100),
                id INTEGER
            )
            ''')
            cursor.execute("INSERT INTO usuarios (id) VALUES (?)", (id_chat, ))
            #cursor.execute("INSERT INTO usuarios (nombre) VALUES (?)", ())
            testbot.sendMessage(id_chat, "Id guardada en la base de datos.")
            conexion.commit()
            conexion.close()

        else:
            testbot.sendMessage(id_chat, "No entendi, " + nombre)

testbot.message_loop(gestor)

while 1:
    time.sleep(100)
