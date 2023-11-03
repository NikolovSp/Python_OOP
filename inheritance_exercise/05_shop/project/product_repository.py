from typing import List
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        try:
            current_product = next(filter(lambda p: p.name == product_name, self.products))
            return current_product
        except StopIteration:
            pass

    def remove(self, product_name: str) -> None:
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self) -> str:
        return "\n".join([f"{p.name}: {p.quantity}" for p in self.products])
