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
    user_id = str(msg['from']['id'])
    content_type, chat_type, chat_id = telepot.glance(msg)

    if (content_type == 'text'):
        comando = msg['text']
        print('Comando: %s' % comando)

        if '/start' in comando:
            bot.sendMessage(chat_id, '¡Hola, '
                +usuario
                +"!\n"
                +"Tu id es: "+user_id
                +"\nSoy Domogram, tu bot favorito! :-), te muestro los comandos disponibles: " + "\n"
                +"/led1_on" + " - Enciendo la luz 1.\n"
                +"/led1_off" + " - Apagar la luz 1.\n"
                +"/led2_on" + " - Enciendo la luz 2.\n"
                +"/led2_off" + " - Apagar la luz 2.\n"
                +"/led3_on" + " - Enciendo la luz 3.\n"
                +"/led3_off" + " - Apagar la luz 3.\n"
                +"/humedad" + " - Te muestro la humedad en el ambiente.\n"
                +"/movimiento"
                + " - Si detecto movimiento, enciendo la luz de alerta.\n"
                +"/leds_on" + " - Encender todas las luces\n"
                +"/leds_off" + " - Apagar todas las luces\n"
                +"/temperatura" + " - Te muestro la temperatura\n"
                +"/reporte"
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
    
    else:
        bot.sendMessage(chat_id, "Es un bonito archivo, pero no soy lo suficientemente listo para procesarlo :-(")

bot.message_loop(handle)

while 1:
    time.sleep(100)
