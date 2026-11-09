import matplotlib.pyplot as plt
import numpy as np

# Dati percentuali e totali dal Rapporto Clusit
anni = ["2020", "2021", "2022", "2023", "2024"]
percentuali = [2.6, 3.4, 7.6, 11.2, 10.1]
incidenti_global = [1874, 2049, 2489, 2779, 3541]  # valori globali
incidenti_ita = [int(g * p/100) for g, p in zip(incidenti_global, percentuali)]

x = np.arange(len(anni))
w = 0.6

fig, ax = plt.subplots(figsize=(10,6))

# Prima parte: barra azzurra (GLOBAL)
ax.bar(x, incidenti_global, width=w, color="#7fc1de", label="Totale Incidenti GLOBAL")

# Seconda parte: sopra la barra GLOBAL aggiungiamo Italia (blu scuro)
ax.bar(x, incidenti_ita, width=w, bottom=incidenti_global, color="#1f5ca8", label="Totale Incidenti ITALIA")

# Etichette: solo percentuali sopra la parte blu ITA
for i, (g, it, p) in enumerate(zip(incidenti_global, incidenti_ita, percentuali)):
    ax.text(i, g+it+50, f"{p}%", ha="center", va="bottom", fontweight="bold")

# Titolo e assi
ax.set_xticks(x)
ax.set_xticklabels(anni)
ax.set_ylabel("Numero di incidenti")
ax.set_title("Confronto Italia vs. Global 2020-2024", fontsize=14, fontweight="bold")

# Scala asse Y ogni 1000
ax.set_yticks(np.arange(0, 5000, 1000))

# Griglia orizzontale leggera
ax.yaxis.grid(True, linestyle=":", alpha=0.4)
ax.set_axisbelow(True)

# Legenda
ax.legend()

plt.tight_layout()

# Salvataggio
out_path = "clusit-fig25.png"
plt.savefig(out_path, dpi=300)
plt.close(fig)

out_path