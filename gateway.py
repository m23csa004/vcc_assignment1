from flask import Flask, jsonify
import requests

app = Flask(__name__)

USER_SERVICE = "http://192.168.100.4:8080"
ORDER_SERVICE = "http://192.168.100.5:8081"

@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get(f"{USER_SERVICE}/users")
    return jsonify(response.json())

@app.route('/orders', methods=['GET'])
def get_orders():
    response = requests.get(f"{ORDER_SERVICE}/orders")
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8079)
