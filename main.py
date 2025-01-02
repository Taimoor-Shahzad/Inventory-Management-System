class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

    def update_stock(self, quantity):
        if quantity < 0 and abs(quantity) > self.stock_quantity:
            raise ValueError("Cannot reduce stock below zero.")
        self.stock_quantity += quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: {self.price}, Stock: {self.stock_quantity}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id in self.products:
            raise ValueError("Product already exists.")
        self.products[product.product_id] = product

    def update_product(self, product_id, **kwargs):
        product = self.products.get(product_id)
        if not product:
            raise ValueError("Product not found.")
        for key, value in kwargs.items():
            setattr(product, key, value)

    def delete_product(self, product_id):
        if product_id not in self.products:
            raise ValueError("Product not found.")
        del self.products[product_id]

    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products.values():
                print(product)

    def search_by_name(self, name):
        found = [prod for prod in self.products.values() if name.lower() in prod.name.lower()]
        return found

    def filter_by_stock(self, threshold):
        return [prod for prod in self.products.values() if prod.stock_quantity <= threshold]

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def authenticate(self, input_username, input_password):
        return self.username == input_username and self.password == input_password

class IMS:
    def __init__(self):
        self.inventory = Inventory()
        self.users = [
            User("admin", "admin123", "Admin"),
            User("user1", "password", "User")
        ]
        self.logged_in_user = None

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.authenticate(username, password):
                self.logged_in_user = user
                print(f"Welcome, {user.username}!")
                return True
        print("Invalid username or password.")
        return False

    def show_menu(self):
        if self.logged_in_user.role == "Admin":
            print("1. Add Product\n2. Update Product\n3. Delete Product\n4. View Products\n5. Search Products\n6. Filter by Stock\n7. Logout")
        else:
            print("1. View Products\n2. Search Products\n3. Filter by Stock\n4. Logout")

    def execute_choice(self, choice):
        if choice == 1:
            if self.logged_in_user.role == "Admin":
                name = input("Enter product name: ")
                category = input("Enter category: ")
                price = float(input("Enter price: "))
                stock_quantity = int(input("Enter stock quantity: "))
                product_id = len(self.inventory.products) + 1
                product = Product(product_id, name, category, price, stock_quantity)
                self.inventory.add_product(product)
            else:
                print("You don't have permission to add products.")
        elif choice == 2:
            if self.logged_in_user.role == "Admin":
                product_id = int(input("Enter product ID to update: "))
                update_field = input("Enter field to update (name, category, price, stock_quantity): ")
                update_value = input(f"Enter new value for {update_field}: ")
                self.inventory.update_product(product_id, **{update_field: update_value})
            else:
                print("You don't have permission to update products.")
        elif choice == 3:
            if self.logged_in_user.role == "Admin":
                product_id = int(input("Enter product ID to delete: "))
                self.inventory.delete_product(product_id)
            else:
                print("You don't have permission to delete products.")
        elif choice == 4:
            self.inventory.view_products()
        elif choice == 5:
            name = input("Enter product name to search: ")
            products = self.inventory.search_by_name(name)
            for product in products:
                print(product)
        elif choice == 6:
            threshold = int(input("Enter stock threshold: "))
            products = self.inventory.filter_by_stock(threshold)
            for product in products:
                print(product)
        elif choice == 7:
            print("Logging out...")
            self.logged_in_user = None
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ims = IMS()

    if ims.login():
        while True:
            ims.show_menu()
            choice = int(input("Enter your choice: "))
            ims.execute_choice(choice)