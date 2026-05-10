from flask import Flask, jsonify, request

app = Flask(__name__)


# Sample Data
items = [
    {"id": 1, "name": "name1", "des": "des1"},
    {"id": 2, "name": "name2", "des": "des2"},
]


# Home Route
@app.route("/")
def home():
    return "Hello"


# =========================================
# GET REQUEST
# Get item by ID
# =========================================
@app.route("/items/<int:id>", methods=["GET"])
def get_item(id):

    # Find item with matching id
    item = next((item for item in items if item["id"] == id), None)

    # If item not found
    if item is None:
        return jsonify({"error": "Item not found"})

    # Return item
    return jsonify(item)


# =========================================
# POST REQUEST
# Create new item
# =========================================
@app.route("/items", methods=["POST"])
def create_item():

    # Create new item
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "des": request.json["des"],
    }

    # Add item to list
    items.append(new_item)

    return jsonify({
        "message": "Item created successfully",
        "item": new_item
    })


# =========================================
# PUT REQUEST
# Update existing item
# =========================================
@app.route("/items/<int:id>", methods=["PUT"])
def update_item(id):

    # Find item
    item = next((item for item in items if item["id"] == id), None)

    # If item not found
    if item is None:
        return jsonify({"error": "Item does not exist"})

    # Update values if provided
    item["name"] = request.json.get("name", item["name"])
    item["des"] = request.json.get("des", item["des"])

    return jsonify({
        "message": "Item updated successfully",
        "item": item
    })


# =========================================
# DELETE REQUEST
# Delete item by ID
# =========================================
@app.route("/items/<int:id>", methods=["DELETE"])
def delete_item(id):

    global items

    # Remove matching item
    items = [item for item in items if item["id"] != id]

    return jsonify({
        "message": "Item deleted successfully"
    })


# =========================================
# Run Flask App
# =========================================
if __name__ == "__main__":
    app.run(debug=True)