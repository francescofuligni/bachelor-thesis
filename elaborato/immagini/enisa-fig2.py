# Grafico "Principali minacce" (donut) – stile ENISA
# Requisiti: solo matplotlib, un unico plot, palette colori come nell'immagine originale.

import matplotlib.pyplot as plt
import numpy as np

# Dati (in migliaia) e percentuali
threats = [
    "DoS/DDoS/RDoS", "Ransomware", "Data breach", "Social Engineering",
    "Malware", "Supply Chain Attack", "Web Threats", "FIMI", "Zero Day"
]
values_k = [4.12, 2.59, 1.91, 0.61, 0.52, 0.17, 0.09, 0.05, 0.03]  # K
perc     = [41.1, 25.8, 19.0,  6.1,  5.2,  1.7,  0.9,  0.5,  0.3]   # %

# Palette coerente con l’immagine inviata
colors = [
    "#005BBB",  # DoS/DDoS/RDoS - blu
    "#E41A1C",  # Ransomware - rosso
    "#1C1C1C",  # Data breach - nero
    "#FF9900",  # Social Engineering - arancione
    "#56B4E9",  # Malware - azzurro
    "#984EA3",  # Supply Chain Attack - viola
    "#4DAF4A",  # Web Threats - verde
    "#A65628",  # FIMI - marrone
    "#999999"   # Zero Day - grigio
]

fig, ax = plt.subplots(figsize=(10, 7))

# Donut (ciambella)
wedges, texts = ax.pie(
    values_k,
    labels=None,                # nessuna label interna
    startangle=90,
    colors=colors,
    pctdistance=0.85,
    wedgeprops={"width": 0.30, "edgecolor": "white"}
)

# Etichette esterne: SOLO per percentuali >= 1%
for w, v, p in zip(wedges, values_k, perc):
    if p >= 1.0:
        ang = (w.theta2 - w.theta1) / 2.0 + w.theta1
        x, y = np.cos(np.deg2rad(ang)), np.sin(np.deg2rad(ang))
        ax.text(
            1.16 * x, 1.16 * y,
            f"{v:.2f}K ({p:.1f}%)",
            ha="center", va="center",
            fontsize=9, fontweight="bold"
        )

# Titolo (italiano) e legenda a lato
ax.set_title("Principali minacce", fontsize=16, fontweight="bold")
ax.legend(wedges, threats, title="Categorie",
          loc="center left", bbox_to_anchor=(1, 0, 0.3, 1))

plt.tight_layout()

# Salva su file
plt.savefig("enisa-fig2.png", dpi=300)
plt.close(fig)