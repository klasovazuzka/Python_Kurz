import csv

with open('penguins.csv', mode='r', encoding='utf-8') as file:
    reader = list(csv.reader(file))
    header = reader[0]  # Záhlaví (názvy sloupců)
    rows = reader[1:]   # Samotná data

    print(f"1. Počet řádků (bez hlavičky): {len(rows)}")
    print(f"2. Počet sloupců: {len(header)}")
    print("-" * 30)
    print("3. Prvních 10 řádků (pro kontrolu):")
    for row in rows[:10]:
        print(row)