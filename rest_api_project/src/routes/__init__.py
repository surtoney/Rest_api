from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/example', methods=['GET'])
def example():
    return {"message": "This is an example endpoint."}

@api.route('/example', methods=['POST'])
def create_example():
    return {"message": "Example created."}, 201

@api.route('/example/<int:id>', methods=['GET'])
def get_example(id):
    return {"message": f"Retrieved example with id {id}."}

@api.route('/example/<int:id>', methods=['PUT'])
def update_example(id):
    return {"message": f"Updated example with id {id}."}

@api.route('/example/<int:id>', methods=['DELETE'])
def delete_example(id):
    return {"message": f"Deleted example with id {id}."}