import json
import requests
import pandas as pd 
import psycopg2
from sqlalchemy import create_engine
import time

ip_address = '127.0.0.1'
api_key = 'efnpmWkIGsgNhMUsxR23G8tbOcYSZAJR1ZW8H1o1tjGPbi/8QODtiCW0FIdPI/kN5hoJnQWhvCiEs9ELymAt9HrL2TnL8N8VuAinq5Yc3J609yyNXuOC96OQf1njb1XN0hXiTB/x7JfeFZpe8b2ymlE+k8bgJOkqgLMUrZDebbk='
endpoint = 'settings/inputs'
start_epoch = '0'
current_time = time.time()
current_time = round(current_time)
print(current_time)
end_epoch = str(current_time)
alchemyengine = create_engine('postgresql+psycopg2://postgres:Stevahn23!!@192.168.1.73:5432/Plant')
if_exists = 'append'

url = 'https://192.168.1.150/api/measurements/historical/5f1bb58a-7895-442b-a3a1-ed8112128526/F/0/'+start_epoch+'/'+end_epoch
headers = {'Accept': 'application/vnd.mycodo.v1+json',
            'X-API-KEY': api_key}
response = requests.get(url, headers=headers, verify=False)
response_dict = json.loads(response.text)
print('Got response_dict')
df = pd.json_normalize(response_dict, record_path='measurements')
print('Made dataframe for Temperature')
df.to_sql('Temperature', alchemyengine, if_exists=if_exists)
print('Written dataframe to Temperature')

url = 'https://192.168.1.150/api/measurements/historical/5f1bb58a-7895-442b-a3a1-ed8112128526/percent/1/'+start_epoch+'/'+end_epoch
headers = {'Accept': 'application/vnd.mycodo.v1+json',
            'X-API-KEY': api_key}
response = requests.get(url, headers=headers, verify=False)
response_dict = json.loads(response.text)
print('Got response_dict')
df = pd.json_normalize(response_dict, record_path='measurements')
print('Made dataframe for Humidity')
df.to_sql('Humidity', alchemyengine, if_exists=if_exists)
print('Written dataframe to Humidity')

url = 'https://192.168.1.150/api/measurements/historical/5f1bb58a-7895-442b-a3a1-ed8112128526/Pa/2/'+start_epoch+'/'+end_epoch
headers = {'Accept': 'application/vnd.mycodo.v1+json',
            'X-API-KEY': api_key}
response = requests.get(url, headers=headers, verify=False)
response_dict = json.loads(response.text)
print('Got response_dict')
df = pd.json_normalize(response_dict, record_path='measurements')
print('Made dataframe for Pressure')
df.to_sql('Pressure', alchemyengine, if_exists=if_exists)
print('Written dataframe to Pressure')


url = 'https://192.168.1.150/api/measurements/historical/5f1bb58a-7895-442b-a3a1-ed8112128526/F/3/'+start_epoch+'/'+end_epoch
headers = {'Accept': 'application/vnd.mycodo.v1+json',
            'X-API-KEY': api_key}
response = requests.get(url, headers=headers, verify=False)
response_dict = json.loads(response.text)
print('Got response_dict')
df = pd.json_normalize(response_dict, record_path='measurements')
print('Made dataframe for Dewpoint')
df.to_sql('Dewpoint', alchemyengine, if_exists=if_exists)
print('Written dataframe to Dewpoint')

url = 'https://192.168.1.150/api/measurements/historical/5f1bb58a-7895-442b-a3a1-ed8112128526/m/4/'+start_epoch+'/'+end_epoch
headers = {'Accept': 'application/vnd.mycodo.v1+json',
            'X-API-KEY': api_key}
response = requests.get(url, headers=headers, verify=False)
response_dict = json.loads(response.text)
print('Got response_dict')
df = pd.json_normalize(response_dict, record_path='measurements')
print('Made dataframe for Altitude')
df.to_sql('Altitude', alchemyengine, if_exists=if_exists)
print('Written dataframe to Altitude')

url = 'https://192.168.1.150/api/measurements/historical/5f1bb58a-7895-442b-a3a1-ed8112128526/Pa/5/'+start_epoch+'/'+end_epoch
headers = {'Accept': 'application/vnd.mycodo.v1+json',
            'X-API-KEY': api_key}
response = requests.get(url, headers=headers, verify=False)
response_dict = json.loads(response.text)
print('Got response_dict')
df = pd.json_normalize(response_dict, record_path='measurements')
print('Made dataframe for Vapor Pressure Deficit')
df.to_sql('Vapor_Pressure_Deficit', alchemyengine, if_exists=if_exists)
print('Written dataframe to Vapor Pressure Deficit')

url = 'https://192.168.1.150/api/measurements/historical/4a6ba274-3fe1-4815-83cf-d1df94353136/lux/0/'+start_epoch+'/'+end_epoch
headers = {'Accept': 'application/vnd.mycodo.v1+json',
            'X-API-KEY': api_key}
response = requests.get(url, headers=headers, verify=False)
response_dict = json.loads(response.text)
print('Got response_dict')
df = pd.json_normalize(response_dict, record_path='measurements')
print('Made dataframe for Light')
df.to_sql('Light', alchemyengine, if_exists=if_exists)
print('Written dataframe to Light')
