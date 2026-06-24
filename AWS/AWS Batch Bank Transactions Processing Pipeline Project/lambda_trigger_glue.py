{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f2dfafb-226a-4604-84c0-519c3d859d6d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e22f2893-75ea-40e1-8816-877d3cecc706",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import boto3\n",
    "import os\n",
    "\n",
    "glue_client = boto3.client(\"glue\")\n",
    "sns_client = boto3.client(\"sns\")\n",
    "\n",
    "GLUE_JOB_NAME = os.environ.get(\"GLUE_JOB_NAME\", \"bank-transactions-etl-job\")\n",
    "SNS_TOPIC_ARN = os.environ.get(\"SNS_TOPIC_ARN\", \"\")\n",
    "\n",
    "def lambda_handler(event, context):\n",
    "    try:\n",
    "        # Read S3 event info\n",
    "        record = event[\"Records\"][0]\n",
    "        bucket_name = record[\"s3\"][\"bucket\"][\"name\"]\n",
    "        object_key = record[\"s3\"][\"object\"][\"key\"]\n",
    "\n",
    "        # Only process raw JSON files\n",
    "        if not object_key.startswith(\"raw/\") or not object_key.endswith(\".json\"):\n",
    "            return {\n",
    "                \"statusCode\": 200,\n",
    "                \"body\": json.dumps(\"File ignored. Not a raw JSON file.\")\n",
    "            }\n",
    "\n",
    "        response = glue_client.start_job_run(\n",
    "            JobName=GLUE_JOB_NAME,\n",
    "            Arguments={\n",
    "                \"--SOURCE_BUCKET\": bucket_name,\n",
    "                \"--SOURCE_KEY\": object_key,\n",
    "                \"--TARGET_PATH\": f\"s3://{bucket_name}/processed/\"\n",
    "            }\n",
    "        )\n",
    "\n",
    "        return {\n",
    "            \"statusCode\": 200,\n",
    "            \"body\": json.dumps({\n",
    "                \"message\": \"Glue job started successfully\",\n",
    "                \"jobRunId\": response[\"JobRunId\"]\n",
    "            })\n",
    "        }\n",
    "\n",
    "    except Exception as e:\n",
    "        error_message = f\"Lambda failed to start Glue job: {str(e)}\"\n",
    "\n",
    "        if SNS_TOPIC_ARN:\n",
    "            sns_client.publish(\n",
    "                TopicArn=SNS_TOPIC_ARN,\n",
    "                Subject=\"Bank Transaction Pipeline Failure\",\n",
    "                Message=error_message\n",
    "            )\n",
    "\n",
    "        raise e"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ddd1666-9363-4d61-ab16-bca0bd08dc3d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
