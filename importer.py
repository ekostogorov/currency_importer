from adapters.http_adapter import HTTP_Adapter
from adapters.mysql_adapter import MySQL_Adapter
import config

class App(object):
  mysql_adapter = None
  http_adapter = None
  config = None
  
  def __init__(self, config):
    self.config = config
    self.http_adapter = HTTP_Adapter(
      self.config.API_URL,
      self.config.ACCESS_TOKEN
    )
    self.pg_adapter = MySQL_Adapter(
      self.config.HOST,
      self.config.PORT,
      self.config.USER,
      self.config.PASSWORD,
      self.config.DB
    )
  
  def start(self):
    data = self.http_adapter.load()
    mapped_data = self.__map__(data)
    return self.pg_adapter.save(mapped_data)

  def __map__(self, data):
    cur_dict = {}
    if "currencies" in data:
      for k, v in data['currencies'].items():
        name = k.replace("ʻ", "")
        code = v.replace("ʻ", "")
        cur_dict[name] = code
      return cur_dict
    else:
      print("No data")

def run():
  app = App(config)
  app.start()

run()