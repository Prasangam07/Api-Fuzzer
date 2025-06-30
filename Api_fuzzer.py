import requests

import sys
website = input("Enter the website URL: ")

res = requests.get(url=website)
if res.status_code == 200:
    print("Website is reachable.")
else:
    print("Website is not reachable. Status code:", res.status_code)

data = res.json()

print("Data fetched from the website:")
print(data)