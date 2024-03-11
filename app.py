from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from product_controller import ProductController

app = Flask(__name__)
# we can change the secret key if required
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

product_controller = ProductController()

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username != 'admin' or password != 'admin123':
        return jsonify({"msg": "Bad username or password"}), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

@app.route('/products', methods=['POST'])
@jwt_required()
def register_product():
    data = request.json
    try:
        product = product_controller.register_product(data)
        return jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    data = request.json
    try:
        product = product_controller.update_product(product_id, data)
        return jsonify(product), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Other endpoints for retrieval, deletion, etc.

if __name__ == '__main__':
    app.run(debug=True)
