import requests
from conf.configuration import *
from clients import ResourceClient, ServiceClient

class NegativeWordsMatcher:

    def __init__(self):
        self.language_detector = ServiceClient(LANG_DETECTION_URL, TOKEN)
        self.resource_client = ResourceClient(RESOURCES_URL, TOKEN)
