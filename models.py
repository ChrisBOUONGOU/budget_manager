from datetime import datetime

class Transaction:
    def __init__(self, amount, category, t_type, tags=None, date=None):
        self.amount = float(amount)
        self.category = category
        self.type = t_type  # "income" or "expense"
        self.tags = tags if tags else []
        self.date = date if date else datetime.now()

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "type": self.type,
            "tags": self.tags,
            "date": self.date.isoformat()
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            data["amount"],
            data["category"],
            data["type"],
            data["tags"],
            datetime.fromisoformat(data["date"])
        )