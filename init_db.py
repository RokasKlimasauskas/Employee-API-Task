# Automatically populate the db for Docker

from app import create_app, db
from app.models import Employee

def populate_db():
    app = create_app()
    with app.app_context():
        db.create_all()
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

if __name__ == "__main__":
    populate_db()
