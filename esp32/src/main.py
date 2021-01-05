from time import sleep
from Wifi import is_connected
from Server import Server
from TemperatureSensor import TemperatureSensor
from config import config

if not is_connected():
    print('No connection found, exiting...')
    exit()


sensor = TemperatureSensor(pin_id = config['sensor']['pin'])
server = Server(
    host = config['server']['host'],
    port = config['server']['port'],
)

while True:
    temperatures = sensor.read()
    if not temperatures:
        print('Error while reading temperatures, exiting...')
        exit()
    print('Temperatures read:', temperatures)
    
    server.post('sensor/' + config['sensor']['id'], { 'temperature': temperatures[0] })

    sleep(config['measure']['period'])
