import asyncio, time, variables, requests
from flask import Flask
from glagol import ys_sock, init
from yandex_music import Client

client = Client(variables.YM_TOKEN)

web = Flask(__name__)

@web.route('/')
def main():
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/volume/<vol>')
def volume(vol):
    asyncio.run(ys_sock({"command":"setVolume", "volume":float(vol)}))
    time.sleep(1.5)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/next')
def next():
    asyncio.run(ys_sock({"command":"next"}))
    time.sleep(1.5)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/prev')
def previous():
    asyncio.run(ys_sock({"command":"prev"}))
    time.sleep(1.5)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/play')
def play():
    asyncio.run(ys_sock({"command":"play"}))
    time.sleep(1.5)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/stop')
def stop():
    asyncio.run(ys_sock({"command":"stop"}))
    time.sleep(1.5)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/rewind/<rew>')
def rewind(rew):
    asyncio.run(ys_sock({"command":"rewind", "position":int(rew)}))
    time.sleep(1.5)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/like')
def like():
    asyncio.run(ys_sock({"command":"sendText", "text":"Поставь лайк"}))
    time.sleep(1.5)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/dislike')
def dislike():
    asyncio.run(ys_sock({"command":"sendText", "text":"Поставь дизлайк"}))
    time.sleep(1.5)
    return asyncio.run(ys_sock({"command":"ping"}))

# Yanify module
@web.route('/yanify/<query>')
def yanify(query):
    r = requests.get(f"https://api.spotify.com/v1/tracks/{query}?market=RU", headers={"Authorization": f"Bearer {variables.SPOTIFY_TOKEN}"}).json()
    asyncio.run(ys_sock({"command":"playMusic", "id": str(client.search(f"{r['artists'][0]['name']} - {r['name']}").tracks.results[0].id), "type": "track"}))
    time.sleep(1.5)
    return asyncio.run(ys_sock({"command":"ping"}))

init()
web.run("0.0.0.0", debug=True)