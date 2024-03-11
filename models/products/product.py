from database.products import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    # Other fields...

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            # Other fields...
        }
