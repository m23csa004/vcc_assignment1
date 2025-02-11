from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = [
        {"id": 101, "item": "Laptop"},
        {"id": 102, "item": "Phone"}
    ]
    return jsonify(orders)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081)
