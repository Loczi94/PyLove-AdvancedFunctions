import requests

jokes_ids = []

def jokes():
    while True:
        resp = requests.get('https://api.icndb.com/jokes/random')
        resp_json = resp.json()
        if resp_json['type']=='success':
            if resp_json['value']['id'] not in jokes_ids:
                jokes_ids.append(resp_json['value']['id'])
                yield resp_json['value']['joke']

for joke in jokes(): print(joke)