import json
import time
import MFRC522
import signal
from mopidy import client, commands
import RPi.GPIO as GPIO

continueReading = True

# Capture SIGINT for cleanup when the script is aborted
def stop(signal,frame):
    global continueReading
    print "Ctrl+C captured, ending read."
    continueReading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, stop)

def main():
    global continueReading

    rpcClient = client.Client("http://localhost:6680")
    mopidy = commands.Commands(rpcClient)

    reader = MFRC522.MFRC522()
    tags = {}
    previousTag = False

    while continueReading:
        time.sleep(1)
        tag = reader.scanForPicc()

        if tag == False:
            if not previousTag and tags :
                print("Tag removed, stopping")
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
