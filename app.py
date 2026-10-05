from flask import Flask, request, jsonify

app = Flask(__name__)

latest_data = {}

@app.route("/price", methods=["POST"])
def receive_price():
    global latest_data
    latest_data = request.get_json(force=True)
    return jsonify({"status": "ok"})

@app.route("/price", methods=["GET"])
def get_price():
    return jsonify(latest_data)

@app.route("/")
def home():
    return "Gold Sniper Bridge is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
