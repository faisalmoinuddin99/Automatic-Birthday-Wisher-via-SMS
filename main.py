import pandas as pd
import datetime
import openpyxl
import requests
import json
import twilio

# Twilio Phone Number: +12059906336
from twilio.rest import Client

account_sid = 'ACdb899526b6219ab64aeb0722960c45dc'
auth_token = '31694f8689d1a4f4a2ec996806e247e4'
client = Client(account_sid, auth_token)

# message = client.messages.create(
#          body='This is the ship that made the Kessel Run in fourteen parsecs?',
#          from_='+15017122661',
#          to='+15558675310'
#      )

# def sendSMS(body,to,form):
#     print(f" SMS send to: {to}, From: {form}, Message: {body} ")
#     s = client.messages.create(f"Message: {body}\n\n From: {form}\n\n To: {to}")
#     print(s.sid)
#
#


df = pd.read_excel('myData.xlsx')
# print(df)

today = datetime.datetime.now().strftime("%d-%m")
yearNow = datetime.datetime.now().strftime("%Y")
# print(year)
writeInd = []
for index,item in df.iterrows():
    # print(index,item["WISH"])
    bday = item["BIRTHDATE"].strftime("%d-%m")
    if today == bday and yearNow not in str(item["YEAR"]):
        message = client.messages \
            .create(
            body= item["WISH"],
            from_='+12059906336',
            to=  item["PHONE.NO"]
        )
        print(message.sid)
        writeInd.append(index)
for i in writeInd:
    yr = df.loc[i,"YEAR"]
    # print(yr)
    df.loc[i,"YEAR"] =f"{yr},{yearNow}"

df.to_excel('myData.xlsx',index= False)
