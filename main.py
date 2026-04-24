from models import Transaction
from manager import BudgetManager
from storage import Storage
from utils import ascii_bar_chart, export_excel

def main():
    manager = BudgetManager()
    storage = Storage()

    manager.transactions = storage.load_json()

    while True:
        print("\n--- Budget Manager ---")
        print("1. Ajouter transaction")
        print("2. Voir solde")
        print("3. Historique")
        print("4. Stats catégories")
        print("5. Export CSV")
        print("6. Export Excel")
        print("7. Sauvegarder")
        print("0. Quitter")

        choice = input("> ")

        if choice == "1":
            amount = float(input("Montant: "))
            category = input("Catégorie: ")
            t_type = input("Type (income/expense): ")
            tags = input("Tags (séparés par virgule): ").split(",")

            t = Transaction(amount, category, t_type, tags)
            manager.add_transaction(t)

        elif choice == "2":
            print(f"Solde: {manager.get_balance()}")

        elif choice == "3":
            for t in manager.transactions:
                print(t.to_dict())

        elif choice == "4":
            stats = manager.stats_by_category()
            ascii_bar_chart(stats)

        elif choice == "5":
            storage.export_csv(manager.transactions)
            print("Export CSV OK")

        elif choice == "6":
            export_excel(manager.transactions)
            print("Export Excel OK")

        elif choice == "7":
            storage.save_json(manager.transactions)
            print("Sauvegardé")

        elif choice == "0":
            break


if __name__ == "__main__":
    main()