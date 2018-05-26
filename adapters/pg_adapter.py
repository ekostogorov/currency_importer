import psycopg2

class PG_Adapter(object):
  host = None
  port = None
  user = None
  password = None
  db = None

  def __init__(self, hst, prt, usr, psswrd, db):
    self.host = hst
    self.port = prt
    self.user = usr
    self.password = psswrd
    self.db = db

  def save(self, data):
    cur = self.__connect__()
    for k, v in data.items():
      query = self.__prepare_query__(k, v)
      cur.execute(query, (k, v))
    print("Import completed")
    return

  def __connect__(self):
    conn_str = "host=" + self.host + " port=" + self.port + " user=" + self.user + " password=" + self.password
    conn = psycopg2.connect(conn_str)
    return conn.cursor()

  def __prepare_query__(self, k, v):
    sql = """
    INSERT INTO public.rates 
    (currency_name, rate) 
    VALUES (%s, %s)
    """
    return sql