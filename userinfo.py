from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {"id": 1, "name": "Amresh"},
        {"id": 2, "name": "Ayush"}
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
