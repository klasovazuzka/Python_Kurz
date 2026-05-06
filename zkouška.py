import pandas as pd

# Načtení souboru (ujisti se, že je ve stejné složce)
df = pd.read_csv('penquins.csv')

# Ukáže prvních pár řádků
print("--- DATA ZE SOUBORU ---")
print(df.head())

# Ukáže základní statistiku (pokud jsou tam čísla)
print("\n--- STATISTIKA ---")
print(df.describe())
df = pd.read_csv(r'C:\Users\Kristynka\Downloads\penguins.csv')