import requests
from datetime import datetime

jokes_ids = []

class Joke:
    def __init__(self, joke, id, create_time, resp_time):
        self.joke = joke
        self.id = id
        self.create_time = create_time
        self.resp_time = resp_time

def jokes():
    while True:
        start = datetime.now()
        resp = requests.get('https://api.icndb.com/jokes/random')
        end = datetime.now()
        resp_json = resp.json()
        if resp_json['type']=='success':
            if resp_json['value']['id'] not in jokes_ids:
                jokes_ids.append(resp_json['value']['id'])
                joke = resp_json['value']['joke']
                create_time = datetime.now()
                joke_info = Joke(joke, resp_json['value']['id'], create_time, end-start)
                yield joke_info

for joke in jokes(): print('ID: '+str(joke.id)+' JOKE: '+str(joke.joke)+' CREATE TIME: '+str(joke.create_time)+' RESP TIME: '+str(joke.resp_time))