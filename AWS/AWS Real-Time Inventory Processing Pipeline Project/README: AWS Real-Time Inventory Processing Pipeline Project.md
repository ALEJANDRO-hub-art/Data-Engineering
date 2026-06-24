I have this project AWS Real-Time Inventory Processing Pipeline Project.

<img width="669" height="253" alt="image" src="https://github.com/user-attachments/assets/a439d79f-f9fd-484f-bff4-21a2146ab62f" />

<img width="795" height="153" alt="image" src="https://github.com/user-attachments/assets/081be397-83e4-4ca8-b002-b076c538ab55" />

<img width="766" height="162" alt="image" src="https://github.com/user-attachments/assets/8b64b56f-13ca-40a4-b7ca-e52d67c0987f" />

<img width="844" height="232" alt="image" src="https://github.com/user-attachments/assets/7dd87989-1090-48da-8797-352cb647d774" />

<img width="680" height="273" alt="image" src="https://github.com/user-attachments/assets/7ac66d22-e6e5-4fda-89e4-7b6c5525c194" />


The assignment objective is to build a real-time pipeline that captures simulated e-commerce inventory events, processes them, and updates DynamoDB with the latest inventory state.

<img width="673" height="306" alt="image" src="https://github.com/user-attachments/assets/c96c9b4c-a983-48f8-b885-5c69f6aed6ac" />

The generator sends events like product_added, product_removed, and product_quantity_changed into Kinesis every second. The Lambda currently handles product_added with put_item() and product_removed with delete_item() against the DynamoDB table product_inventory.













