class Serializer:
    commands = []

    def rpc(self, method, params = None):
        command = {
            'method': method,
        }

        if params:
            command['params'] = params

        self.commands.append(command)

        return True

    def getCommandBuffer(self):
        return self.commands

    def clear(self):
        self.commands = []


