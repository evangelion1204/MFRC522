import json
import time
from mopify import client
import MFRC522


def main():
    mopify = client.Client("http://192.168.1.198:6680")
    # print mopify.get_playback_state()
    # print mopify.get_playlists()
    # print mopify.play_uri("spotify:user:1187838290:playlist:1Cm42wNpmI2TQC1zei0MXw")
    # print mopify.get_tracklist()
    # print mopify.stop()
    reader = MFRC522.MFRC522()

    while True:
        commands = []
        time.sleep(1)
        tag = reader.scanForPicc()

        if tag == False:
            continue

        body = tag.readBodyAsString()
        print("Read raw body:", body)
        try:
            commands = json.loads(body)
        except ValueError:
            continue

        for command in commands:
            print(command)


if __name__ == "__main__":
    main()
