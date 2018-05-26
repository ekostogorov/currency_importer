import requests
import json

class HTTP_Adapter(object):
  url = None
  token = None

  def __init__(self, url, token):
    self.url = url
    self.token = token

  def load(self):
    url = self.__build_url__()
    print("URL", url)
    r = requests.get(url)
    if r.status_code == 200:
      json_data = r.json()
      return json_data
    else:
      raise requests.HTTPError("error connection to remote host, status code is: ", r.status_code)
      

  def __build_url__(self):
    return self.url + "?access_key=" + self.token + "&format=1"
