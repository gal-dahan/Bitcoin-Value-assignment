from flask import Flask, jsonify
import requests
import random
from datetime import datetime

app = Flask(__name__)


def generate_random_bitcoin_value():
    timestamp = datetime.now().isoformat()

    bitcoin_value = round(random.uniform(5000, 60000), 2)

    return timestamp, bitcoin_value


"""

def fetch_bitcoin_value():
    url = "https://rest.coinapi.io/v1/exchangerate/BTC/USD"
    headers = {
        "X-CoinAPI-Key": "A84A3789-3DDA-4F6A-BBF2-A766BE3B97D7"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    timestamp = data.get('time', '')
    bitcoin_value = data.get('rate', '')

    return timestamp, bitcoin_value

    """


@app.route('/bitcoin_value')
def get_bitcoin_value():
    timestamp, bitcoin_value = generate_random_bitcoin_value()
    response = {
        "message": f"Service A, bitcoin value is {bitcoin_value}$ for '{timestamp}'",
        "timestamp": timestamp,
        "bitcoin_value": bitcoin_value
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
