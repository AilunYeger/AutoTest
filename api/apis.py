from utils.httpRequest import HttpRequests
import requests, os
from utils.sourceLoad import data


path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'config', 'setting.ini')
host = data.loadIni(path)['HOST']['test-pay-host']

class Api(HttpRequests):
    def __init__(self):
        self.session = requests.session()
        self.host = host

    def auth(self, **kwargs):
        return self.send('/pay/auth', 'POST', **kwargs)

    def bindPretie(self, **kwargs):
        return self.send('/pay/bind/pretie', 'POST', **kwargs)

    def bindConfirm(self, **kwargs):
        return self.send('/pay/bind/confirm', 'POST', **kwargs)

    def singlePay(self, **kwargs):
        return self.send('/pay/single/pay', 'POST', **kwargs)

    def singleCollection(self, **kwargs):
        return self.send('/pay/single/collection', 'POST', **kwargs)

api = Api()