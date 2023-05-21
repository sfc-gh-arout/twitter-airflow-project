# twitter-airflow-project
Data Engineering project using Airflow

## Overview

This project scraps Tweets of the mentioned user from Twitter API using developer account, cleans the data to store data from JSON to a more readable CSV format using Python and finally schedules using the open source orchestrator tool Airflow to load the final CSV data to the AWS S3 bucket.

### Architecture

![Twitter Airflow project](https://github.com/sfc-gh-arout/twitter-airflow-project/blob/main/Twitter_project.png)

#### Documentation refered

Tweepy API authentication - https://docs.tweepy.org/en/stable/getting_started.html
PythonOperator in Airflow - https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/python.html#pythonoperator

#### Requirements

Twitter developer account
AWS account
EC2 preferably t3.medium - Ubuntu
S3 bucket
Apache Airflow Standard
Python Pandas
Open 8080 port in EC2 inbound rules
Create new IAM role to be able to upload CSV from EC2 to S3 bucket.
