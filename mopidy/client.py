import requests
import json

class Client:
    HEADERS = {"content-type": "application/json"}

    host = ''
    id = 0

    def __init__(self, host="http://localhost:6680"):
        self.host = host

    def rpc(self, method, params = None):
        id = self.id
        self.id += 1

        command = {
            "method": method,
            "jsonrpc": "2.0",
            "id": id,
        }

        if params:
            command['params'] = params

        response = requests.post(
            url=self.host + "/mopidy/rpc",
            data=json.dumps(command),
            headers=self.HEADERS,
        ).json()

        if "result" in response:
            return response["result"]
        else:
            print response
            return False


