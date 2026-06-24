I have this project Apache Flink Kafka-to-Kafka Streaming Pipeline Project.

<img width="589" height="221" alt="image" src="https://github.com/user-attachments/assets/20e78cd0-6e20-4557-89dc-7e81c25754a5" />

 <img width="589" height="331" alt="image" src="https://github.com/user-attachments/assets/3e9b4d14-5e30-4790-abd5-eea9bd3db5e0" />

 <img width="589" height="379" alt="image" src="https://github.com/user-attachments/assets/75c5bad6-ea07-4ab3-a091-a8811f2d5007" />

 <img width="589" height="205" alt="image" src="https://github.com/user-attachments/assets/61b54611-1657-4d55-aa54-4fddd50a27f3" />

 <img width="589" height="137" alt="image" src="https://github.com/user-attachments/assets/a23217fe-4a87-47fd-9be9-b9ddf751521b" />

 <img width="589" height="182" alt="image" src="https://github.com/user-attachments/assets/53d28b3f-06d9-40c8-8976-4afecf9e6e93" />

 <img width="589" height="104" alt="image" src="https://github.com/user-attachments/assets/847808fe-3b02-4619-8367-90ee6ad66c7e" />

 <img width="589" height="244" alt="image" src="https://github.com/user-attachments/assets/6763e118-551a-4ece-9afa-a1a0187f950c" />

 <img width="589" height="180" alt="image" src="https://github.com/user-attachments/assets/10b5f7f4-e9d6-4df9-b080-0e49586033df" />

 <img width="589" height="174" alt="image" src="https://github.com/user-attachments/assets/e77446c2-65f7-486c-8569-63a624ed131a" />

 <img width="589" height="186" alt="image" src="https://github.com/user-attachments/assets/91f24743-f953-4b0e-b61d-88bc5cc9fe12" />

 <img width="589" height="152" alt="image" src="https://github.com/user-attachments/assets/8c1a8b61-d629-4a7b-9a9b-fd98a8eef564" />

 <img width="589" height="176" alt="image" src="https://github.com/user-attachments/assets/b845ec33-9b3c-4324-955b-69ac1ed6ebf1" />

 <img width="589" height="187" alt="image" src="https://github.com/user-attachments/assets/dc876e4c-799c-42c6-8875-31d3cd00a381" />

 <img width="589" height="178" alt="image" src="https://github.com/user-attachments/assets/1aa07752-97e3-463b-88b7-a17486443214" />

 <img width="589" height="235" alt="image" src="https://github.com/user-attachments/assets/5512d7ad-c5b0-4098-9e8c-f7623af484ca" />

 <img width="589" height="420" alt="image" src="https://github.com/user-attachments/assets/65f4bfc1-2022-46be-b0d4-f552b2fda330" />

 <img width="589" height="100" alt="image" src="https://github.com/user-attachments/assets/8850dae1-2818-4e3d-b01d-97160caae012" />

 <img width="589" height="263" alt="image" src="https://github.com/user-attachments/assets/c30e4b24-487f-4501-9f2f-bf1ae4cdaf5d" />

 <img width="589" height="134" alt="image" src="https://github.com/user-attachments/assets/d8c9e3f6-5e12-40ef-8245-864f4e38789a" />

 <img width="589" height="193" alt="image" src="https://github.com/user-attachments/assets/3406a0a8-332c-41ca-a584-48b46f1294df" />

 <img width="589" height="120" alt="image" src="https://github.com/user-attachments/assets/2db5d7e0-9422-4bd8-85ad-1945d3803415" />

 <img width="589" height="93" alt="image" src="https://github.com/user-attachments/assets/2174d0a1-c79c-4f86-adf2-ec5ea6090a7e" />

 <img width="589" height="96" alt="image" src="https://github.com/user-attachments/assets/975f922e-0ee7-4f14-944b-49ea9c2edf47" />

 <img width="589" height="98" alt="image" src="https://github.com/user-attachments/assets/2f0277e2-2360-4251-8944-604b1a334a92" />

 <img width="589" height="119" alt="image" src="https://github.com/user-attachments/assets/0afffe7d-4ad1-4c7f-a393-97bbf40bbd64" />

 <img width="589" height="98" alt="image" src="https://github.com/user-attachments/assets/763c9ca2-8961-4dad-9e57-e245dda96541" />

<img width="589" height="93" alt="image" src="https://github.com/user-attachments/assets/4dfc162f-3fad-48fb-b7b9-1912a8f2e977" />

<img width="589" height="89" alt="image" src="https://github.com/user-attachments/assets/0e96453f-0d94-40ef-b93b-49903827f3eb" />



Project name: **Apache Flink Kafka-to-Kafka Streaming Pipeline**

It reads order events from one Kafka topic, filters orders where total_price > 100, and writes the valid filtered records into another Kafka topic using Apache Flink. The code uses source topic orders_src_flink and target topic orders_tgt_flink.
 
**Files and folders**

**kafka_to_kafka_flink.py**
- Main PyFlink streaming job. It connects to Kafka, reads JSON orders, validates them, filters orders above 100, and publishes them to another Kafka topic. 

**flink_local_setup.txt**
- Instructions to install Apache Flink locally, install PyFlink, configure Python, add Kafka connector JAR, start the Flink cluster, and run the job. 

