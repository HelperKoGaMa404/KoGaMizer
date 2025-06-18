import requests
import random
import time
import json

with open('game_messages.json', 'r') as file:
    data = json.load(file)
rand_com = data[random.randint(0, 17)]
session = requests.session()
def post_game_comment(username : str, password : str, server : str, game_id : str, message : str):
    url = {
        'br': 'https://kogama.com.br',
        'www': 'https://www.kogama.com',
        'friends': 'https://friends.kogama.com',
    }[server.lower()]
    session.post(f"{url}/auth/login/", json={"username": username,"password": password})
    _handle_requests(method='POST', url=f"{url}/game/{game_id}/comment/", data={"comment": message})

def _handle_requests(method, url, data=None):
    if method == 'GET':
        session.get(url)
    elif method == 'POST':
        session.post(url, json=data)

while True:
    post_game_comment("xXType_your_username_hereXx", "MySuperCoolPass123", "www", "2263148", rand_com)post_game_comment("xXType_your_username_hereXx", "MySuperCoolPass123", "www", "2263148", rand_com)
    time.sleep(100)
