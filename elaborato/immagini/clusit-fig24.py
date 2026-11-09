import matplotlib.pyplot as plt

# Dati del grafico
anni = ["2020", "2021", "2022", "2023", "2024"]
italia = [29.7, 45.8, 168.6, 64.9, 15.2]
globali = [12.4, 9.3, 21.5, 11.7, 27.4]

x = range(len(anni))
larghezza = 0.35

# Creazione grafico
plt.figure(figsize=(10,6))
plt.bar([i - larghezza/2 for i in x], italia, width=larghezza, label="Italia", color="#1f5ca8")
plt.bar([i + larghezza/2 for i in x], globali, width=larghezza, label="Global", color="#66b2c2")

# Aggiunta etichette sopra le barre
for i, v in enumerate(italia):
    plt.text(i - larghezza/2, v + 1, f"{v}%", ha="center", fontweight="bold")

for i, v in enumerate(globali):
    plt.text(i + larghezza/2, v + 1, f"{v}%", ha="center", color="dimgray")

# Personalizzazione
plt.xticks(x, anni)
plt.title("Confronto crescita % Italia vs Global", fontsize=14, fontweight="bold")
plt.legend()
plt.tight_layout()

# Salvataggio in PNG
output_path = "clusit-fig24.png"
plt.savefig(output_path, dpi=300)
plt.close()

output_path