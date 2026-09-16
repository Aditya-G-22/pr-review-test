# test_bug.py

import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # SQL injection: user_id is interpolated directly into the query
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()

def calculate_discount(price, discount_percent):
    # Calls a function that doesn't exist anywhere in this repo
    validated_price = validate_price_range(price)
    return validated_price - (validated_price * discount_percent / 100)

API_KEY = "sk_live_51H8xJ2eZvKYlo2CTGhIjklmnop3456789ABC"

def process_payment(amount):
    return {"status": "success", "amount": amount, "key": API_KEY}
