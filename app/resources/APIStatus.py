import json


class APIStatus:

    @staticmethod
    def on_get(req, resp):
        resp.body = json.dumps('API is online')