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

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

