from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for food items
food_items = [
    {"id": 1, "name": "Burger", "price": 5.99},
    {"id": 2, "name": "Pizza", "price": 8.99},
    {"id": 3, "name": "Pasta", "price": 7.49},
]

# Route to get all food items
@app.route('/food', methods=['GET'])
def get_food_items():
    return jsonify(food_items)

# Route to get a specific food item by ID
@app.route('/food/<int:item_id>', methods=['GET'])
def get_food_item(item_id):
    item = next((item for item in food_items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Food item not found"}), 404
    return jsonify(item)

# Route to add a new food item
@app.route('/food', methods=['POST'])
def add_food_item():
    new_item = request.get_json()
    if not new_item or 'name' not in new_item or 'price' not in new_item:
        return jsonify({"error": "Invalid data"}), 400

    # Generate a new unique ID
    new_id = max(item['id'] for item in food_items) + 1
    new_item['id'] = new_id
    food_items.append(new_item)
    return jsonify(new_item), 201

# Route to update a food item by ID
@app.route('/food/<int:item_id>', methods=['PUT'])
def update_food_item(item_id):
    updated_item = request.get_json()
    if not updated_item or 'name' not in updated_item or 'price' not in updated_item:
        return jsonify({"error": "Invalid data"}), 400

    item = next((item for item in food_items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Food item not found"}), 404

    item['name'] = updated_item['name']
    item['price'] = updated_item['price']
    return jsonify(item)

# Route to delete a food item by ID
@app.route('/food/<int:item_id>', methods=['DELETE'])
def delete_food_item(item_id):
    item = next((item for item in food_items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error": "Food item not found"}), 404

    food_items.remove(item)
    return jsonify({"message": "Food item deleted"})

if __name__ == '__main__':
    app.run(debug=True)