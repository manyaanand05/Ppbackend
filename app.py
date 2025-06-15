from flask import jsonify
from config import app, db
from models.user import User
from models.product import Product

@app.route('/')
def hello():
    return jsonify({"message": "Welcome to Pharma Project API!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
