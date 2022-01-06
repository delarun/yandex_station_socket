import requests, websockets, ssl, time, json, variables

def ys_struct(data):
    data = json.loads(data)
    out = {"status":data['status'], 'state': data['state']}
    return json.dumps(out)

async def ys_sock(payload):
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_context.load_cert_chain("scert.pem", "spk.pem")
    async with websockets.connect(f"wss://{variables.YS_IP}:{variables.YS_PORT}", ssl=ssl_context) as websocket:
        await websocket.send(json.dumps({"conversationToken":variables.YS_TOKEN, "id":variables.YS_ID, "sentTime":time.time(), "payload":payload}))
        return ys_struct(await websocket.recv())

def init():
    ys = requests.get(f"{variables.GLAGOL_URL}/device_list",
        headers={"Authorization": f"Oauth {variables.YM_TOKEN}"}).json()["devices"][0]
    with open("scert.pem", "w") as text_file:
        text_file.write(ys['glagol']['security']['server_certificate'])
    with open("spk.pem", "w") as text_file:
        text_file.write(ys['glagol']['security']['server_private_key'])
    variables.YS_TOKEN = requests.get(f"https://quasar.yandex.net/glagol/token?device_id={ys['id']}&platform={ys['platform']}", 
        headers={"Authorization": f"Oauth {variables.YM_TOKEN}"}).json()['token']