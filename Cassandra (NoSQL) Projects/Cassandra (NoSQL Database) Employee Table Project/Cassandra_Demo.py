#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World !!")


# In[3]:


pip install cassandra-driver


# In[4]:


import cassandraprint (cassandra.__version__)


# In[5]:


import cassandra
print (cassandra.__version__)


# In[8]:


from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
  'secure_connect_bundle': 'secure-connect-cassandra-demo.zip'
}
auth_provider = PlainTextAuthProvider('PumxPaWkZMjZnBWbbCLxpPZw', 'QS4mrxN39XrPvb3TxhzOyWZMy00cc1gNDgqTIuhYUeB-L,pNtR1m7tj9uTdMx+vOdXO0.7xzyD23BK+NXftsmeh-ofLFXrx6siQ86rfm-coWWzXNZIrl,wub4P9xcYe_')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
# print(row)
if row:
    print(row[0])
else:
    print("An error occurred.")


# In[9]:


# Command to use a keyspace
try:
    query = "use employee_keyspace"
    session.execute(query)
    print("Inside the employee_keyspace")
except Exception as err:
    print("Exception Occured while using Keyspace : ",err)


# In[10]:


# Command to create a table inside a KEyspace
try:
    query = """create table employee(
                emp_id int,
                emp_name varchar,
                emp_salary int,
                emp_dept varchar,
                emp_email varchar,
                emp_phone varchar,
                primary key (emp_id, emp_dept)
              )
            """
    session.execute(query)
    print("Table created inside the keyspace")
except Exception as err:
    print("Exception Occured while creating the table : ",err)


# In[11]:


# Alter the table in cassandra to drop a column
try:
    query = "alter table employee drop emp_email"
    session.execute(query)
    print("Column dropped successfully !!")
except Exception as err:
    print("Exception Occured while dropping the column: ",err)


# In[12]:


# Alter the table in cassandra to add a new column
try:
    query = "alter table employee add emp_email text"
    session.execute(query)
    print("Column added successfully !!")
except Exception as err:
    print("Exception Occured while adding the column: ",err)


# In[ ]:


# Drop a table in cassandra
try:
    query = "drop table employee"
    session.execute(query)
    print("Table dropped successfully !!")
except Exception as err:
    print("Exception Occured while dropping the table: ",err)


# In[13]:


# Insert data into cassandra table
try:
    query = "insert into employee(emp_id, emp_name, emp_salary, emp_dept, emp_email, emp_phone) values(1, 'Shashank', 10000, 'Software', 'abc.gmail.com','+91 768467474')"
    session.execute(query)
    print("Record inserted successfully !!")
except Exception as err:
    print("Exception Occured while inserting the data into table: ",err)


# In[14]:


# Insert data into cassandra table
try:
    query = "insert into employee(emp_id, emp_name, emp_salary, emp_dept, emp_email, emp_phone) values(2, 'Rahul', 20000, 'IT', 'xyx.gmail.com','+91 908467474')"
    session.execute(query)
    print("Record inserted successfully !!")
except Exception as err:
    print("Exception Occured while inserting the data into table: ",err)


# In[15]:


# Insert data into cassandra table
try:
    query = "insert into employee(emp_id, emp_name, emp_salary, emp_dept, emp_email, emp_phone) values(3, 'Sunny', 22000, 'HR', 'klm.gmail.com','+91 800067474')"
    session.execute(query)
    print("Record inserted successfully !!")
except Exception as err:
    print("Exception Occured while inserting the data into table: ",err)


# In[16]:


# Insert data into cassandra table
try:
    query = "insert into employee(emp_id, emp_name, emp_salary, emp_dept, emp_email, emp_phone) values(4, 'Vishal', 30000, 'Software', 'mno.gmail.com','+91 600467474')"
    session.execute(query)
    print("Record inserted successfully !!")
except Exception as err:
    print("Exception Occured while inserting the data into table: ",err)


# In[17]:


# Select query on cassandra table
try:
    query = "select * from employee"
    result = session.execute(query)
    for row in result:
        print(row)
except Exception as err:
    print("Exception Occured while selecting the data from table: ",err)


# In[21]:


# Select query for specific columns in cassandra table and how to access from Row object
try:
    query = "select emp_id, emp_name from employee"
    result = session.execute(query)
    # option 1
    for row in result:
        print("Emp ID : {}, Emp Name : {}".format(row[0],row[1]))
except Exception as err:
    print("Exception Occured while selecting the data from table: ",err)


# In[22]:


# Write a query to get total count and max salary of employees
try:
    query = "select count(*) as row_count, max(emp_salary) as max_salary from employee"
    result = session.execute(query)
    row = result.one()
    print(row)
    #print(row[0])
except Exception as err:
    print("Exception Occured while selecting the data from table: ",err)


# In[24]:


# Write a query to filter data from cassandra table or how to use where clause
# Rules for where clause - It can be used effectively with high performance for given below type of columns
# 1.) Partition Key (Single or Composite)
                   #OR
# 2.) if Cluster column  used in where clause then it should be with Partition Key
                   #OR
# 3.) A column on which we have applied the index
                   #OR
# 4.) A column which is not part of partition key or index column or clustering column then we can use where clause but we have to
# use keyword ALLOW FILTERING - it will be a super slow performance when data volume is very high

try:
    query = "select * from employee where emp_name='Shashank' ALLOW FILTERING"
    result = session.execute(query)
    row = result.one()
    print(row)
except Exception as err:
    print("Exception Occured while selecting the data from table: ",err)


# In[25]:


# where clause for Partition key only or Rule no -1

try:
    query = "select * from employee where emp_id=2"
    result = session.execute(query)
    row = result.one()
    print(row)
except Exception as err:
    print("Exception Occured while selecting the data from table: ",err)


# In[27]:


# where clause for Clustering key only or Rule no - 2 

try:
    query = "select * from employee where emp_dept='Software' and emp_id=1"
    result = session.execute(query)
    row = result.one()
    print(row)
except Exception as err:
    print("Exception Occured while selecting the data from table: ",err)


# In[28]:


# Group by in cassandra  -  Allowed for all columns which are part of Primary Key
# Follow given below rules
# Rule - 1 : Use only partition key in the group by
              #OR
# Rule - 2 : if Cluster key column is used then follow the actual declared sequence in the primary key
try:
    query = "select emp_id, sum(emp_salary) as sum_salary from employee group by emp_id"
    result = session.execute(query)
    row = result.one()
    for row in result:
        print("Emp ID : ", row[0])
        print("Sum Of Salary : ", row[1])
except Exception as err:
    print("Exception Occured while selecting the data from table: ",err)


# In[29]:


# Group by in cassandra 
# Rule - 2 : if Cluster key column is used then follow the actual declared sequence in the primary key
try:
    query = "select emp_id, emp_dept, sum(emp_salary) as sum_salary from employee group by emp_id, emp_dept"
    result = session.execute(query)
    row = result.one()
    for row in result:
        print("Emp ID : ", row[0])
        print("Emp Dept : ", row[1])
        print("Sum Of Salary : ", row[2])
except Exception as err:
    print("Exception Occured while selecting the data from table: ",err)


# In[ ]:




