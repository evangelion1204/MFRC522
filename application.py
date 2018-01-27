import json
import time
from mopidy import client, commands
import MFRC522


def main():
    rpcClient = client.Client("http://192.168.1.198:6680")
    mopidy = commands.Commands(rpcClient)

    reader = MFRC522.MFRC522()
    tags = {}
    previousTag = None

    while True:
        time.sleep(1)
        tag = reader.scanForPicc()

        if tag == False:
            if not previousTag:
                print("No tags found, stopping")
                mopidy.stop()
                tags = {}

            previousTag = tag
            continue

        previousTag = tag

        if tag.getUidAsHex() in tags:
            print("Skipping tag with UID", tag.getUidAsHex())
            continue

        print("Discovered new tag with UID", tag.getUidAsHex())

        tags[tag.getUidAsHex()] = tag

        body = tag.readBodyAsString()
        print("Read raw body:", body)
        try:
            rpcCommands = json.loads(body)
        except ValueError:
            continue

        for command in rpcCommands:
            method = command['method']
            params = command['params'] if 'params' in command else {}
            rpcClient.rpc(method, params)


if __name__ == "__main__":
    main()
