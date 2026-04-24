def ascii_bar_chart(data):
    max_value = max(data.values()) if data else 1

    for key, value in data.items():
        bar = "#" * int((value / max_value) * 40)
        print(f"{key:15} | {bar} ({value})")


def export_excel(transactions, filename="budget.xlsx"):
    from openpyxl import Workbook

    wb = Workbook()
    ws = wb.active
    ws.append(["Amount", "Category", "Type", "Tags", "Date"])

    for t in transactions:
        ws.append([
            t.amount,
            t.category,
            t.type,
            ",".join(t.tags),
            t.date.strftime("%Y-%m-%d")
        ])

    wb.save(filename)