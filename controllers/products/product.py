from .services import ProductService

class ProductController:
    def __init__(self):
        self.product_service = ProductService()

    def register_product(self, data):
        return self.product_service.register_product(data)

    def update_product(self, product_id, data):
        return self.product_service.update_product(product_id, data)

    # Other controller methods for retrieval, deletion, etc.
