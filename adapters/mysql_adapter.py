import MySQLdb as mdb

class MySQL_Adapter(object):
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
    conn = self.__connect__()
    cur = conn.cursor()
    for k, v in data.items():
      print(k, v)
      query = self.__prepare_query__(k, v)
      print(query)
      cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
    print("Import completed")

  def __connect__(self):
    conn = mdb.connect(
      host = self.host,
      port = self.port,
      user = self.user,
      passwd = self.password,
      db = self.db
    )
    return conn

  def __prepare_query__(self, code, name):
    sql = """
    INSERT INTO {0}.currencies
    (code, name) 
    VALUES ('{1}', '{2}')
    ON DUPLICATE KEY UPDATE
    code = '{1}', name = '{2}'
    """.format(self.db, code, name)
    return sql