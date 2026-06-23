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

Open the code editor. Paste the code from **2 lambda_function.py.**
- Click Deploy.
- Click Test.

That **2 lambda_function.py.**

<img width="641" height="174" alt="image" src="https://github.com/user-attachments/assets/a2230330-c7c4-4ef8-9473-257e837f1802" />

Create a test event.
- Click Test again.

**Part 3 — Lambda with dependency**

For **3 lambda_function.py**, you cannot paste only the file if it uses requests. You must zip the dependency.

The **3 lambda_function.py** is in this folder:

<img width="640" height="186" alt="image" src="https://github.com/user-attachments/assets/dfc07dc2-279c-4105-8dd3-2a810e80be06" />

Use the commands from **commands_to_zip.txt**:

<img width="316" height="144" alt="image" src="https://github.com/user-attachments/assets/eb9672f4-1296-4432-b4ec-98ef02d0cdaa" />

Then in AWS Lambda:

Open the Lambda function. Go to Code.
Click Upload from. Choose .zip file.
- Upload the zip.

Click Save.

Click Test.

Lets explain this in detail.

Your file 3 lambda_function.py imports:

<img width="163" height="54" alt="image" src="https://github.com/user-attachments/assets/00a663da-68d6-491a-86d9-e28e91dc7345" />

AWS Lambda does not automatically include the requests library, so you must upload:
- lambda_function.py
- requests library files

together inside one **.zip** file. This is the **.zip** that you upload.

**What each command does**

<img width="236" height="55" alt="image" src="https://github.com/user-attachments/assets/c8589c31-40b4-4e15-8d28-961777d85b84" />

in our case is: cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\14 AWS\Module 10 - AWS Class 1\3 Lambda_Code\lambda_with_dependency"

Opens the folder where your Lambda code is located.

<img width="268" height="55" alt="image" src="https://github.com/user-attachments/assets/63a91455-de36-4697-8e76-65f52270314a" />

Downloads the requests library into a local folder called package.

<img width="249" height="54" alt="image" src="https://github.com/user-attachments/assets/598f4c7d-02ea-4d75-aca8-f36ffa5cf363" />

in our case is: cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\14 AWS\Module 10 - AWS Class 1\3 Lambda_Code\lambda_with_dependency\package"

Moves inside the dependency folder.

<img width="265" height="61" alt="image" src="https://github.com/user-attachments/assets/c16e2dae-9da0-4010-bf62-b7868c7ececc" />

Creates a zip file and puts all dependency files inside it.

<img width="225" height="56" alt="image" src="https://github.com/user-attachments/assets/57bb694b-c67f-44b5-baa6-5bf067dd8ef4" />

Moves back to the main Lambda folder.

in our case is: cd "C:\Users\Usuario\Desktop\GrowDataSkills\Complete Data Engineering With AWS - Basic To Advance\14 AWS\Module 10 - AWS Class 1\3 Lambda_Code\lambda_with_dependency"

<img width="305" height="58" alt="image" src="https://github.com/user-attachments/assets/c3750982-2b0f-4d5b-9e80-fcba971418af" />

Adds your actual Lambda code into the same zip file.

*Final zip should contain*

Inside **lambda_code_dep_zipped.zip**, AWS Lambda should see this structure:
- lambda_function.py
- requests/
- urllib3/
- certifi/
- charset_normalizer/
- idna/
- other dependency files...

Very important: lambda_function.py must be at the root level of the zip, not inside another folder.

**AWS Lambda GUI steps**

Go to AWS Console. Search Lambda. Open your Lambda function.

Click the Code tab. Click Upload from. Choose .zip file.
- Select: **lambda_code_dep_zipped.zip**

Click Save.

Make sure the handler is:
- lambda_function.lambda_handler

Click Test.

Create a test event.

Click Test again.

**Part 4 — GitHub Actions CI/CD setup**

Open your GitHub repository.

Click Add file → Create new file.

Create: **lambda_function/app.py**. Paste the **app.py** code.

Create: **lambda_function/requirements.txt**. 
- Paste:
  - requests
  - pandas
  
Create: **.github/workflows/deploy.yml**
- Paste your **deploy.yml.**

**Part 5 — Add GitHub Secrets**

In GitHub: Open your repository.

