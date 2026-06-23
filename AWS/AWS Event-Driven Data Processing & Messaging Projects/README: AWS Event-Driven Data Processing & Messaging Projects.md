I have this project AWS Event-Driven Data Processing & Messaging Projects.

<img width="589" height="104" alt="image" src="https://github.com/user-attachments/assets/3f1dd8d8-34f8-4b77-8c62-1f3549156ee5" />

This is not one single project. **It is a collection of 5 AWS Event-Driven Architecture mini-projects**, each demonstrating a different AWS integration pattern.

 <img width="284" height="159" alt="image" src="https://github.com/user-attachments/assets/91a7ef9f-98a8-4814-8959-242120588a7e" />

**Mini Project 1: EventBridge Pipes**

Folder: 2 Event_Bridge_Pipe

Purpose:
- Demonstrates:

Producer
<br>⬇️
<br>SQS Queue
<br>⬇️
<br>EventBridge Pipe
<br>⬇️
<br>Filtering
<br>⬇️
<br>Transformation
<br>⬇️
<br>Target Service

The sample file contains:
- Purchase order messages
- Event filtering
- Event transformation

Architecture:

```text
Application
<br>⬇️
SQS
<br>⬇️
EventBridge Pipe
<br>⬇️
Filter Events
<br>⬇️
Transform Payload
<br>⬇️
<br>Target
```

















