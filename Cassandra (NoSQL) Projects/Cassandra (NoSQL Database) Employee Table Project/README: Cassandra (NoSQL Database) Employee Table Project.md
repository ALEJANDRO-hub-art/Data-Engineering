I have this Cassandra (NoSQL Database) Employee Table Project

<img width="730" height="206" alt="image" src="https://github.com/user-attachments/assets/174fa143-3261-4440-93ac-a4e16681c746" />

Based on the uploaded files:

**Cassandra_Demo.py** contains Python code that connects to a Cassandra database, creates tables, inserts records, runs queries, and demonstrates Cassandra operations.

**docker-compose.yml** is typically used to start Cassandra and related services in Docker containers.

<img width="597" height="160" alt="image" src="https://github.com/user-attachments/assets/4722c223-e179-42b9-a339-5be7a94c1044" />

<img width="614" height="335" alt="image" src="https://github.com/user-attachments/assets/29d54f3b-7cd4-4f02-8bbb-f177021c930e" />
 

GUI steps

**1. Open Docker Desktop**

- Open Docker Desktop. 
- Make sure it says Docker Engine running.
- Leave Docker Desktop open

**2. Open the project folder**

Open File Explorer

Go to your **Cassandra_Demo_Project** folder.

Right-click inside the folder

Click Open in Terminal

or

Open cmd prompt and do:

cd "C:\Users\Usuario\Desktop\Cassandra_Demo_Project"

**3. Start Cassandra**

Run:

- docker compose up -d

Then check:

- docker ps

You should see a Cassandra container running on port:

- 9042

**4. Enter Cassandra shell**

Where is this **Cassandra shell**. Docker Container: If running Cassandra via Docker, open an interactive bash session in your container and execute cqlsh directly, or run:**docker exec -it <container_name> cqlsh** this code we use it in the following command.

Run:

- docker exec -it cassandra-demo-project-cassandra-1 cqlsh

If the container name is different, first run:

- docker ps

Copy the Cassandra container name.

**5. Create keyspace manually**

Inside **cqlsh**, run:

CREATE KEYSPACE employee_keyspace
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

Then:

USE employee_keyspace;

**cqlsh** stands for **Cassandra Query Language Shell**. It is a Python-based command-line interface shipped with every ⁠Apache Cassandra package that allows you to execute Cassandra Query Language (CQL) commands directly against your database.


**6. Run project commands manually in Cassandra GUI / terminal - Cassandra terminal (cqlsh)**

Create table:

CREATE TABLE employee (

  emp_id int,
  
  emp_name varchar,
  
  emp_salary int,
  
  emp_dept varchar,
  
  emp_email varchar,
  
  emp_phone varchar,
  
  PRIMARY KEY (emp_id, emp_dept)
  
);

Insert records:

<img width="489" height="198" alt="image" src="https://github.com/user-attachments/assets/37b28301-5e57-4f65-9ca0-0086db144343" />

<img width="590" height="356" alt="image" src="https://github.com/user-attachments/assets/d5dc7d40-1529-414e-b4a4-bf97e77596fe" />

<img width="593" height="284" alt="image" src="https://github.com/user-attachments/assets/437de73a-97cb-43ef-bb36-6b1e5b541720" />


















