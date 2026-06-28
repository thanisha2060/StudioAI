from extensions import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = 'projects'

    id            = db.Column(db.Integer, primary_key=True)
    title         = db.Column(db.String(200), nullable=False)
    category      = db.Column(db.String(100), nullable=False)
    budget        = db.Column(db.Numeric(10, 2), nullable=False)
    delivery_days = db.Column(db.Integer, nullable=False)
    description   = db.Column(db.Text, nullable=True)
    image         = db.Column(db.String(300), nullable=True)
    created_at    = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.title}>'

    def to_dict(self):
        return {
            'id':            self.id,
            'title':         self.title,
            'category':      self.category,
            'budget':        float(self.budget),
            'delivery_days': self.delivery_days,
            'description':   self.description,
            'image':         self.image,
            'created_at':    self.created_at.strftime('%d %b %Y'),
        }
