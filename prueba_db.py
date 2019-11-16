import sqlite3
import telepot
import os
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
    print ("Nombre: " + str(a[0]) + " - ID: " + str(a[1]) + " - Usuario: @" + str(a[2]))

print("\nUSUARIOS: ")
for u in users:
    print("Nombre: " + str(u[0]) + " - ID: " + str(u[1]) + " - Usuario: @" + str(u[2]))

print("\nINTENTOS: ")
for i in filtro:
    print("Nombre: " + str(i[0]) + " - ID: " + str(i[1]) + " - Usuario: @" + str(i[2]))

#Message handler
def gestor(msg):
    tipo_contenido, tipo_chat, id_chat = telepot.glance(msg)
    nombre = msg['from']['first_name']
    id_user = str(msg['from']['id'])

    if 'username' not in msg['from']:
        username = "No existe"

    else:    
        username = msg['from']['username']

    base = 'testdb.db'
    conexion = sqlite3.connect(base)
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    users = cursor.fetchall()
    users_list = []
    for u in users:
            users_list.append(str(u[2]))
    
    if username in users_list:
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

        #Si el contenido enviado es texto...
        if tipo_contenido == 'text':
            comando = msg['text']

            if comando == '/start':
                testbot.sendMessage(id_chat, "Bienvenido, " + nombre + "\n"
                + "Tu ID es: " + id_user + "\n"
                + "Tu usuario: " + username)

            #AGREGAR USUARIOS
            elif comando.startswith('/agregar '):
                parametro = msg['text'][9:]

                if parametro.startswith('@'):
                    testbot.sendMessage(id_chat, "Usuario: " + parametro)
                    conexion = sqlite3.connect("testdb.db")
                    cursor = conexion.cursor()
                    cursor.execute("SELECT (username) FROM usuarios")
                    users = cursor.fetchall()
                    users_list = []
                    for u in users:
                        users_list.append(str(u[0]))

                    if parametro[1:] in users_list:
                        testbot.sendMessage(id_chat, parametro + " ya se encuentra registrado.")

                    elif parametro[1:] not in users_list:
                        cursor.execute("INSERT INTO usuarios (username) VALUES (?)", (parametro[1:], ))
                        testbot.sendMessage(id_chat, "He registrado a {}".format(parametro))
                        conexion.commit()

                else:
                    testbot.sendMessage(id_chat, "Asegurate de que el usuario empiece con @ !")
                
            #ELIMINAR USUARIOS
            elif comando.startswith('/eliminar '):
                parametro = msg['text'][10:]

                if parametro.startswith('@'):
                    testbot.sendMessage(id_chat, "Eliminando usuario: " + parametro)
                    conexion = sqlite3.connect("testdb.db")
                    cursor = conexion.cursor()
                    cursor.execute("SELECT (username) FROM usuarios")
                    users = cursor.fetchall()
                    users_list = []
                    for u in users:
                        users_list.append(str(u[0]))

                    if parametro[1:] in users_list:
                        cursor.execute("DELETE FROM usuarios WHERE username = ?", (parametro[1:], ))
                        testbot.sendMessage(id_chat, "He aniquilado a {} del registro.".format(parametro))
                        conexion.commit()
                        conexion.close()

                    elif parametro[1:] not in users_list:
                        testbot.sendMessage(id_chat, "Mi estimadisimo {} no existe en el registro.".format(parametro))

                else:
                    testbot.sendMessage(id_chat, "Envia un usuario correcto, empezando con @.")

            
            elif comando == '/admins':
                base = 'testdb.db'
                conexion = sqlite3.connect(base)
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM admins")
                admins = cursor.fetchall()
                for a in admins:
                    testbot.sendMessage(id_chat, "Nombre: " + a[0] + " - ID: " + str(a[1]) + " - Administrador: @" + a[2])

            elif comando == '/usuarios':
                base = 'testdb.db'
                conexion = sqlite3.connect(base)
                cursor = conexion.cursor()
                cursor.execute("SELECT * FROM usuarios")
                users = cursor.fetchall()
                testbot.sendMessage(id_chat, "Usuarios del bot:")
                for u in users:
                    if str(u[0]) != 'None' or str(u[1]) != 'None':
                        testbot.sendMessage(id_chat, "Nombre: " + str(u[0]) + "\nID: " + str(u[1]) + "\nUsuario: @" + u[2])
                    else:
                        testbot.sendMessage(id_chat, "Nombre: Sin especificar\nID: Sin especificar\nUsuario: @" + u[2])

            elif comando == '/help' or comando == '/ayuda':
                testbot.sendMessage(id_chat, "La sección de ayuda estará disponible proximamente.")

            else:
                testbot.sendMessage(id_chat, "No entendi, " + nombre)
    
    else:
        testbot.sendMessage(id_chat, "Acceso denegado. No tienes permitido hacer eso!")

#Loop
testbot.message_loop(gestor)

while 1:
    time.sleep(100)
