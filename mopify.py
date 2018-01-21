import requests
import json

class Command:
    HEADERS = {"content-type": "application/json"}

    host = ''
    id = 0

    def __init__(self, host="http://localhost:6680"):
        self.host = host

    def get_playback_state(self):
        return self.call_rpc("core.playback.get_state")

    def play_uri(self, uri):
        self.clear_tracklist()
        self.add_to_tracklist(uri)
        self.play()

    def clear_tracklist(self):
        return self.call_rpc("core.tracklist.clear")

    def add_to_tracklist(self, uri):
        return self.call_rpc("core.tracklist.add", { "uri": uri })

    def get_tracklist(self):
        return self.call_rpc("core.tracklist.get_tracks")

    def get_playlists(self):
        return self.call_rpc("core.playlists.as_list")

    def play(self):
        return self.call_rpc("core.playback.play")

    def stop(self):
        return self.call_rpc("core.playback.stop")

    def call_rpc(self, method, params = {}):
        id = self.id
        self.id += 1

        payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
            "id": id,
        }

        response = requests.post(
            url=self.host + "/mopidy/rpc",
            data=json.dumps(payload),
            headers=self.HEADERS,
        ).json()

        if "result" in response:
            return response["result"]
        else:
            print response
            return False


