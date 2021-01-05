import network


def connect_to_wifi(ssid, password):

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Wifi connection successful!')
    print('Network config:', sta_if.ifconfig())
    
    
def is_connected():
    sta_if = network.WLAN(network.STA_IF)
    return sta_if.isconnected()