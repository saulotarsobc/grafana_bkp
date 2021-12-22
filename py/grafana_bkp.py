import requests
import json

server = 'http://IP:3000'
api_token = 'API_TOKEN'
headers = {
    "Authorization": "Bearer " + api_token
}


def search():
    url = server + "/api/search"
    content = requests.get(url=url, headers=headers, verify=False)
    return content.json()


def gerarJson(nome, dashboardJson):
    with open(nome, 'w') as json_file:
        json.dump(dashboardJson, json_file, indent=4)
        print('Dashboard salva com sucesso >> ' + nome)


for dash in search():
    uid = dash['uid']
    nome = dash['title'] + '.json'
    url = server + '/api/dashboards/uid/' + uid
    result = requests.get(url=url, headers=headers, verify=False).json()
    dashboardJson = result['dashboard']
    gerarJson(nome, dashboardJson)
