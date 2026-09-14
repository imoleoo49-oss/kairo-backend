from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Kairo backend is alive."


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True)

    if data is None:
        return jsonify({
            "reply": "Kairo received an invalid request."
        }), 400

    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "reply": "You sent me absolutely nothing."
        }), 400

    reply = "Kairo received your message: " + message

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=10000
    )
