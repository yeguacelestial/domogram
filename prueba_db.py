import sqlite3
import telepot
import os
from acceso_helper import TablasDB
import time
from dotenv import *
from collections import defaultdict

load_dotenv()
token_test = os.getenv('TOKEN_TEST')
testbot = telepot.Bot(token_test)

#Config db
base = 'testdb.db'
conexion = sqlite3.connect(base)
cursor = conexion.cursor()

#Create 'Usuarios' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios(
    nombre VARCHAR(100),
    id INTEGER,
    username VARCHAR(100)
)
''')

#Create 'Admins' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS admins(
    nombre VARCHAR(100),
    id INTEGER,
    username VARCHAR(100)
)
''')

#Create 'filtro' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS filtro(
    nombre VARCHAR(100),
    id INTEGER,
    username VARCHAR(100)
)
''')

conexion.commit()

#Fetch db
cursor.execute("SELECT * FROM admins")
admins = cursor.fetchall()

cursor.execute("SELECT * FROM usuarios")
users = cursor.fetchall()

cursor.execute("SELECT * FROM filtro")
filtro = cursor.fetchall()

#Print db
print("ADMINISTRADORES DEL BOT:")
for a in admins:
    print ("Nombre: " + a[0] + " - ID: " + str(a[1]) + " - Usuario: @" + str(a[2]))

print("\nUSUARIOS: ")
for u in users:
    print("Nombre: " + u[0] + " - ID: " + str(u[1]) + " - Usuario: @" + str(u[2]))

print("\nINTENTOS: ")
for i in filtro:
    print("Nombre: " + i[0] + " - ID: " + str(i[1]) + " - Usuario: @" + str(i[2]))

#Message handler
def gestor(msg):
    tipo_contenido, tipo_chat, id_chat = telepot.glance(msg)
    nombre = msg['from']['first_name']
    id_user = str(msg['from']['id'])
    username = msg['from']['username']

    #Grupos
    if tipo_chat == 'group':
        userinfo = testbot.getChat(id_chat)
        print("\nTipo de chat: " + tipo_chat + "\n" + "ID: " + id_user)

        if 'username' not in msg['from']:
            username = "No existe"
            print("Nombre de usuario: " + username)

        else:
            username = str(msg['from']['username'])
            print("Nombre de usuario: " + username)

        print("Mensaje: " + str(msg['text']) + "\n")
            

    elif tipo_chat == 'private':
        print("\nTipo de chat: " + tipo_chat + "\n" + "ID: " + id_user)
        print("Nombre de usuario: " + str(msg['from']['username']))
        print ("Mensaje: " + msg['text'] + "\n")

    if tipo_contenido == 'text':
        comando = msg['text']

        if comando == '/start':
            testbot.sendMessage(id_chat, "Bienvenido, " + nombre + "\n"
            + "Tu ID es: " + id_user + "\n"
            + "Tu usuario: " + username)

        elif comando == '/guardar':
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
        
        elif comando == '/fetch_admins':
            base = 'testdb.db'
            conexion = sqlite3.connect(base)
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM admins")
            admins = cursor.fetchall()
            testbot.sendMessage(id_chat, "ADMINS:")
            for a in admins:
                testbot.sendMessage(id_chat, "Nombre: " + a[0] + " - ID: " + str(a[1]))

        elif comando == '/fetch_users':
            base = 'testdb.db'
            conexion = sqlite3.connect(base)
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios")
            users = cursor.fetchall()
            testbot.sendMessage(id_chat, "USERS:")
            for u in users:
                testbot.sendMessage(id_chat, "Nombre: " + u[0] + " - ID: " + str(u[1]))

        else:
            testbot.sendMessage(id_chat, "No entendi, " + nombre)

#Loop
testbot.message_loop(gestor)

while 1:
    time.sleep(100)
