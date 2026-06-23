I have this project AWS Lambda Development & CI-CD Pipeline Project.

<img width="505" height="57" alt="image" src="https://github.com/user-attachments/assets/3686e3d2-85f1-4ad9-9088-71a40c311485" />

<img width="618" height="163" alt="image" src="https://github.com/user-attachments/assets/32ebbb96-7bbf-4280-86fd-a63ae786a5fc" />

<img width="636" height="242" alt="image" src="https://github.com/user-attachments/assets/d837bf38-7bbd-452c-b361-80a74efa5d39" />

<img width="643" height="193" alt="image" src="https://github.com/user-attachments/assets/b9ab9092-4ac6-49c6-842c-ae3f9c436629" />

<img width="658" height="150" alt="image" src="https://github.com/user-attachments/assets/f5b2d223-64ab-4005-aafc-b05b0e13f1d6" />

<img width="625" height="185" alt="image" src="https://github.com/user-attachments/assets/cc089716-65ca-49dc-b87f-c497e0d3313f" />

<img width="644" height="178" alt="image" src="https://github.com/user-attachments/assets/1072adff-6fb4-4968-9ac0-5761df62da04" />

<img width="626" height="211" alt="image" src="https://github.com/user-attachments/assets/ca32d501-3068-4d6e-94ca-bed85dca1523" />

<img width="631" height="170" alt="image" src="https://github.com/user-attachments/assets/34482dd1-4541-4e3b-9c50-8f302b81bf3b" />

**Project name** 

AWS Lambda Development & CI/CD Pipeline Project

Better GitHub title: AWS Lambda CI/CD Deployment Pipeline with GitHub Actions

What this project does

This project teaches AWS Lambda development in 3 stages:
- Basic Lambda function with no dependency.
- Lambda function with local Python module/layer logic using **math_ops.py**.
- Production-style Lambda CI/CD pipeline where GitHub Actions packages app.py, installs dependencies, and deploys to AWS Lambda.

Your screenshots show 3 main folders: 2 S3_Data, 3 Lambda_Code, and 4 AWS_Lambda_CICD_Code. The CI/CD folder contains lambda_function/app.py, requirements.txt, and deploy.yml.

<img width="646" height="570" alt="image" src="https://github.com/user-attachments/assets/b4515db6-55b8-4352-8cf5-30105d945f95" />

**GitHub folder structure**

Use this structure:

<img width="247" height="154" alt="image" src="https://github.com/user-attachments/assets/c576621d-d77e-4655-86f0-15a017459bb2" />

**End-to-end architecture**

# 🚀 AWS Lambda CI/CD Workflow Architecture

```text
Developer pushes code to GitHub
        ⬇️
GitHub Actions starts **deploy.yml**
        ⬇️
Installs Python, zip, jq, boto3
        ⬇️
Installs Lambda dependencies from requirements.txt
        ⬇️
Packages **app.py** + dependencies into lambda.zip
        ⬇️
Uses AWS credentials from GitHub Secrets
        ⬇️
Creates or updates AWS Lambda
        ⬇️
Lambda runs **app.py**
        ⬇️
Lambda calls external API
        ⬇️
Data is loaded into pandas DataFrame
        ⬇️
Logs appear in AWS CloudWatch
```

## 📊 End-to-End Flow

- 👨‍💻 Developer pushes code to GitHub
- ⚙️ GitHub Actions automatically triggers `deploy.yml`
- 🐍 Python environment and required tools are installed
- 📦 Lambda dependencies are installed from `requirements.txt`
- 🗜️ Application code and dependencies are packaged into `lambda.zip`
- 🔐 AWS credentials are retrieved from GitHub Secrets
- ☁️ GitHub Actions creates or updates the AWS Lambda function
- 🚀 AWS Lambda executes `app.py`
- 🌐 Lambda connects to an external API
- 🐼 API data is loaded into a Pandas DataFrame
- 📜 Execution logs are written to AWS CloudWatch

**Step-by-step execution**

**Part 1 — AWS S3 upload**

Go to AWS Console. Search S3. Click Create bucket.
- Name it something like: **aws-lambda-cicd-store-data**

Open the bucket. Click Upload.
- Upload: **store_data.csv**. Click Upload.

**Part 2 — Create Lambda manually**

Go to AWS Console. Search Lambda. Click Create function. Choose Author from scratch.
- Function name: **lambda_with_no_dependency**
- Runtime: **Python 3.11**

Click Create function.

Open the code editor. Paste the code from 2 lambda_function.py. 
- Click Deploy.
- Click Test.

That **2 lambda_function.py.**

<img width="641" height="174" alt="image" src="https://github.com/user-attachments/assets/a2230330-c7c4-4ef8-9473-257e837f1802" />

Create a test event.
- Click Test again.































