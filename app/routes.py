from flask import request, jsonify, current_app
from .models import Employee
from . import db

def register_routes(app):
    @app.route('/')
    def index():
        current_app.logger.info("Index route accessed")
        return "Welcome to the Employee API!"

    @app.route('/employees', methods=['GET'])
    def get_employees():
        current_app.logger.info("Get employees route accessed")
        employees = Employee.query.all()
        return jsonify([e.as_dict() for e in employees])

    @app.route('/employee/<int:id>', methods=['GET'])
    def get_employee(id):
        current_app.logger.info(f"Get employee {id} route accessed")
        employee = Employee.query.get_or_404(id)
        return jsonify(employee.as_dict())

    @app.route('/employee', methods=['POST'])
    def add_employee():
        current_app.logger.info("Add employee route accessed")
        data = request.get_json()
        new_employee = Employee(
            name=data['name'],
            department=data['department'],
            workflow=data.get('workflow')
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify(new_employee.as_dict()), 201

    @app.route('/employee/<int:id>', methods=['PUT'])
    def update_employee(id):
        current_app.logger.info(f"Update employee {id} route accessed")
        employee = Employee.query.get_or_404(id)
        data = request.get_json()
        employee.name = data.get('name', employee.name)
        employee.department = data.get('department', employee.department)
        employee.workflow = data.get('workflow', employee.workflow)
        db.session.commit()
        return jsonify(employee.as_dict())

    @app.route('/employee/<int:id>', methods=['DELETE'])
    def delete_employee(id):
        current_app.logger.info(f"Delete employee {id} route accessed")
        employee = Employee.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()
        return '', 204

    @app.route('/populate', methods=['POST'])
    def populate():
        current_app.logger.info("Populate route accessed")
        sample_data = [
            {"name": "Alice", "department": "HR", "workflow": 0.5},
            {"name": "Bob", "department": "Finance", "workflow": 0.7},
            {"name": "Charlie", "department": "Engineering", "workflow": 0.9},
            {"name": "Diana", "department": "Marketing", "workflow": 0.6},
            {"name": "Eve", "department": "Sales", "workflow": 0.8}
        ]
        for data in sample_data:
            new_employee = Employee(**data)
            db.session.add(new_employee)
        db.session.commit()
        return 'Data populated!', 200
