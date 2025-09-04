# UI Automation Framework - Selenium Python

This project automates the test cases for [Automation Practice Website](https://practice.automationtesting.in/).

## 📂 Features Covered
1. **Cart Functionality**
   - Add and remove products from cart
   - Verify product count and total
   - Negative case: Checkout with empty cart

2. **User Registration & Login**
   - New user registration
   - Existing user login
   - Negative cases: duplicate email, wrong password

3. **Address Management**
   - Add/Edit billing & shipping addresses
   - Verify saved addresses
   - Negative cases: missing/invalid details

## 🧪 Categories
- **Positive Flows**: Successful cart, registration, login, and address actions
- **Negative Flows**: Invalid inputs, duplicate users, and validation errors

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/rshakya99/Automation-framework.git
   cd Automation-framewor
2. Create a virtual environment:
   python3 -m venv venv

3. Activate the virtual environment:
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows

4. Install dependencies:
   pip install -r requirements.txt

5. Run all tests with Allure reports:
   pytest --alluredir=reports/allure-results

6. Generate & view the Allure report:
   allure serve reports/allure-results






   
  
   



