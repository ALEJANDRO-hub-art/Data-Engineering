# %%
print("Hello World !!")

# %%
pip install cassandra-driver

# %%
import cassandra
print (cassandra.__version__)

# %%
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
  'secure_connect_bundle': 'secure-connect-cassandra-demo.zip'
}
auth_provider = PlainTextAuthProvider('YcFBXWbhJbGWbvvqFdIUmpvs', 'iAOq5Z_Z+DxYAurWtvTpwMApnFn6IDUGHigG2oQsxUspbTY,pLkP5NyQZoJsEjB87rewk-LP-a.OkOz+xOIr0PbeuMmMcsxLLWFSWaUagQZcy6FulrKMvzD.dsD6eNET')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
# print(row)
if row:
    print(row[0])
else:
    print("An error occurred.")

# %%
# Command to use a keyspace
try:
    query = "use ecommerce"
    session.execute(query)
    print("Inside the ecommerce keyspace")
except Exception as err:
    print("Exception Occured while using Keyspace : ",err)

# %%
# Command to create a table inside a KEyspace
try:
    query = """CREATE TABLE ecommerce.orders (
    order_id uuid,
    customer_id uuid,
    order_status varchar,
    order_purchase_timestamp timestamp,
    order_approved_at timestamp,
    order_delivered_carrier_date timestamp,
    order_delivered_customer_date timestamp,
    order_estimated_delivery_date timestamp,
    order_hour int,
    Oorder_day_of_week varchar,
    PRIMARY KEY ((customer_id), order_id, order_purchase_timestamp)
)"""
    session.execute(query)
    print("Table created inside the keyspace")
except Exception as err:
    print("Exception Occured while creating the table : ",err)

