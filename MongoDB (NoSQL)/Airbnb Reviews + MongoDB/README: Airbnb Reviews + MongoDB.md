We have the Airbnb Reviews + MongoDB Project.

<img width="687" height="210" alt="image" src="https://github.com/user-attachments/assets/ccf641a9-ecd1-44f4-a655-ebd02bdbbb8a" />

<img width="624" height="334" alt="image" src="https://github.com/user-attachments/assets/a10ed6cc-9403-42c3-b470-4061395eeaf8" />

The **mongo_connect.py** file doesnt load **airbnb_reviews.json**; it assumes the JSON data is already stored inside MongoDB. In other words **mongo_connect.py** is not a loader its a **query / analytics script**.

✅ What the script actually does
✔ Connects to MongoDB Atlas

<img width="296" height="87" alt="image" src="https://github.com/user-attachments/assets/027b47d2-3493-4ea9-a865-3105bed95dd2" />

✔ Selects database + collection

<img width="311" height="106" alt="image" src="https://github.com/user-attachments/assets/02be17f9-220e-476b-9ff0-650fae56fe73" />

❌ Does NOT insert any JSON file. (Your instructor commented out insert lines)
✔ Runs a MongoDB aggregation

<img width="358" height="103" alt="image" src="https://github.com/user-attachments/assets/c9628a49-0dbe-46e3-a7e6-55b88aa9edf2" />

✔ Prints the results of the aggregation
It does analytics like:

- Group by country + suburb
- Compute average price












