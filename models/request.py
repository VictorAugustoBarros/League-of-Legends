import json

import requests


class Request:
    def __init__(self, api_key):
        self.api_key = api_key
        self.americas_api = "https://americas.api.riotgames.com"
        self.br_api = "https://br1.api.riotgames.com"
        self.key = "api_key=%s" % api_key

    def do_get_request(self, url):
        req = requests.get(url=url)
        return json.loads(req.text)

    def do_request_br(self, method):
        url = self.br_api + method + "?%s" % self.key
        req = requests.get(url=url)

        return json.loads(req.text)

    def do_request_america(self, method):
        url = self.americas_api + method + "?%s" % self.key
        req = requests.get(url=url)

        return json.loads(req.text)
