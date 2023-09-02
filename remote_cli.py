from dotenv import load_dotenv
import os
import requests

class RemoteCli:

    def __init__(self):
        load_dotenv()
        BIN_ID = '64f2bda4d972192679bd648b'
        self.url = 'https://api.jsonbin.io/v3/b/' + BIN_ID
        self.headers = { 
            'Content-Type': 'application/json',
            'X-Master-Key': os.getenv("SEBS_API_KEY")
        }


    def update_remote(self, data: list):
        req = requests.put(self.url, json=data, headers=self.headers)
        #print(self.headers)
        #print(req.text)
