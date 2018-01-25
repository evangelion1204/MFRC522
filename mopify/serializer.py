import json

class Serializer:
    def __init__(self, client=None):
        self.client = client

    def play_uri(self, uri):
        return json.dumps({
            'command': 'play_uri',
            'params': { 'uri': uri },
        })


