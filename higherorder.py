# 1. Add Country Code to Phone Numbers
phones = ["9876543210", "9123456780", "9988776655"]
phones_with_code = list(map(lambda x: "+91-" + x, phones))
print(phones_with_code)

# 2. Convert Prices from Dollars to Rupees
prices_usd = [10, 25, 40, 100]
prices_inr = list(map(lambda x: x * 83, prices_usd))
print(prices_inr)

# 3. Filter Gmail IDs
emails = ["harish@gmail.com", "abc@yahoo.com", "xyz@gmail.com"]
gmail_ids = list(filter(lambda x: x.endswith("@gmail.com"), emails))
print(gmail_ids)

# 4. Get Short Product Names
products = ["Pen", "Notebook", "Laptop", "Charger", "Bag"]
short_products = list(filter(lambda x: len(x) <= 5, products))
print(short_products)

# 5. Convert Names to Usernames
names = ["Harish", "Sushma", "Nandu"]
usernames = list(map(lambda x: x.lower() + "@gmail.com", names))
print(usernames)

# 6. Filter Expired Products
years = [2022, 2023, 2025, 2026]
expired = list(filter(lambda x: x < 2025, years))
print(expired)

# 7. Mask Credit Card Numbers
cards = ["1234567890123456", "9876543210987654"]
masked = list(map(lambda x: "*"*12 + x[-4:], cards))
print(masked)

# 8. Filter High Salary Employees
salaries = [25000, 45000, 60000, 15000, 80000]
high_salary = list(filter(lambda x: x >= 40000, salaries))
print(high_salary)

# 9. Format Product Labels
labels = ["apple", "mango", "orange"]
formatted = list(map(lambda x: f"Product: {x}", labels))
print(formatted)

# 10. Students Passed
marks = [35, 80, 55, 20, 90]
passed = list(filter(lambda x: x >= 40, marks))
print(passed)

# 11. Filter Strong Passwords
passwords = ["abc123", "Admin@123", "hello", "Pa$$word"]
strong = list(filter(lambda x: len(x) >= 8 and ("@" in x or "$" in x), passwords))
print(strong)

# 12. Process Transaction Records
transactions = ["1000-CREDIT", "500-DEBIT", "1200-CREDIT", "200-DEBIT"]

# Extract amounts
amounts = list(map(lambda x: int(x.split("-")[0]), transactions))
print(amounts)

# Separate credits and debits
credits = list(filter(lambda x: "CREDIT" in x, transactions))
debits = list(filter(lambda x: "DEBIT" in x, transactions))
print("Credits:", credits)
print("Debits:", debits)
