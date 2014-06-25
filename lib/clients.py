# encoding: utf-8
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#  The original code are licensed under the GNU Lesser General Public License.

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


