from database import db
from models.products.product import Product

class ProductRepository:
    def create_product(self, data):
        # Implement creation logic and save to database
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product.serialize()

    def update_product(self, product_id, data):
        # Implement update logic and save to database
        product = Product.query.get(product_id)
        if product:
            for key, value in data.items():
                setattr(product, key, value)
            db.session.commit()
            return product.serialize()
        else:
            raise ValueError("Product not found")

    # Other repository methods for retrieval, deletion, etc.
