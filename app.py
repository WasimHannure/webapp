from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated in-memory database
DATA_STORE = {"items": ["Python", "Runtime", "Stack"]}

@app.route("/", methods=["GET"])
def home():
    """Root endpoint returning basic status."""
    return jsonify({"status": "healthy", "message": "Welcome to the test stack"})

@app.route("/items", methods=["GET", "POST"])
def manage_items():
    """Endpoint to fetch items or add a new one."""
    if request.method == "POST":
        new_item = request.json.get("item")
        if not new_item:
            return jsonify({"error": "Missing item parameter"}), 400
        DATA_STORE["items"].append(new_item)
        return jsonify({"message": "Item added successfully", "items": DATA_STORE["items"]}), 201
    
    return jsonify(DATA_STORE)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
