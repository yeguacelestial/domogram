import telepot
import time
import serial
import sys

ser = serial.Serial('/dev/ttyACM0', 11400)
bot = telepot.Bot('TOKEN')

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
            +"Reporte general"
            +" - Te muestro el estado de todos los dispositivos"+"\n"
            +"/start"+" - Lista de comandos."
        )

    elif 'Encender luz 1' in comando:
        ser.write('l1on')
        bot.sendMessage(chat_id, "Luz 1 encendida")

    elif 'Apagar luz 1' in comando:
        ser.write('l1off')
        bot.sendMessage(chat_id, "Luz 1 apagada")

    elif 'Encender luz 2' in comando:
        ser.write('l2on')
        bot.sendMessage(chat_id, "Luz 2 encendida")

    elif 'Apagar luz 2' in comando:
        ser.write('l2off')
        bot.sendMessage(chat_id, "Luz 2 apagada")

    elif 'Humedad' in comando:
        ser.write('hum')
        line = ser.readline()
        bot.sendMessage(chat_id, "Humedad: " + line)

    elif 'Movimiento' in comando:
        ser.write('mov')
        line = ser.readline()
        bot.sendMessage(chat_id, "Se detectó movimiento a la distancia: " + line)

    elif 'Encender todas las luces' in comando:
        ser.write('ledson')
        bot.sendMessage(chat_id, "Todas las luces estan encendidas.")

    elif 'Apagar todas las luces' in comando:
        ser.write('ledsoff')
        bot.sendMessage(chat_id, "Todas las luces estan apagadas.")
        
    elif 'Temperatura' in comando:
        ser.write('temp')
        line = ser.readline()
        bot.sendMessage(chat_id, "Temperatura: " + line)

    elif 'Reporte general' in comando:
        ser.write('report')
        line = ser.readline()
        bot.sendMessage(chat_id, "Reporte general: " + line)

    else:
        bot.sendMessage(chat_id, "Comando inválido.")

bot.message_loop(handle)

while 1:
    time.sleep(20)
