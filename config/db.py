from sqlalchemy import create_engine, MetaData

nombreBaseDeDatos= "clientesdb"
engine = create_engine("mysql+pymysql://root:root@localhost:3306/{}".format(nombreBaseDeDatos))

meta = MetaData()
conn = engine.connect()

