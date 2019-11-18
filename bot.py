import telepot
import time
import serial
import sys
import os
import sqlite3
from dotenv import *

load_dotenv()
token = os.getenv('TOKEN')
ser = serial.Serial('/dev/ttyACM0', 115200)
bot = telepot.Bot(token)

print('Bot')
print('Esperando acciones...')

#Handle msg
def handle(msg):
    usuario = msg['from']['first_name']
    user_id = str(msg['from']['id'])
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text'):
        comando = msg['text']
        print('Comando: %s' % comando)

        if 'username' not in msg['from']:
            bot.sendMessage(chat_id, 'No tienes un nombre de usuario :-(, crea uno para continuar.')

        else:
            username = msg['from']['username']
            base = 'users.db'
            conexion = sqlite3.connect(base)
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios")
            users = cursor.fetchall()
            users_list = []
            for u in users:
                users_list.append(str(u[2]))

            if username in users_list:
                if '/start' in comando:
                    bot.sendMessage(chat_id, 'Nombre de usuario: @{}'.format(username))
                    bot.sendMessage(chat_id, '¡Tienes acceso! 👍')
                    bot.sendMessage(chat_id, '¡Hola, '
                        +usuario
                        +"! 🤓🤓🤓\n"
                        +"Soy Domogram, tu bot favorito! 😀😀😀"
                    )

                elif '/cuarto_on' in comando:
                    ser.write(b'Q')
                    bot.sendMessage(chat_id, "La luz del cuarto está encendida 🧐")

                elif '/cuarto_off' in comando:
                    ser.write(b'W')
                    bot.sendMessage(chat_id, "La luz del cuarto está apagada")

                elif '/estancia_on' in comando:
                    ser.write(b'E')
                    bot.sendMessage(chat_id, "La luz de la estancia está encendida 🧐")

                elif '/estancia_off' in comando:
                    ser.write(b'R')
                    bot.sendMessage(chat_id, "La luz de la estancia está apagada")

                elif '/bano_on' in comando:
                    ser.write(b'T')
                    bot.sendMessage(chat_id, "La luz del baño está encendida 🧐")

                elif '/bano_off' in comando:
                    ser.write(b'Y')
                    bot.sendMessage(chat_id, "La luz del baño está apagada")
                
                elif '/cocina_on' in comando:
                    ser.write(b'G')
                    bot.sendMessage(chat_id, "La luz de la cocina está encendida 🧐")

                elif '/cocina_off' in comando:
                    ser.write(b'H')
                    bot.sendMessage(chat_id, "La luz de la cocina está apagada")

                elif '/entrada_on' in comando:
                    ser.write(b'J')
                    bot.sendMessage(chat_id, "La luz de la entrada está encendida 🧐")

                elif '/entrada_off' in comando:
                    ser.write(b'K')
                    bot.sendMessage(chat_id, "La luz de la entrada está apagada")

                elif '/comedor_on' in comando:
                    ser.write(b'L')
                    bot.sendMessage(chat_id, "La luz del comedor está encendida 🧐")

                elif '/comedor_off' in comando:
                    ser.write(b'Z')
                    bot.sendMessage(chat_id, "La luz del comedor está apagada")

                elif '/humedad' in comando:
                    ser.write(b'X')
                    line = ser.readline()
                    bot.sendMessage(chat_id, b"Humedad: " + line)

                elif '/movimiento' in comando:
                    ser.write(b'V')
                    line = ser.readline()
                    bot.sendMessage(chat_id, b"Se detecto movimiento a la distancia: " + line + b"cm.")

                elif '/casa_on' in comando:
                    ser.write(b'U')
                    bot.sendMessage(chat_id, "Todas las luces estan encendidas. 🧐🧐🧐")

                elif '/casa_off' in comando:
                    ser.write(b'I')
                    bot.sendMessage(chat_id, "Todas las luces estan apagadas.")
                    
                elif '/temperatura' in comando:
                    ser.write(b'O')
                    line = ser.readline()
                    bot.sendMessage(chat_id, b"Temperatura: " + line)

                elif '/abrir' in comando:
                    ser.write(b'A')
                    bot.sendMessage(chat_id, "Abrí la casa. 🧐")

                elif '/cerrar' in comando:
                    ser.write(b'S')
                    bot.sendMessage(chat_id, "Cerré la casa.")

                elif '/reporte' in comando:
                    ser.write(b'P')
                    line = str(ser.readline())
                    bot.sendMessage(chat_id, "Reporte general: " + line)

                else:
                    bot.sendMessage(chat_id, "🤣🤣🤣 Comando invalido bro 💩💩💩")
            else:
                bot.sendMessage(chat_id, 'No tienes acceso al bot 😕😕😕')
                bot.sendMessage(chat_id, 'Sugiero que contactes al administrador: @hombrecelestial 🧐🧐🧐')
    
    else:
        bot.sendMessage(chat_id, "Bien jugado...no sé como reaccionar ante eso 🙃🙃🙃")

bot.message_loop(handle)

while 1:
    time.sleep(100)
