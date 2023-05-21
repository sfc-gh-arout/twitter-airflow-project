# Twitter-Airflow-Project
Data Engineering project using Airflow


## Overview

This project scraps Tweets of the mentioned user from Twitter API using developer account, cleans the data to store data from JSON to a more readable CSV format using Python and finally schedules using the open source orchestrator tool Airflow to load the final CSV data to the AWS S3 bucket.


### Architecture

![Twitter Airflow project](https://github.com/sfc-gh-arout/twitter-airflow-project/blob/main/Twitter_project.png)


### Documentation refered

Tweepy API authentication - https://docs.tweepy.org/en/stable/getting_started.html

PythonOperator in Airflow - https://airflow.apache.org/docs/apache-airflow/stable/howto/operator/python.html#pythonoperator


### Requirements

Twitter developer account

AWS account

EC2 preferably t3.medium - Ubuntu

S3 bucket

Apache Airflow Standard

Python Pandas

Open 8080 port in EC2 inbound rules

Create a new IAM role in EC2 to be able to upload CSV from EC2 to S3 bucket.


### Process followed

 *Used Mac machine and Visual Studio Code for local development*.
- Create or access your Twitter Developer account using https://developer.twitter.com/
- Go to portal >> Projects&Apps >> Add App >> Key Access and Tokens and copy the API key and API secret Key.
- Once App is created go to Keys and Tokens and copy the Access token and Access token secret as well. 
- Create 2 python files using Twitter_etl_cleaned.py and twitter_dag.py in the local environment.
- Key in the consumer_key, consumer_secret, access_token, access_token_secret in the Twitter_etl_cleaned.py from the keys copied in the above steps.
- You can check by running Twitter_etl_cleaned.py locally to see if it executes or not.
- Go to your AWS account and spin a EC2 machine preferably t3 medium (please note this is not free) or t2 micro(this is free) and install Ubuntu.
- Create a S3 bucket in the region closest to you.
- Create a new IAM role in the EC2 and give AmazonS3FullAccess and AmazonEC2FullAccess(for development purpose only, not advised in production).
- Open the port 8080 for all or your IP in the EC2 to be able to connect to the Airflow server from web.
- Connect to the EC2 machine and run commands.bash file to install the necesary packages. 
- Run the command ***Airflow Standalone*** in Ubuntu(EC2) which will start the airflow server.
- the user name and password will be mentioned on the ubuntu screen message when airflow is started using the command above.
- Copy the public Ipv4 DNS name of the EC2 machine and append :8080 in the end on your browser to connect to the Airflow server from your machine using the username and password.
- Go to the Airflow directory in Ubuntu(EC2) and modify the airflow.cfg file to change the dags_folder to /home/ubuntu/airflow/twitter_dag and save the file.
- Create a folder name twitter_dag in the airflow directory and copy the Twitter_etl_cleaned.py and twitter_dag.py from local environment to here.
- Stop the airflow server using Ctrl+C and start using ***Airflow Standalone***. 
- Check the Airflow Web, the DAG should be visible. Trigger the DAG and you should see a CSV saved to the S3 upon successfull run.

**Enjoy the Project!**



