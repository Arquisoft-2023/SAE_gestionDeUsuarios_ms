from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()



data_base_user = str(os.environ.get('DATABASE_USER_DB'))
data_base_password = str(os.environ.get('DATABASE_PASSWORD_DB'))
data_base_port = str(os.environ.get('DATABASE_PORT_DB'))
data_base_name = str(os.environ.get('DATABASE_NAME_DB'))

# Master data base
data_base_host_master = str(os.environ.get('DATABASE_HOST_DB_MASTER'))

data_base_url_master= f"postgresql+psycopg2://{data_base_user}:{data_base_password}@{data_base_host_master}:{data_base_port}/{data_base_name}"

engine = create_engine(data_base_url_master,isolation_level="AUTOCOMMIT")
conn = engine.connect()
Session = sessionmaker(bind = engine)
session = Session()

#Replica data base
data_base_host_replica = str(os.environ.get('DATABASE_HOST_DB_REPLICA'))

data_base_url_replica= f"postgresql+psycopg2://{data_base_user}:{data_base_password}@{data_base_host_replica}:{data_base_port}/{data_base_name}"

engine_replica = create_engine(data_base_url_replica,isolation_level="AUTOCOMMIT")
conn_replica = engine_replica.connect()
Session_replica = sessionmaker(bind = engine_replica)
session_replica = Session_replica()



