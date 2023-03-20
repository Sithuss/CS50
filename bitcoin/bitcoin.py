import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
elif sys.argv[1].isalpha():
    sys.exit("Command-line argument is not a number")
else:
    mul = flo(sys.argv[1])

try:
    request =  requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    print("error")


out = request.json()

result = out["bpi"]
val = result["USD"]
value = val["rate_float"]
total = value * mul
print(f"${total:,.4f}")