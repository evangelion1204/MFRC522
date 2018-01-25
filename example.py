from mopidy import client, commands, serializer

def main():
    realClient = client.Client("http://192.168.1.198:6680")
    rpcSerializer = serializer.Serializer()
    # mopidy = commands.Commands(realClient)
    mopidy = commands.Commands(rpcSerializer)

    print(mopidy.get_playback_state())
    print(rpcSerializer.getCommandBuffer())


if __name__ == "__main__":
    main()
