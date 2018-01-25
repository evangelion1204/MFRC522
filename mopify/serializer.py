class Serializer:
    def __init__(self, client=None):
        self.client = client

    def play_uri(self, uri):
        return {
            'command': 'play_uri',
            'params': { 'uri': uri },
        }


