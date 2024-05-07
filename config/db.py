from sqlalchemy import create_engine, MetaData

nombreBaseDeDatos= "clientesdb"
engine = create_engine("mysql+pymsql://root:root@localhost:3306/{}".format(nombreBaseDeDatos))
conn = engine.connect()

