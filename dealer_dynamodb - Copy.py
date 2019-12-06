import sys
import os
import boto3
import requests
import base64
import json
import logging
import pymysql


host = "shane.cdzgsou1rhh1.us-east-2.rds.amazonaws.com"
port = 3306
username = "shane"
database = "production"
password = ""


access_key = ''
secret_key = ''
region = 'us-east-2'

def main():

    try:
        # client = boto3.client('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)
        dynamodb = boto3.resource('dynamodb', region_name='us-east-2', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    except:
        logging.error('could not connect to dynamodb')
        sys.exit(1)

    try:
        conn = pymysql.connect(host, user=username, passwd=password, db=database, port=port, use_unicode=True, charset='utf8')
        cursor = conn.cursor()
    except:
        logging.error("could not connect to rds")
        sys.exit(1)


    table = dynamodb.Table('dealer_list')
    print(table)

    cursor.execute('SELECT * FROM dealer_list_unique_alll;')

    for row in cursor.fetchall():
        row = row[1:]
        print(row)

        data = {
            'dealer': row[0],
            'street': row[1],
            'city': row[2],
            'state': row[3],
            'zip': row[4],
            'phone': row[5]
        }

        # data.update(track)
        # print(data)
        table.put_item(Item=data )



if __name__=='__main__':
    main()
