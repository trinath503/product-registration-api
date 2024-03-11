from .repository import ProductRepository

class ProductService:
    def __init__(self):
        self.product_repo = ProductRepository()

    def register_product(self, data):
        # Implement validation logic here
        return self.product_repo.create_product(data)

    def update_product(self, product_id, data):
        # Implement validation logic here
        return self.product_repo.update_product(product_id, data)

    # Other service methods for retrieval, deletion, etc.
