config = {
    'network': {
        'ssid': 'My WiFi',
        'password': 'mywifisecretpassword'
    },
    'server': { # This is an example server information and should be replaced with your actual server
        'host': '192.168.0.12',
        'port': 1880, # port used when using NodeRED
        'route': 'sensor' # if the route you wish to post to is /sensor
    },
    'sensor': { 'id': 'my_sensor_id', 'pin': 32 }, # using the pin 32 on the ESP32 board
    'measure': { 'period': 5 * 60 } #sample every 5min
}
