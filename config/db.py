from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()



data_base_user = str(os.environ.get('DATABASE_USER_DB'))
data_base_password = str(os.environ.get('DATABASE_PASSWORD_DB'))
data_base_host = str(os.environ.get('DATABASE_HOST_DB'))
data_base_port = str(os.environ.get('DATABASE_PORT_DB'))
data_base_name = str(os.environ.get('DATABASE_NAME_DB'))

#data_base_url= f"postgresql+psycopg2://{data_base_user}:{data_base_password}@{data_base_host}:{data_base_port}/{data_base_name}"
data_base_url= f"postgresql+psycopg2://{data_base_user}:{data_base_password}@{data_base_host}:5432/{data_base_name}"



engine = create_engine(data_base_url,isolation_level="AUTOCOMMIT")
conn = engine.connect()
Session = sessionmaker(bind = engine)
session = Session()