Click Settings. Click Secrets and variables. Click Actions. Click New repository secret.
- Add: **AWS_ACCESS_KEY_ID**

Click New repository secret again.
- Add: **AWS_SECRET_ACCESS_KEY**

Lets explain this in detail.

**Add GitHub Secrets (Exact GUI Steps)**

These secrets allow GitHub Actions to authenticate with AWS and deploy your Lambda function automatically.

*Part A — Create AWS Access Keys*

*1. Open AWS Console*

Go to: https://console.aws.amazon.com

Login.

*2. Open IAM*

In the search bar at the top type: IAM
- Click: IAM

*3. Open Users*

Left menu: Users. Click: Users

*4. Select Your User*

Example: admin or alejandro

Click your username.

*5. Open Security Credentials*

Top tabs:
- Permissions
- Groups
- Tags
- Security credentials

Click: Security credentials

*6. Create Access Key*

Scroll down until you see: Access keys

Click: Create access key

*7. Select Use Case*

Choose: Command Line Interface (CLI)

Click: Next

*8. Create Key*

Click: Create access key

AWS generates:
- Access Key ID
- Secret Access Key

Example:
- Access Key ID: AKIAxxxxxxxxxxxx
- Secret Access Key: aBcDeFgHiJkLmNoPqRsTuVwXyZ

Copy both values immediately.

AWS only shows the Secret Access Key once.

*Open GitHub Repository*

*1. Open GitHub*

Go to: https://github.com

Open your repository.

Example: **aws-lambda-cicd-project**

*2. Open Settings*

Top menu:
- Code
- Issues
- Pull Requests
- Actions
- Projects
- Wiki
- Settings

Click: Settings

*3. Open Secrets*

Left menu: Secrets and variables. Expand it.
- Click: Actions

Path:
Settings
    ↓
Secrets and variables
    ↓
Actions

*Part C — Create AWS_ACCESS_KEY_ID*

Click: New repository secret

You will see:
- Name
- Secret

Fill in:
- Name: **AWS_ACCESS_KEY_ID**
- Secret: Paste: AKIAxxxxxxxxxxxx

(the Access Key ID from AWS)

Click: Add secret

*Part D — Create AWS_SECRET_ACCESS_KEY*

Click: New repository secret

Fill in:
- Name: **AWS_SECRET_ACCESS_KEY**
- Secret: Paste: aBcDeFgHiJkLmNoPqRsTuVwXyZ

(the Secret Access Key from AWS)

Click: Add secret

*Part E — Verify Secrets*

You should now see:
- **AWS_ACCESS_KEY_ID**
- **AWS_SECRET_ACCESS_KEY**

under: Repository secrets

*What GitHub Uses Them For*

When you push code:

# 🚀 AWS Lambda Deployment Architecture

```text
Git Push
    ⬇️
GitHub Actions
    ⬇️
deploy.yml
    ⬇️
Reads AWS_ACCESS_KEY_ID
    ⬇️
Reads AWS_SECRET_ACCESS_KEY
    ⬇️
Connects to AWS
    ⬇️
Updates Lambda Function
```

## 📋 Workflow Summary

- 👨‍💻 Developer performs a Git Push
- ⚙️ GitHub Actions workflow is triggered
- 📄 `deploy.yml` starts executing
- 🔐 Reads `AWS_ACCESS_KEY_ID` from GitHub Secrets
- 🔐 Reads `AWS_SECRET_ACCESS_KEY` from GitHub Secrets
- ☁️ Authenticates and connects to AWS
- 🚀 Updates the AWS Lambda function with the latest deployment package

*Optional (Recommended)*

Instead of using an Administrator user, create a dedicated IAM user such as: **github-actions-lambda**

and give it only:
- AWSLambda_FullAccess
- IAMReadOnlyAccess

This is the production best practice for CI/CD deployments.

Lets continue.

**Part 6 — Run deployment**

Go to your repository. Click Actions. Click Deploy Lambda.

Push code to either: main or test

GitHub Actions will create/update Lambda: **cicd_lambda_main** or **cicd_lambda_test**

**Final result**

At the end, your project automatically deploys an AWS Lambda function every time you push changes to GitHub. The Lambda installs dependencies, calls an API, processes the response with pandas, reads environment variables, and logs the output in CloudWatch.







