from sqlalchemy import create_engine, MetaData

nombreBaseDeDatos= "clientesdb"
engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/{}".format(nombreBaseDeDatos))

meta = MetaData()
conn = engine.connect()

