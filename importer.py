from http_adapter import HTTP_Adapter
from pg_adapter import PG_Adapter

class App(object):
  pg_adapter = None
  http_adapter = None
  config = None
  
  def __init__(self, config):
    self.config = config
    self.http_adapter = HTTP_Adapter(
      self.config.API_URL,
      self.config.ACCESS_TOKEN
    )
    self.pg_adapter = PG_Adapter(
      self.config.HOST,
      self.config.PORT,
      self.config.USER,
      self.config.PASSWORD
    )
  
  def start(self):
    data = self.http_adapter.load()
    mapped_data = self.__map__(data)
    return self.pg_adapter.save(mapped_data)

  def __map__(self, data):
    return data
