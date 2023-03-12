from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config



data_base_user = config('DATABASE_USER')
data_base_password = config('DATABASE_PASSWORD')
data_base_host = config('DATABASE_HOST')
data_base_port = config('DATABASE_PORT')
data_base_name = config('DATABASE_NAME')

data_base_url= f"postgresql+psycopg2://{data_base_user}:{data_base_password}@{data_base_host}:{data_base_port}/{data_base_name}"

engine = create_engine(data_base_url)
conn = engine.connect()
Session = sessionmaker(bind = engine)
session = Session()

