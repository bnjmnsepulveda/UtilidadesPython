import requests
import json

HEADERS = {'Content-Type': 'application/json'}


def get(url, payload):
    with requests.post(url, headers=HEADERS, params=payload) as req:
        if req.status_code == 200:
            return req.json()


def post(url, entity):
    with requests.post(url, data=json.dumps(entity), headers=HEADERS) as req:
        if req.status_code == 200:
            return req.json()


def put(url, entity):
    with requests.put(url, data=json.dumps(entity), headers=HEADERS) as req:
        if req.status_code == 200:
            return req.json()


def delete(url):
    with requests.delete(url) as req:
        if req.status_code == 200:
            return req.text

