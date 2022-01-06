# Yandex Station Socket

## Paths
- /play - Play music
- /stop - Stop music
- /next - Next track
- /prev - Previous track
- /like - Like track
- /dislike - Dislike track
- /rewind/100 - Rewind track (Put your value)
- /volume/0.2 - Set volume (Put your value)
- /yanify/(query) - Yanify module search query

## Install
- pip install -r requirements.txt

## Modules
#### Yanify module
- You need a Spotify Premium to do that
- Compile librespot and start it like <code>librespot -n "Yanify" --initial-volume 2 --onevent="python3 (Path to the yanify-module.py)"</code>
- Track rewind don't work

## Original idea
[Github](https://github.com/anVlad11/dd-alicization)