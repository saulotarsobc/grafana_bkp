import requests
import json

server = 'http://10.0.0.1:3000'
api_token = 'SeuTokenAki'
headers = {
    "Authorization": f"Bearer {api_token}"
}


def search():
    return requests.get(
        url=f"{server}/api/search",
        headers=headers,
        verify=False
    ).json()


def criarJson(nome, dashEmJson):
    with open(nome, 'w') as json_file:
        json.dump(dashEmJson, json_file, indent=4)
        print(f'Sucesso >> {nome}')


for dash in search():
    result = requests.get(
        url=f"{server}/api/dashboards/uid/{dash['uid']}",
        headers=headers,
        verify=False
    ).json()
    criarJson(f"{dash['type']} - {dash['title']}.json", result['dashboard'])
