# bug_test_2.py

def calculate_total(items):
    total = 0
    for item in items:
        # Calls a function that doesn't exist anywhere in this repo
        price = get_discounted_price(item)
        total += price
    return total

def divide_evenly(amount, people):
    # No check for people == 0 — will crash on real input
    return amount / people

def build_query(table_name, user_input):
    # Unparameterized string built into a query — injection risk
    return f"SELECT * FROM {table_name} WHERE name = '{user_input}'"
