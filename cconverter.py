from requests import HTTPError
import requests
import json

cur_code = input()

url = f"http://www.floatrates.com/daily/{cur_code.lower()}.json"
cache = {}
rates = {}
# Save rates for usd and eur first
try:
    r = requests.get(url=url)
    r.raise_for_status()
    rates = json.loads(r.text)
    if cur_code.lower() != 'usd':
        cache['usd'] = rates['usd']['rate']
    else:
        cache['usd'] = 1
    if cur_code.lower() != 'eur':
        cache['eur'] = rates['eur']['rate']
    else:
        cache['eur'] = 1
except HTTPError:
    print("An error occured while connecting to the site")
except requests.RequestException:
    print("Unable to connect, error")

while True:
    conv_code = input()
    if conv_code == '':
        break
    amt = float(input())
    print("Checking the cache...")
    if conv_code.lower() in cache.keys():
        print("Oh! It is in the cache!")
        print(f"You received {round(cache[conv_code.lower()] * amt, 2)} {conv_code}.")
    else:
        print("Sorry, but it is not in the cache!")
        cache[conv_code.lower()] = rates[conv_code.lower()]['rate']
        print(f"You received {round(cache[conv_code.lower()] * amt, 2)} {conv_code}.")
