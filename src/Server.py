from urequests import post
from ujson import dumps

class Server:
    headers = {'content-type': 'application/json'}
    
    def __init__(self, host, port=80, route=''):
        self.url = 'http://'+ host+':'+ str(port) +'/'+ route
    

    def post(self, data_type, value):
        payload = { data_type : value }
        try:
            print('Sending data to server...')
            res = post(url = self.url, headers = self.headers, data = dumps(payload))
            print('Successfuly sent data:', res.text)
        except Exception as error:
            print(error)
