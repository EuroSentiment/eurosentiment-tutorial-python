import requests
import json

class ServiceClient():

    def __init__(self, service_url, token):
        self.service_url = service_url
        self.token = token

    def request(self, input):
        headers = {'x-eurosentiment-token': self.token}
        response = requests.post(self.service_url,
                                 data=json.dumps(input),
                                 headers=headers)
        return json.loads(response.content)

class ResourceClient():

    def __init__(self, resource_url, token):
        self.resource_url = resource_url
        self.token = token

    def request(self, input):
        headers = {"x-eurosentiment-token": self.token,
                   "content-type":"application/json"}
        response = requests.post(self.resource_url,
                                 data=json.dumps(input),
                                 headers=headers)
        return json.loads(response.content)


