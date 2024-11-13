from ..model import Product

from ..database import database

from ..service.product_service import ProductService


class ProductController:
    product_service = ProductService()

    def get_products(self):
        products = self.product_service.get_products()

        if not products:
            return {"message": "Products not found."}, 404

        return [
            {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "stock_quantity": product.stock_quantity,
                "brand": product.brand,
                "weight": product.weight,
                "dimension": product.dimension,
                "color": product.color,
            }
            for product in products
        ], 200

    def get_product(self, id: int):
        product = self.product_service.get_product_by_id(id=id)

        if not product:
            return {"message": "Product not found."}, 404

        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "brand": product.brand,
            "weight": product.weight,
            "dimension": product.dimension,
            "color": product.color,
        }, 200
