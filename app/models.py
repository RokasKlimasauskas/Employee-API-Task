from . import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    department = db.Column(db.String(80), nullable=False)
    workflow = db.Column(db.Float, nullable=True)

    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}
