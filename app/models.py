from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    child_name = db.Column(db.String(100), nullable=False)
    is_paid = db.Column(db.Boolean, default=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Client('{self.email}', '{self.child_name}', '{self.is_paid}')"