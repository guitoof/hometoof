from urequests import post
from ujson import dumps

class Server:
    headers = {'content-type': 'application/json'}
    
    def __init__(self, host, port=80):
        self.base_url = 'http://'+ host+':'+ str(port)
    

    def post(self, route, payload):
        url = self.base_url + '/' + route
        try:
            print('Sending data to server...')
            res = post(url = url, headers = self.headers, data = dumps(payload))
            print('Successfuly sent data:', res.text)
        except Exception as error:
            print(error)
