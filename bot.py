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
            base = 'testdb.db'
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
                    bot.sendMessage(chat_id, '🤓Verificando si estás en la base de datos...🤓')
                    bot.sendMessage(chat_id, '¡Tienes acceso! 👍')
                    bot.sendMessage(chat_id, '¡Hola, '
                        +usuario
                        +"!\n"
                        +"Tu id es: "+user_id
                        +"\nSoy Domogram, tu bot favorito! 😀😀😀, te muestro los comandos disponibles: " + "\n"
                        +"/led1_on" + " - Enciendo la luz 1.\n"
                        +"/led1_off" + " - Apagar la luz 1.\n"
                        +"/led2_on" + " - Enciendo la luz 2.\n"
                        +"/led2_off" + " - Apagar la luz 2.\n"
                        +"/led3_on" + " - Enciendo la luz 3.\n"
                        +"/led3_off" + " - Apagar la luz 3.\n"
                        +"/led4_on" + " - Enciendo la luz 4.\n"
                        +"/led4_off" + " - Apagar la luz 4.\n"
                        +"/led5_on" + " - Enciendo la luz 5.\n"
                        +"/led5_off" + " - Apagar la luz 5.\n"
                        +"/led6_on" + " - Enciendo la luz 6.\n"
                        +"/led6_off" + " - Apagar la luz 6.\n"
                        +"/humedad" + " - Te muestro la humedad en el ambiente.\n"
                        +"/movimiento"
                        + " - Si detecto movimiento, enciendo la luz de alerta.\n"
                        +"/leds_on" + " - Encender todas las luces\n"
                        +"/leds_off" + " - Apagar todas las luces\n"
                        +"/temperatura" + " - Te muestro la temperatura\n"
                        +"/abrir_puerta_principal" + " - Abro la puerta principal\n"
                        +"/cerrar_puerta_principal" + " - Cierro la puerta principal\n"
                        +"/abrir_puerta_cuarto" + " - Abro la puerta de tu cuarto\n"
                        +"/cerrar_puerta_cuarto" + " - Cierro la puerta del cuarto\n"
                        +"/reporte"
                        +" - Te muestro el estado de todos los dispositivos"+"\n"
                        +"/start"+" - Te vuelvo a mostrar este mensaje."
                    )

                elif '/led1_on' in comando:
                    ser.write(b'Q')
                    bot.sendMessage(chat_id, "Luz 1 encendida")

                elif '/led1_off' in comando:
                    ser.write(b'W')
                    bot.sendMessage(chat_id, "Luz 1 apagada")

                elif '/led2_on' in comando:
                    ser.write(b'E')
                    bot.sendMessage(chat_id, "Luz 2 encendida")

                elif '/led2_off' in comando:
                    ser.write(b'R')
                    bot.sendMessage(chat_id, "Luz 2 apagada")

                elif '/led3_on' in comando:
                    ser.write(b'T')
                    bot.sendMessage(chat_id, "Luz 3 encendida")

                elif '/led3_off' in comando:
                    ser.write(b'Y')
                    bot.sendMessage(chat_id, "Luz 3 apagada")
                
                elif '/led4_on' in comando:
                    ser.write(b'G')
                    bot.sendMessage(chat_id, "Luz 4 encendida")

                elif '/led4_off' in comando:
                    ser.write(b'H')
                    bot.sendMessage(chat_id, "Luz 4 apagada")

                elif '/led5_on' in comando:
                    ser.write(b'J')
                    bot.sendMessage(chat_id, "Luz 5 encendida")

                elif '/led5_off' in comando:
                    ser.write(b'K')
                    bot.sendMessage(chat_id, "Luz 5 apagada")

                elif '/led6_on' in comando:
                    ser.write(b'L')
                    bot.sendMessage(chat_id, "Luz 6 encendida")

                elif '/led6_off' in comando:
                    ser.write(b'Z')
                    bot.sendMessage(chat_id, "Luz 6 apagada")

                elif '/humedad' in comando:
                    ser.write(b'X')
                    line = ser.readline()
                    bot.sendMessage(chat_id, b"Humedad: " + line)

                elif '/movimiento' in comando:
                    ser.write(b'V')
                    line = ser.readline()
                    bot.sendMessage(chat_id, b"Se detecto movimiento a la distancia: " + line)

                elif '/leds_on' in comando:
                    ser.write(b'U')
                    bot.sendMessage(chat_id, "Todas las luces estan encendidas.")

                elif '/leds_off' in comando:
                    ser.write(b'I')
                    bot.sendMessage(chat_id, "Todas las luces estan apagadas.")
                    
                elif '/temperatura' in comando:
                    ser.write(b'O')
                    line = ser.readline()
                    bot.sendMessage(chat_id, b"Temperatura: " + line)

                elif '/abrir_puerta_principal' in comando:
                    ser.write(b'A')
                    bot.sendMessage(chat_id, "Abri la puerta principal.")

                elif '/cerrar_puerta_principal' in comando:
                    ser.write(b'S')
                    bot.sendMessage(chat_id, "Cerré la puerta principal.")

                elif '/abrir_puerta_cuarto' in comando:
                    ser.write(b'D')
                    bot.sendMessage(chat_id, "Abri la puerta de tu cuarto.")

                elif '/cerrar_puerta_cuarto' in comando:
                    ser.write(b'F')
                    bot.sendMessage(chat_id, "Cerré la puerta de tu cuarto.")

                elif '/reporte' in comando:
                    ser.write(b'P')
                    line = str(ser.readline())
                    bot.sendMessage(chat_id, "Reporte general: " + line)

                else:
                    bot.sendMessage(chat_id, "🤣🤣🤣 Comando invalido bro 💩💩💩")
            else:
                bot.sendMessage(chat_id, 'Acceso denegado. No estas registrado en la base de datos...😕😕😕')
                bot.sendMessage(chat_id, 'Sugiero que contactes al administrador del bot: @hombrecelestial 🧐🧐🧐')
    
    else:
        bot.sendMessage(chat_id, "Bien jugado...no sé como reaccionar ante eso 🙃🙃🙃")

bot.message_loop(handle)

while 1:
    time.sleep(100)