**Where to upload/place the files**

Place the files like this on your computer:
 
<img width="333" height="166" alt="image" src="https://github.com/user-attachments/assets/01f25a86-527a-4170-bd55-82b258defc25" />

The Kafka connector JAR must go inside:
- flink-1.20.0/lib/

Your Python job can stay in your project folder, for example:
- C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\16 Apache Flink\2 Flink_Code_and_Setup

 Do:
 - cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\16 Apache Flink\2 Flink_Code_and_Setup"
 
Verify:
- dir

You should see:
- flink-1.20.3
- kafka_to_kafka_flink.py
- flink_local_setup.txt
 
*Enter Flink Folder*

Run:
- cd flink-1.20.3

Verify:
- dir

You should see:
- bin
- conf
- lib
- log
- plugins
 
*Install PyFlink*

From CMD:

Run:
- pip install apache-flink==1.20.0 or
- pip3 install apache-flink==1.20.0
 
*Find Python Path*

Run:
- where python

Example output: C:\Users\Usuario\AppData\Local\Programs\Python\Python311\python.exe

In our case is:

<img width="690" height="330" alt="image" src="https://github.com/user-attachments/assets/e11fdd30-3eee-44bd-aeac-44d3c761f303" />

 *Edit Flink Configuration*

Open:
- flink-1.20.3\conf\config.yaml

<img width="638" height="352" alt="image" src="https://github.com/user-attachments/assets/cc91198c-f61b-4856-ba00-760ca300b088" />

Add:
- python.client.executable: C:\Users\Usuario\anaconda3\python.exe
- python.executable: C:\Users\Usuario\anaconda3\python.exe

Here we have it:

<img width="694" height="431" alt="image" src="https://github.com/user-attachments/assets/34c9d984-0836-4272-b7df-ade5881b116b" />

*Kafka Connector*

Download: **flink-sql-connector-kafka-1.17.2.jar**

Copy it into: flink-1.20.3\lib
 
Lets explain this in detail.
 
Yes. The JAR file needs to be downloaded manually and copied into your Flink lib folder. The file is available from Maven Central.

*Step 1: Download the Kafka Connector*

Open this page in your browser:

Link: flink-sql-connector-kafka-1.17.2 Download
- Then click: flink-sql-connector-kafka-1.17.2.jar

The file size should be approximately 5.5 MB.

*Step 2: Save the File*

Save it anywhere convenient, for example:
- C:\Users\Usuario\Downloads\

*Step 3: Copy the JAR to Flink*
- Copy: flink-sql-connector-kafka-1.17.2.jar

into:
- C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\16 Apache Flink\2 Flink_Code_and_Setup\flink-1.20.3\lib 
 
After copying, your lib folder should contain something like:

<img width="335" height="118" alt="image" src="https://github.com/user-attachments/assets/0d534aeb-6de8-41a6-916a-0f4d2b567c65" />

*Step 4: Verify*

- Open: C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\16 Apache Flink\2 Flink_Code_and_Setup\flink-1.20.3\lib

You should see:
- flink-sql-connector-kafka-1.17.2.jar

listed together with the other Flink JARs.

*Step 5: Restart Flink*

If Flink is already running:

Command Prompt
- cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\16 Apache Flink\2 Flink_Code_and_Setup\flink-1.20.3"

bin\stop-cluster.bat
bin\start-cluster.bat

In our folder are these:

<img width="694" height="429" alt="image" src="https://github.com/user-attachments/assets/d3561382-1721-4db7-9aab-b3f9d4e1b0e1" />

This reloads the new Kafka connector. After that, your PyFlink Kafka job (kafka_to_kafka_flink.py) will be able to access Kafka through the connector.

*Start Flink Cluster (Windows)*

You do NOT use:
- ./bin/start-cluster.sh

Instead use:
- cd bin
- start-cluster.bat or .\start-cluster.bat

*Open Flink GUI* 

Open browser: http://localhost:8081

You should see the Flink Dashboard.

*Run Your Flink Job*

Return to the Flink root folder:
- cd ..

You should now be inside:
- ...\2 Flink_Code_and_Setup\flink-1.20.3

Run:

<img width="300" height="50" alt="image" src="https://github.com/user-attachments/assets/e8df9e22-d2df-4c41-846d-65cd504c3253" />

Because your Python file is one folder above the Flink installation.

Alternative full path:
- bin\flink.bat run -py "%USERPROFILE%\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\16 Apache Flink\2 Flink_Code_and_Setup\kafka_to_kafka_flink.py"

The job will read from Kafka topic: **orders_src_flink**

Filter records where:

<img width="173" height="52" alt="image" src="https://github.com/user-attachments/assets/dea6cf13-8748-466f-ae72-c52996d84ef8" />

and write them to:
- **orders_tgt_flink**

as defined in your Python file.

**Commands You Will Actually Run on Windows**

</>
- cd "%USERPROFILE%\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\16 Apache Flink\2 Flink_Code_and_Setup"
- cd flink-1.20.3
- pip install apache-flink==1.20.0
- where python
- cd bin
- start-cluster.bat
- cd .. (This returns to the Flink root folder)
- bin\flink.bat run -py ..\kafka_to_kafka_flink.py

These are the exact CMD commands for your Windows setup based on the folder structure shown in your screenshots.

