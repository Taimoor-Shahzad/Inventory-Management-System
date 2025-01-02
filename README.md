# Inventory Management System (IMS)

## **Overview**
The Inventory Management System (IMS) is a console- and Streamlit-based application designed to manage inventory for small businesses. It includes functionalities like adding, editing, and removing products, adjusting stock levels, and maintaining role-based user access (Admin/User). The system ensures easy management of inventory and provides a user-friendly interface for users with minimal technical knowledge.

---

## **Features**

### **Role-Based Access Control**
- **Admin Role**:
  - Add new products to the inventory.
  - Remove existing products.
  - View all products with detailed information.
  - Adjust stock levels.
- **User Role**:
  - View and search products.
  - Filter products by name or category.

### **Product Management**
- Create, read, update, and delete products.
- Real-time stock adjustment.
- Persistent data storage in JSON files (`inventory.json` and `users.json`).

### **Error Handling**
- User-friendly error messages for invalid actions.
- Custom exceptions for authentication and inventory operations.

### **Streamlit Interface**
- Modern, responsive web interface.
- Sidebar navigation for easy access to features.
- Real-time interaction with data.

---

## **Project Structure**

```
Inventory Management System/
├── ims_core.py           # Backend logic for authentication and product management.
├── app.py                # Streamlit-based frontend interface.
├── data/                 # Persistent storage for users and inventory.
│   ├── inventory.json    # JSON file for storing inventory data.
│   ├── users.json        # JSON file for storing user data.
```

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.8 or above
- Streamlit library

### **Installation Steps**
1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd Inventory Management System
   ```
3. Install required dependencies:
   ```bash
   pip install streamlit pandas
   ```
4. Ensure the `data` folder contains the following files:
   - `inventory.json`: Initialize with `[]` (empty list).
   - `users.json`: Initialize with `{}` (empty dictionary).

---

## **How to Run**

### **Running the Application**
1. Navigate to the project directory:
   ```bash
   cd Inventory Management System
   ```
2. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```
3. Open the URL provided by Streamlit (usually `http://localhost:8501`) in your web browser.

### **Default Credentials**
- **Admin Login**:
  - Username: `admin`
  - Password: `adminpass`

---

## **Using the Application**

### **1. Login**
- Enter your username and password on the login screen.
- Based on your role, the respective dashboard (Admin/User) will load.

### **2. Admin Functionalities**
- **Add Product**: Enter product details (ID, name, category, price, stock) and click "Add Product".
- **Remove Product**: Select a product from the dropdown and click "Remove Product".
- **View Products**: Displays all products in a tabular format.
- **Adjust Stock**: Select a product, specify the adjustment (positive or negative), and click "Adjust Stock".

### **3. User Functionalities**
- **View Products**: Displays all available products.
- **Search Products**: Use the search bar to find products by name or category.

### **4. Logout**
- Use the "Logout" button in the sidebar to log out of the system.

---

## **Technical Details**

### **Backend (`ims_core.py`)**
- **AuthenticationManager**: Handles user authentication and registration.
- **ProductManager**: Manages inventory operations (add, remove, adjust stock).
- **Persistent Storage**: Data is stored in `inventory.json` and `users.json`.

### **Frontend (`app.py`)**
- **Streamlit Framework**: Provides a web-based interface for the IMS.
- **Dynamic Role-Based Views**: Loads admin or user dashboards based on login credentials.

### **Error Handling**
- Custom exceptions like `AuthenticationError`, `ProductNotFoundError`, and `InsufficientStockError` ensure smooth operation and clear error messages.

---

## **Future Enhancements**
- Add support for exporting inventory data as CSV/Excel files.
- Implement graphs and charts for stock analysis.
- Add password encryption for enhanced security.
- Multi-language support for a broader user base.