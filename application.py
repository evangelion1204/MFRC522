import json
import time
from mopidy import client
import MFRC522


def main():
    mopify = client.Client("http://192.168.1.198:6680")
    reader = MFRC522.MFRC522()
    tags = {}

    while True:
        time.sleep(1)
        tag = reader.scanForPicc()

        if tag == False:
            continue

        if tag.getUidAsHex() in tags:
            print("Skipping tag with UID", tag.getUidAsHex())
            continue

        print("Discovered new tag with UID", tag.getUidAsHex())

        tags[tag.getUidAsHex()] = tag

        body = tag.readBodyAsString()
        print("Read raw body:", body)
        try:
            commands = json.loads(body)
        except ValueError:
            continue

        for command in commands:
            method = command['method']
            params = command['params'] if 'params' in command else {}
            mopify.rpc(method, params)


if __name__ == "__main__":
    main()
