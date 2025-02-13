class ProductTable:
    def __init__(self):
        self.products = []

    def add_product(self, name, price):
        self.products.append({"name": name, "price": price})

    def display_products(self):  # Hier wurde der Doppelpunkt hinzugefügt
        print("Produktliste:")
        for product in self.products:
            print(f"Name: {product['name']}, Preis: {product['price']}")

# Beispielverwendung
if __name__ == "__main__":
    product_table = ProductTable()
    product_table.add_product("ElecktroHeizung", 249.99)
    product_table.add_product("KinderFahrad", 199.99)
    product_table.display_products()