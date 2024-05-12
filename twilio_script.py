import os
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,TWILIO_PHONE_NUMBER,API_KEY_WAPI,USER_PHONE
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import requests
from tqdm import tqdm
from datetime import datetime
from utils import request_wapi,get_forecast,create_df,send_message,get_date,send_message_whatsapp



query = 'Valencia/Spain'
api_key = API_KEY_WAPI

input_date= get_date()
response = request_wapi(api_key,query)

datos = []

for i in tqdm(range(24),colour = 'green'):

    datos.append(get_forecast(response,i))


df_rain = create_df(datos)

# Send Message
message_id = send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df_rain,query)


print('Mensaje SMS enviado con exito ' + message_id)

message_id = send_message_whatsapp(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,input_date,df_rain,query)

print('Mensaje Whatsapp enviado con exito ' + message_id)
