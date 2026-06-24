I have this project AWS Batch Bank Transactions Processing Pipeline Project.

<img width="726" height="271" alt="image" src="https://github.com/user-attachments/assets/c4075447-156f-48fe-822f-afe49502df6e" />

<img width="733" height="157" alt="image" src="https://github.com/user-attachments/assets/7e11bb67-875b-4567-ad69-24ebfa5a0964" />

<img width="731" height="172" alt="image" src="https://github.com/user-attachments/assets/fe559132-8082-476e-8891-99c309230139" />

<img width="764" height="151" alt="image" src="https://github.com/user-attachments/assets/95bc2324-cab3-4bb5-a066-7c5e7c081bd2" />

<img width="745" height="154" alt="image" src="https://github.com/user-attachments/assets/7c485bba-9787-4216-bd53-a244b560119f" />

<img width="751" height="146" alt="image" src="https://github.com/user-attachments/assets/189a6e72-a3db-4d3a-a296-6ce05e014dba" />

This is one complete AWS data engineering project, not mini projects.

What the project does

A daily bank transactions JSON file is uploaded to Amazon S3. That upload automatically triggers AWS Lambda, which starts an AWS Glue ETL job. Glue cleans the data, removes bad/null records, removes duplicate transaction_id records, converts the data to Parquet, saves it back to S3, and makes it queryable in Amazon Athena. The project also uses CloudWatch + SNS for monitoring and alerts.

Files and where to upload them

<img width="658" height="489" alt="image" src="https://github.com/user-attachments/assets/7f23f7ef-fa0e-4f53-a2f8-6aaecc810925" />








































