class Serializer:
    commands = []

    def rpc(self, method, params = {}):
        self.commands.append({
            'method': method,
            'params': params,
        })

        return True

    def getCommandBuffer(self):
        return self.commands

    def clear(self):
        self.commands = []


