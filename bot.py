import telepot
import time
import serial
import sys
import os
from dotenv import *

load_dotenv()
token = os.getenv('TOKEN')
ser = serial.Serial('/dev/ttyACM0', 115200)
bot = telepot.Bot(token)

print('Bot')
print('Esperando acciones...')

def handle(msg):
    usuario = msg['from']['first_name']
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text'):
        comando = msg['text']
        print('Comando: %s' % comando)

        if '/start' in comando:
            bot.sendMessage(chat_id, 'Buen dia, '
                +usuario
                +"\n"+"Lista de comandos reconocibles: " + "\n"
                +"Encender luz 1" + "- Enciendo la luz 1.\n"
                +"Apagar luz 1" + "- Apagar la luz 1.\n"
                +"Encender luz 2" + "- Enciendo la luz 2.\n"
                +"Apagar luz 2" + "- Apagar la luz 2.\n" 
                +"Humedad" + "-Te muestro la humedad en el ambiente.\n"
                +"Movimiento"
                + "- Si detecto movimiento, enciendo la luz de alerta.\n"
                +"Encender todas las luces" + "- Encender todas las luces\n"
                +"Apagar todas las luces" + "- Apagar todas las luces\n"
                +"Temperatura" + "- Te muestro la temperatura\n"
                +"Reporte gene'){ral"
                +" - Te muestro el estado de todos los dispositivos"+"\n"
                +"/start"+" - Lista de comandos."
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

        elif '/humedad' in comando:
            ser.write(b'T')
            line = ser.readline()
            bot.sendMessage(chat_id, "Humedad: " + line)

        elif '/movimiento' in comando:
            ser.write(b'Y')
            line = ser.readline()
            bot.sendMessage(chat_id, "Se detecto movimiento a la distancia: " + line)

        elif '/leds_on' in comando:
            ser.write(b'U')
            bot.sendMessage(chat_id, "Todas las luces estan encendidas.")

        elif '/leds_off' in comando:
            ser.write(b'I')
            bot.sendMessage(chat_id, "Todas las luces estan apagadas.")
            
        elif '/temperatura' in comando:
            ser.write(b'O')
            line = ser.readline()
            bot.sendMessage(chat_id, "Temperatura: " + line)

        elif '/reporte' in comando:
            ser.write(b'P')
            line = ser.readline()
            bot.sendMessage(chat_id, "Reporte general: " + line)

        else:
            bot.sendMessage(chat_id, "Comando invalido.")

bot.message_loop(handle)

while 1:
    time.sleep(100)