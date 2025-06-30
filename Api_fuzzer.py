# ================================================
# 🚨 DISCLAIMER:
# This script is created for educational purposes 
# only. Use it responsibly and only on websites 
# you own or have explicit permission to access.
#
# Unauthorized access to computer systems is illegal 
# and punishable under local and international laws.
#
# The author (Prasangam Pathak) is not responsible 
# for any misuse or damage caused by this script.
# ================================================

import requests

import sys
print(" Enter the url in this format : http//:example.com/api ")
website = input("Enter the website URL: ") 

res = requests.get(url=website)
if res.status_code == 200:
    print("Website is reachable.")
else:
    print("Website is not reachable. Status code:", res.status_code)

data = res.json()

print("Data fetched from the website:")
print(data)

