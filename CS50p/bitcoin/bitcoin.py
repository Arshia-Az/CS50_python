import requests
import sys
import json

try:
    count_of_bitcoin = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()

    rate = o["bpi"]["USD"]["rate_float"]
    price = rate * count_of_bitcoin
    print(f"${price:,.4f}")
except requests.RequestException:
    ...

except IndexError:
    # print("Missing command-line argument")
    sys.exit(1)

except ValueError:
    # print("Command-line argument is not a number")
    sys.exit(1)
