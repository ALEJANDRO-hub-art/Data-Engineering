I have the following project Kafka + Spark Stateful Transaction Aggregation Project.

<img width="858" height="233" alt="image" src="https://github.com/user-attachments/assets/52b3b7e6-30fc-4019-8f33-90717c9fe552" />

**It has 2 Spark streaming jobs:**

Stateful GroupBy Aggregation
- File: **kafka_spark_stateful_groupby.py**
- Calculates total transaction amount per user.
- 
Stateful Window GroupBy Aggregation
- File: **kafka_spark_stateful_window_groupby.py**
- Calculates total transaction amount per user every 3-minute window.

The producer sends JSON transaction data into Kafka **topic trx_topic_data.**
The dataset is **user_transactions(1).json.**

**Files and where to upload them**

Put all files in one local project folder on Windows:

C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\8 Spark\Module 5 - Spark Class 5\1 Class Content PPT, Notes, Exercises DONE\Stateful_GroupBy_Streaming_Pipeline DONE

<img width="707" height="167" alt="image" src="https://github.com/user-attachments/assets/28adbe59-6e72-4061-9b2e-8e41d35f40eb" />

<img width="711" height="314" alt="image" src="https://github.com/user-attachments/assets/cece4fa6-9871-4c90-a6d9-4300e90cd67f" />



























