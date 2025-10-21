from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(120), unique=True, nullable=False)
    year_level = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Student {self.name}>"