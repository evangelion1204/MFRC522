import argparse
import json
import time
import MFRC522
from mopify import serializer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--command', help='command to store')
    parser.add_argument('--params', help='additional required params')
    args = parser.parse_args()

    params = args.params.split(',')

    mopifySerializer = serializer.Serializer()

    if args.command == 'play_uri':
        writeCommand(mopifySerializer.play_uri(params[0]))
    else:
        print("Command not supported", args.command)

def writeCommand(command):
    reader = MFRC522.MFRC522()
    print("Place a writeable tag on the reader")
    while True:
        time.sleep(1)
        tag = reader.scanForPicc()

        if tag == False:
            continue

        tag.writeStringInBody(json.dumps([command]))

        return

if __name__ == "__main__":
    main()
