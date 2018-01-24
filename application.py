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

    # while True:
    time.sleep(1)
    tag = reader.scanForPicc()
    print(tag.readBodyAsString())

if __name__ == "__main__":
    main()
