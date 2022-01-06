import os, requests, variables

if os.environ['PLAYER_EVENT'] == "playing":
        requests.get(f"{variables.HOST_IP}/yanify/{os.environ['TRACK_ID']}")
if os.environ['PLAYER_EVENT'] == "paused" or os.environ['PLAYER_EVENT'] == "stopped":
        requests.get(f"{variables.HOST_IP}/stop")
if os.environ['PLAYER_EVENT'] == "volume_set":
        requests.get(f"{variables.HOST_IP}/volume/{float((int) ((float(os.environ['VOLUME']) / 65535.0) * 100))/100}")