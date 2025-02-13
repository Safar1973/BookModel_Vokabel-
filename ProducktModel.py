class ProductModel:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.products.append(product)
        print(f"Product '{name}' added successfully.")

    def list_products(self):
        """
        List all products in the list.
        """
        if not self.products:
            print("No products found.")
        else:
            print("List of Products:")
            for idx, product in enumerate(self.products, start=1):
                print(f"{idx}. Name: {product['name']}, Price: €{product['price']}, Quantity: {product['quantity']}")

    def find_product_by_name(self, name):
        for product in self.products:
            if product["name"].lower() == name.lower():
                return product
        return None
    def update_product_quantity(self, name, new_quantity):
        product = self.find_product_by_name(name)
        if product:
            product["quantity"] = new_quantity
            print(f"Quantity of product '{name}' updated to {new_quantity}.")
        else:
            print(f"No product found with name: {name}")

    def delete_product_by_name(self, name):
        product = self.find_product_by_name(name)
        if product:
            self.products.remove(product)
            print(f"Product '{name}' deleted successfully.")
        else:
            print(f"No product found with name: {name}")
if __name__ == "__main__":
    product_model = ProductModel()
    product_model.add_product("SchoolTasche", 250, 99)
    product_model.add_product("Luftreinigung", 300, 10)
    product_model.list_products()
    found_product = product_model.find_product_by_name("SchoolTasche")
    if found_product:
        print(f"Found product: {found_product['name']}, Price: ${found_product['price']}, Quantity: {found_product['quantity']}")
    product_model.update_product_quantity("SchoolTasche", 7)
    product_model.delete_product_by_name("Luftreinigung")
    product_model.list_products()
