
# update table with the current date using airflow 

from sqlalchemy import *
from datetime import datetime

host = 'ec2-52-48-159-67.eu-west-1.compute.amazonaws.com'
port = '5432'
database = 'dfgo0j8urfpsu2'
user = 'X'
password = 'Y'

conn_str = f"postgresql://{user}:{password}@{host}/{database}"
engine = create_engine(conn_str)
connection = engine.connect()
metadata = MetaData()

table_to_update = Table('table_to_update', metadata,
   Column('desc', String(255), nullable=False),
   Column('time', DateTime, nullable=False)
)
metadata.create_all(engine)
query = insert(table_to_update).values(desc='table updated', time=datetime.now())
ResultProxy = connection.execute(query)
#print('Insert done')
