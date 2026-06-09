I have this Cassandra (NoSQL Database) Employee Table Project

<img width="730" height="206" alt="image" src="https://github.com/user-attachments/assets/174fa143-3261-4440-93ac-a4e16681c746" />

Based on the uploaded files:

**Cassandra_Demo.py** contains Python code that connects to a Cassandra database, creates tables, inserts records, runs queries, and demonstrates Cassandra operations.

**docker-compose.yml** is typically used to start Cassandra and related services in Docker containers.

<img width="597" height="160" alt="image" src="https://github.com/user-attachments/assets/4722c223-e179-42b9-a339-5be7a94c1044" />

GUI steps

**1. Open Docker Desktop**
Open Docker Desktop
Make sure it says Docker Engine running
Leave Docker Desktop open

**2. Open the project folder**

Open File Explorer

Go to your **Cassandra_Demo_Project** folder. In our case is **C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\7 Cassandra (NoSQL)\Module 4 - Cassandra Class 2\Step 1\Cassandra_Code main**

Right-click inside the folder

Click Open in Terminal

or

Open cmd prompt and do:

cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\7 Cassandra (NoSQL)\Module 4 - Cassandra Class 2\Step 1\Cassandra_Code main"

**3. Start Cassandra**

Run:

- docker compose up -d

Then check:

- docker ps

You should see a Cassandra container running on port:

- 9042
















