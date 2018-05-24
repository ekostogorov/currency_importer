import psycopg2

class PG_Adapter(object):
  host = None
  port = None
  user = None
  password = None
  source = None

  def __init__(self, hst, prt, usr, psswrd, src):
    self.host = hst
    self.port = prt
    self.user = usr
    self.password = psswrd
    self.source = src

  def save(self, data):
    cur = self.__connect__()
    for k, v in data.items():
      query = self.__prepare_query__()
      cur.execute(query, (k, v))
    print("Import completed")
    return



  def __connect__(self):
    conn_str = "host=" + self.host + " port=" + self.port + " user=" + self.user + " password=" + self.password
    conn = psycopg2.connect(conn_str)
    return conn.cursor()

  def __prepare_query__(self):
    sql = """
    INSERT INTO %s 
    (currency_id, rate) 
    VALUES (%d, %d)
    """
    return sql
