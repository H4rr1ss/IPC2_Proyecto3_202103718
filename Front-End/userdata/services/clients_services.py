import requests
import json


class Client_services:
    def createClient(data):
        response = requests.post(
            'http://127.0.0.1:5000/client/register', json=data)

        return json.loads(response.text)

    def searchUser(data):
        response = requests.post(
            'http://127.0.0.1:5000/client/login', json=data)

        return json.loads(response.text)
