import json
import random
from datetime import datetime, timedelta
from uuid import uuid4

def generate_transaction():
    transaction_types = ["debit", "credit"]
    descriptions = [
        "ATM Withdrawal",
        "Salary Deposit",
        "POS Payment",
        "Online Transfer",
        "Bill Payment",
        "Cash Deposit"
    ]

    return {
        "transaction_id": f"T{random.randint(100000, 999999)}",
        "account_id": f"A{random.randint(10000, 99999)}",
        "transaction_date": datetime.now().strftime("%Y-%m-%d"),
        "amount": round(random.uniform(10.0, 5000.0), 2),
        "transaction_type": random.choice(transaction_types),
        "branch_id": f"B{random.randint(1, 5)}",
        "description": random.choice(descriptions)
    }

def generate_transactions_file(num_records=20, filename=None):
    data = [generate_transaction() for _ in range(num_records)]

    # add a duplicate row
    if len(data) > 2:
        data.append(data[2])

    # add a few bad rows for testing
    data.append({
        "transaction_id": None,
        "account_id": "A99999",
        "transaction_date": datetime.now().strftime("%Y-%m-%d"),
        "amount": 100.0,
        "transaction_type": "credit",
        "branch_id": "B1",
        "description": "Bad Row Null ID"
    })

    data.append({
        "transaction_id": f"T{random.randint(100000, 999999)}",
        "account_id": "A88888",
        "transaction_date": None,
        "amount": 150.0,
        "transaction_type": "debit",
        "branch_id": "B2",
        "description": "Bad Row Null Date"
    })

    data.append({
        "transaction_id": f"T{random.randint(100000, 999999)}",
        "account_id": "A77777",
        "transaction_date": datetime.now().strftime("%Y-%m-%d"),
        "amount": None,
        "transaction_type": "debit",
        "branch_id": "B3",
        "description": "Bad Row Null Amount"
    })

    if not filename:
        filename = f"transactions_{datetime.now().strftime('%Y-%m-%d')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Created file: {filename}")

if __name__ == "__main__":
    generate_transactions_file()
