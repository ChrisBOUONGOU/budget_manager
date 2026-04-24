from collections import defaultdict
from datetime import datetime

class BudgetManager:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        balance = 0
        for t in self.transactions:
            if t.type == "income":
                balance += t.amount
            else:
                balance -= t.amount
        return balance

    def filter_by_month(self, year, month):
        return [
            t for t in self.transactions
            if t.date.year == year and t.date.month == month
        ]

    def stats_by_category(self):
        stats = defaultdict(float)
        for t in self.transactions:
            if t.type == "expense":
                stats[t.category] += t.amount
        return stats