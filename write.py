import argparse
import json
import time
import MFRC522
from mopidy import serializer, commands


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--command', help='command to store')
    parser.add_argument('--params', help='additional required params')
    args = parser.parse_args()

    params = args.params.split(',')

    mopidySerializer = serializer.Serializer()
    mopidy = commands.Commands(mopidySerializer)

    if args.command == 'play_uri':
        mopidy.play_uri(params[0])
        writeCommands(mopidySerializer.getCommandBuffer())
    else:
        print("Command not supported", args.command)

def writeCommands(commands):
    reader = MFRC522.MFRC522()
    print("Writing commands", commands)
    print("Place a writeable tag on the reader")
    while True:
        time.sleep(1)
        tag = reader.scanForPicc()

        if tag == False:
            continue
        body = json.dumps(commands, separators=(',', ':'))
        print("Writing body", body)
        tag.writeStringInBody(body)

        return

if __name__ == "__main__":
    main()
