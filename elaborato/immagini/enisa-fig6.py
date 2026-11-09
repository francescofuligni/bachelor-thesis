import matplotlib.pyplot as plt
import numpy as np

# Dati d'esempio (sostituisci con i valori reali del grafico ENISA)
categorie = ["Ransomware", "Malware", "Social Engineering", "Data-related threats",
             "DDoS", "Information Manipulation", "Supply Chain Attacks"]
anni = ["2021", "2022", "2023", "2024"]

# Matrice valori: righe categorie, colonne anni
dati = np.array([
    [18, 20, 22, 25],   # Ransomware
    [15, 16, 14, 13],   # Malware
    [10, 12, 13, 15],   # Social Engineering
    [8, 9, 11, 12],     # Data-related threats
    [12, 14, 16, 18],   # DDoS
    [5, 6, 7, 8],       # Information Manipulation
    [7, 8, 9, 9]        # Supply Chain Attacks
])

# Colori coerenti con ENISA
colori = [
    "#1f77b4",  # blu ransomware
    "#ff7f0e",  # arancio malware
    "#2ca02c",  # verde social engineering
    "#d62728",  # rosso data-related
    "#9467bd",  # viola DDoS
    "#8c564b",  # marrone info manipulation
    "#17becf"   # azzurro supply chain
]

x = np.arange(len(anni))
bar_width = 0.6

# Creazione stacked bar
fig, ax = plt.subplots(figsize=(10, 6))

bottom = np.zeros(len(anni))
for i, (cat, color) in enumerate(zip(categorie, colori)):
    ax.bar(x, dati[i], bar_width, label=cat, color=color, bottom=bottom)
    bottom += dati[i]

# Personalizzazioni
ax.set_xticks(x)
ax.set_xticklabels(anni)
ax.set_ylabel("Percentuale (%)")
ax.set_title("Evoluzione delle minacce principali (ENISA ETL)")
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()

# Salvataggio
plt.savefig("enisa-fig6.png", dpi=300)
plt.close(fig)