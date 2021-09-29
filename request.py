import json
import requests
import pandas as pd 
import psycopg2
from sqlalchemy import create_engine
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ip_address = '127.0.0.1'
api_key = 'YOUR_API_KEY'
endpoint = 'outputs/3f5a4806-c830-432d-b329-7821da8336e4'
url = 'https://{ip}/api/{ep}'.format(ip=ip_address, ep=endpoint)
data = {"state": True}  # Turn Output On
headers = {'Accept': 'application/vnd.mycodo.v1+json',
           'X-API-KEY': api_key}
response = requests.post(url, json=data, headers=headers, verify=False)
print("Response Status: {}".format(response.status_code))
print("Response Headers: {}".format(response.headers))
response_dict = json.loads(response.text)
print("Response Dictionary: {}".format(response_dict))
'''
ip_address = '127.0.0.1'
api_key = 'efnpmWkIGsgNhMUsxR23G8tbOcYSZAJR1ZW8H1o1tjGPbi/8QODtiCW0FIdPI/kN5hoJnQWhvCiEs9ELymAt9HrL2TnL8N8VuAinq5Yc3J609yyNXuOC96OQf1njb1XN0hXiTB/x7JfeFZpe8b2ymlE+k8bgJOkqgLMUrZDebbk='
endpoint = 'settings/inputs'
start_epoch = '0'
end_epoch = '0'
alchemyengine = create_engine('postgresql+psycopg2://postgres:Stevahn23!!@192.168.1.73:5432/Plant')
if_exists = 'append'


url = 'https://192.168.1.150/api/measurements/historical/5f1bb58a-7895-442b-a3a1-ed8112128526/F/0/'+start_epoch+'/'+end_epoch
headers = {'Accept': 'application/vnd.mycodo.v1+json',
            'X-API-KEY': api_key}
response = requests.post(url,data,json)
response_dict = json.loads(response.text)
print('Got response_dict')
df = pd.json_normalize(response_dict, record_path='measurements')
print('Made dataframe for Temperature')
df.to_sql('Temperature', alchemyengine, if_exists=if_exists)
print('Written dataframe to Temperature')
'''