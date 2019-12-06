import sys
import requests
import base64
import json
import logging
import pymysql
import csv
import sys
import os
import boto3
import requests
import base64
import json
import logging
import pymysql
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
import pandas as pd
from sqlalchemy import create_engine

# mysql -h shane.cdzgsou1rhh1.us-east-2.rds.amazonaws.com -P 3306 -D production -u shane -p

host = "shane.cdzgsou1rhh1.us-east-2.rds.amazonaws.com"
port = 3306
username = "shane"
database = "production"
password = ""

URL = 'https://owners.honda.com/collision/profirstbodyshop/'
driver = webdriver.Firefox(executable_path="C:/geckodriver.exe")

zip2 = pd.read_excel('D:/DS/zip 3rd.xlsx', dtype='str')
zip2 = zip2['ZIP'].tolist()

df = pd.DataFrame(columns = ['dealer_','street_','city_','state_','zip_','phone_'])

dealer = []
street = []
city = []
state = []
zip = []
phone = []

engine = create_engine('mysql+pymysql://' + username + ':' + password + '@' + host + ':' + str(port) + '/' + database, echo=False)

driver.get(URL)

def main():

    try:
        conn = pymysql.connect(host, user=username, passwd=password, db=database, port=port, use_unicode=True, charset='utf8')
        cursor = conn.cursor()
    except:
        logging.error("could not connect to rds")
        sys.exit(1)


    dealers = {}

    for i in zip2:

        driver.find_element_by_xpath("""//*[@id="dl-zipcode"]""").clear()
        driver.find_element_by_xpath("""//*[@id="dl-zipcode"]""").send_keys(i)
        driver.find_element_by_xpath("""//*[@id="form-zip-search-bodyshop"]/fieldset/div/div/button""").click()

        while True:
            try:
                driver.find_element_by_xpath("""//*[@id="btnLoadMore"]""").click()
            except:
                break

        soup = BeautifulSoup(driver.page_source, 'html5lib')

        dealer_table = soup.find_all(class_="dealer-name")
        for dealer_row in dealer_table:
            dealer_temp = dealer_row.find('span').text
            dealer.append(dealer_temp)

        street_table = soup.select("span.street-address")[1:]
        for street_row in street_table:
            street_temp = street_row.text
            street.append(street_temp)

        city_table = soup.select("span.locality")[1:]
        for city_row in city_table:
            city_temp = city_row.text
            city.append(city_temp.strip(' ,'))

        state_table = soup.select("span.region")[1:]
        for state_row in state_table:
            state_temp = state_row.text
            state.append(state_temp)

        zip_table = soup.select("span.postal-code")[1:]
        for zip_row in zip_table:
            zip_temp = zip_row.text
            zip.append(zip_temp)

        phone_table = soup.select("a.dealer-phone")
        for phone_row in phone_table:
            phone_temp = phone_row.find("span").text
            phone.append(phone_temp)

        df.drop(df.index, inplace=True)

        df['dealer_'] = [data for data in dealer]
        df['street_'] = [data for data in street]
        df['city_'] = [data for data in city]
        df['state_'] = [data for data in state]
        df['zip_'] = [data for data in zip]
        df['phone_'] = [data for data in phone]

        df.to_sql(con=engine, name='dealer_list5', if_exists='append')

        print("Done for", i)

    sql = """INSERT INTO dealer_list_unique5 (dealer_,street_,city_,state_,zip_,phone_)
    SELECT DISTINCT dealer_,street_,city_,state_,zip_,phone_
    FROM dealer_list5; """
    cursor.execute(sql)
    conn.commit()


if __name__=='__main__':
    main()
