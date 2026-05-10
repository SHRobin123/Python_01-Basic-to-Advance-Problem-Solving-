#Currency Converter API Example

import requests

amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g. USD): ")
to_currency = input("To currency (e.g. BDT): ")

api_key = "YOUR_API_KEY"

url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"

response = requests.get(url)

data = response.json()

if data["result"] == "success":

    rate = data["conversion_rates"][to_currency]

    converted = amount * rate

    print(f"{amount} {from_currency} = {converted} {to_currency}")

else:
    print("API Error or Invalid currency")

'''
output:-

Enter amount: 10
From currency (e.g. USD): USD
To currency (e.g. BDT): BDT

10 USD = 1100.5 BDT
'''