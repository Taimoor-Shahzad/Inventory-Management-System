import json
from typing import Dict, List

# Paths to Data Files
INVENTORY_FILE = "data/inventory.json"
USERS_FILE = "data/users.json"

# Role Definitions
class Role:
    ADMIN = "Admin"
    USER = "User"

# Custom Exceptions
class AuthenticationError(Exception):
    pass

class AuthorizationError(Exception):
    pass

class ProductNotFoundError(Exception):
    pass

class InsufficientStockError(Exception):
    pass

# User Management
class User:
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role

    def verify_password(self, password: str) -> bool:
        return self.password == password

# Authentication Manager
class AuthenticationManager:
    def __init__(self):
        self.users = self.load_users()

    def load_users(self) -> Dict[str, User]:
        try:
            with open(USERS_FILE, "r") as f:
                data = json.load(f)
            return {
                username: User(username, user_data["password"], user_data["role"])
                for username, user_data in data.items()
            }
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self):
        with open(USERS_FILE, "w") as f:
            json.dump(
                {
                    username: {"password": user.password, "role": user.role}
                    for username, user in self.users.items()
                },
                f,
            )

    def register_user(self, username: str, password: str, role: str):
        if username in self.users:
            raise ValueError("User already exists.")
        self.users[username] = User(username, password, role)
        self.save_users()

    def authenticate_user(self, username: str, password: str) -> User:
        if username not in self.users:
            raise AuthenticationError("User not found.")
        user = self.users[username]
        if not user.verify_password(password):
            raise AuthenticationError("Incorrect password.")
        return user

# Product Management
class Product:
    def __init__(self, product_id: int, name: str, category: str, price: float, stock_quantity: int):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

class ProductManager:
    def __init__(self):
        self.products = self.load_inventory()

    def load_inventory(self) -> List[Product]:
        try:
            with open(INVENTORY_FILE, "r") as f:
                data = json.load(f)
            return [
                Product(
                    product["product_id"],
                    product["name"],
                    product["category"],
                    product["price"],
                    product["stock_quantity"],
                )
                for product in data
            ]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_inventory(self):
        with open(INVENTORY_FILE, "w") as f:
            json.dump(
                [
                    {
                        "product_id": product.product_id,
                        "name": product.name,
                        "category": product.category,
                        "price": product.price,
                        "stock_quantity": product.stock_quantity,
                    }
                    for product in self.products
                ],
                f,
            )

    def add_product(self, product: Product):
        if any(p.product_id == product.product_id for p in self.products):
            raise ValueError("Product with this ID already exists.")
        self.products.append(product)
        self.save_inventory()

    def remove_product(self, product_id: int):
        self.products = [p for p in self.products if p.product_id != product_id]
        self.save_inventory()

    def get_products(self) -> List[Product]:
        return self.products

    def adjust_stock(self, product_id: int, quantity: int):
        for product in self.products:
            if product.product_id == product_id:
                if product.stock_quantity + quantity < 0:
                    raise InsufficientStockError("Cannot reduce stock below zero.")
                product.stock_quantity += quantity
                self.save_inventory()
                return
        raise ProductNotFoundError("Product not found.")

# Usage Example
if __name__ == "__main__":
    auth_manager = AuthenticationManager()
    product_manager = ProductManager()

    # Add default admin user if not already present
    if "admin" not in auth_manager.users:
        auth_manager.register_user("admin", "adminpass", Role.ADMIN)
        print("Default admin user added.")
    else:
        print("Admin user already exists.")

    # Add default admin user
    try:
        auth_manager.register_user("admin", "adminpass", Role.ADMIN)
        print("Default admin user added.")
    except ValueError:
        print("Admin user already exists.")
