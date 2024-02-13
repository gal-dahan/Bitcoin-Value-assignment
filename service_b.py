from flask import Flask, jsonify
import time
import requests
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

BITCOIN_VALUES = {}


def fetch_bitcoin_value():
    #url = "http://localhost:8000/bitcoin_value"
    service_a_url = "http://service-a:8000/bitcoin_value"

    response = requests.get(service_a_url)

    if response.status_code == 200:
        data = response.json()
        timestamp = data.get('timestamp', '')
        bitcoin_value = data.get('bitcoin_value', '')
        print(timestamp)
        print(bitcoin_value)
        return timestamp, bitcoin_value
    else:
        print(f"Error: Unable to fetch data from service-A. Status code: {response.status_code}")
        return None, None


def calculate_average_value():
    if BITCOIN_VALUES:
        print(BITCOIN_VALUES)
        average_value = sum(BITCOIN_VALUES.values()) / len(BITCOIN_VALUES)
        return average_value
    return None


@app.route('/average')
def get_average_value():
    average_value = calculate_average_value()
    if average_value is not None:
        return jsonify({'Average value of BITCOIN the last 10 minutes': average_value, 'bitcoin_values': BITCOIN_VALUES})
    else:
        return "Not enough data for calculation."


def update_values():
    print("update_values")
    timestamp, bitcoin_value = fetch_bitcoin_value()
    if timestamp and bitcoin_value:
        BITCOIN_VALUES[timestamp] = bitcoin_value
        if len(BITCOIN_VALUES) > 10:
            oldest_timestamp = sorted(BITCOIN_VALUES.keys())[0]
            del BITCOIN_VALUES[oldest_timestamp]


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_values, 'interval', minutes=1)
    scheduler.start()

    app.run(debug=True, host='0.0.0.0', port=5000)
