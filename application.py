import json
import time
import mopify
import MFRC522


def main():
    client = mopify.Command("http://192.168.1.198:6680")
    # print client.get_playback_state()
    # print client.get_playlists()
    # print client.play_uri("spotify:user:1187838290:playlist:1Cm42wNpmI2TQC1zei0MXw")
    # print client.get_tracklist()
    # print client.stop()
    reader = MFRC522.MFRC522()

    while True:
        commands = []
        time.sleep(1)
        tag = reader.scanForPicc()

        if tag == False:
            continue

        body = tag.readBodyAsString()

        try:
            commands = json.loads(body)
        except ValueError:
            continue

        for command in commands:
            print(command)


if __name__ == "__main__":
    main()
