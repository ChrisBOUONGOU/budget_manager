import json
import csv
from models import Transaction

class Storage:
    def __init__(self, filename="data.json"):
        self.filename = filename

    def save_json(self, transactions):
        with open(self.filename, "w") as f:
            json.dump([t.to_dict() for t in transactions], f, indent=4)

    def load_json(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [Transaction.from_dict(d) for d in data]
        except FileNotFoundError:
            return []

    def export_csv(self, transactions, filename="export.csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["amount", "category", "type", "tags", "date"])
            writer.writeheader()
            for t in transactions:
                writer.writerow(t.to_dict())