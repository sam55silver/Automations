import requests
import time
from datetime import datetime

BITCOIN_URL = 'https://api.coindesk.com/v1/bpi/currentprice/CAD.json'
NOTIFICATION_URL = 'https://maker.ifttt.com/trigger/{}/with/key/cy77aFy2BpKy86YIMGvK6f'

BITCOIN_THRESHOLD = 100000


def get_latest_bitcoin_price():
    r = requests.get(BITCOIN_URL)
    r_json = r.json()
    return float(r_json['bpi']['CAD']['rate_float'])


def webhook(event, value):
    # Value being sent to webhook
    data = {'value1': value}
    # inserts desired event
    url = NOTIFICATION_URL.format(event)
    requests.post(url, json=data)


def main():
    try:
        while True:
            price = get_latest_bitcoin_price()
            print(f"Bitcoin price {price}")

            # Send notification
            if price < BITCOIN_THRESHOLD:
                webhook('bitcoin_price_emerg', price)
                print(f"Price is {price}. Sending Notification...")

            time.sleep(5*60)
    except KeyboardInterrupt:
        print("\nBYE!\n")


if __name__ == '__main__':
    main()
