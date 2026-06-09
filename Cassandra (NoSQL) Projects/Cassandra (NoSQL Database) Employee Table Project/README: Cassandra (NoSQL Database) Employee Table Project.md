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

Run:

- docker exec -it cassandra-demo-project-cassandra-1 cqlsh

If the container name is different, first run:

- docker ps

Copy the Cassandra container name.















