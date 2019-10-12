import telepot
import time
import serial
import sys

ser = serial.Serial('/dev/ttyACM0', 11400)

print('Bot')
print('Esperando acciones...')

def handle(msg):
    usuario = msg['from']['first_name']

content_type, chat_type, chat_id = telepot.glance(msg)

if (content_type == 'text'):
    comando = msg['text']
    print('Comando: %s' % comando)

if '/start' in comando:
    bot.sendMessage(chat_id, 'Buen día, ',
        +userName
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
        +"Reporte general"
        +" - Te muestro el estado de todos los dispositivos"+"\n"
        +"/start"+" - Lista de comandos."
    )


