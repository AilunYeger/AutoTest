import time
from utils.sourceLoad import data
from api.apis import api
import json
import os

class Operation:
    def __init__(self):
        self.bath_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        self.tranNo = str(int(time.time()*1000))
        self.headers = {
            "bankNo": "00000100",
            "Content-Type": "application/json",
            "clientTranNo": self.tranNo,
            "globalTranNo": self.tranNo
        }


    def do_auth(self, **kwargs):
        json_path = os.path.join(self.bath_path, 'config', 'json', 'auth.json')
        json_data = data.loadJson(json_path, **kwargs)
        json_data['tranNo'] = self.tranNo
        return api.auth(json=json_data, headers=self.headers)

operator = Operation()








if __name__ == '__main__':
    op = Operation()
    op.auth(acctNo='6228480468693141177')