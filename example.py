import json
from mopidy import client, commands, serializer
# from recorder import proxy

def main():
    realClient = client.Client("http://192.168.1.198:6680")
    # mopidy = commands.Commands(realClient)
    rpcSerializer = serializer.Serializer()
    mopidy = commands.Commands(rpcSerializer)
    # Recorder = proxy.RecordWithOutPassthrough(commands.Commands)
    # recorder = Recorder(rpcSerializer)

    print(mopidy.play_uri('spotify:user:1187838290:playlist:7jTHoHHHX50SMonOHZBjfI'))
    # print(recorder.play_uri('spotify:user:1187838290:playlist:7jTHoHHHX50SMonOHZBjfI'))
    print(json.dumps(rpcSerializer.getCommandBuffer(), separators=(',', ':')))


if __name__ == "__main__":
    main()
