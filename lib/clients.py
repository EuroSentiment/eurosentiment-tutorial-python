class ServiceClient():

    def __init__(self, service_url, token):
        self.service_url = service_url
        self.token = token

class ResourceClient():
    def __init__(self, resource_url, token):
        self.resource_url = resource_url
        self.token = token
