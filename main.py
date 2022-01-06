import asyncio, time
from flask import Flask
from glagol import ys_sock, init

web = Flask(__name__)

@web.route('/')
def main():
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/vol/<vol>')
def volume(vol):
    asyncio.run(ys_sock({"command":"setVolume", "volume":float(vol)}))
    time.sleep(1)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/next')
def next():
    asyncio.run(ys_sock({"command":"next"}))
    time.sleep(1)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/prev')
def previous():
    asyncio.run(ys_sock({"command":"prev"}))
    time.sleep(1)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/play')
def play():
    asyncio.run(ys_sock({"command":"play"}))
    time.sleep(1)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/stop')
def stop():
    asyncio.run(ys_sock({"command":"stop"}))
    time.sleep(1)
    return asyncio.run(ys_sock({"command":"ping"}))

@web.route('/rewind/<rew>')
def rewind(rew):
    asyncio.run(ys_sock({"command":"rewind", "position":int(rew)}))
    time.sleep(1)
    return asyncio.run(ys_sock({"command":"ping"}))

init()
web.run(debug=True)