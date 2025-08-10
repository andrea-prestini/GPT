import numpy as np
import matplotlib.pyplot as plt


def get_input_float(prompt):
    """Funzione per richiedere un input numerico gestendo errori."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Errore: Inserisci un valore numerico valido.")


# --- Input Dinamico ---
print(
    "Inserisci i parametri per la funzione di profitto P(Q) = prezzo_unitario * Q - costo_quadratico * Q^2"
)
prezzo_unitario = get_input_float("Inserisci il prezzo unitario: ")
costo_quadratico = get_input_float("Inserisci il coefficiente di costo quadratico: ")
Q_max = get_input_float("Inserisci la capacità massima (Q_max): ")


# Funzione profitto
def profitto(Q, prezzo_unitario, costo_quadratico):
    return prezzo_unitario * Q - costo_quadratico * Q**2


# Quantità senza vincoli: derivata prima = 0 (prezzo_unitario - 2*costo_quadratico*Q = 0)
if costo_quadratico == 0:
    Q_opt_no_vincolo = float("inf") if prezzo_unitario > 0 else 0
else:
    Q_opt_no_vincolo = prezzo_unitario / (2 * costo_quadratico)

# Applichiamo il vincolo Q <= Q_max
Q_opt = min(Q_opt_no_vincolo, Q_max)

# Calcolo profitto ottimale
profitto_opt = profitto(Q_opt, prezzo_unitario, costo_quadratico)

# Output testuale
print("--- Risultati ---")
print(f"Quantità ottimale: {Q_opt:.2f} unità")
print(f"Profitto massimo: {profitto_opt:.2f} €")

# Analisi di sensibilità
if Q_max < Q_opt_no_vincolo:
    print(
        f"⚠ Il vincolo di capacità ({Q_max}) è attivo e riduce il potenziale profitto."
    )

# Grafico
Q_range = np.linspace(0, Q_max, 400)
plt.plot(
    Q_range,
    profitto(Q_range, prezzo_unitario, costo_quadratico),
    label=f"Profitto (P(Q) = {prezzo_unitario}Q - {costo_quadratico}Q^2)",
)
plt.axvline(Q_opt, color="red", linestyle="--", label=f"Q ottimale = {Q_opt:.2f}")
plt.axhline(
    profitto_opt,
    color="green",
    linestyle="--",
    label=f"Profitto max = {profitto_opt:.2f}€",
)
plt.xlabel("Quantità (Q)")
plt.ylabel("Profitto (€)")
plt.title("Massimizzazione del profitto con vincolo di capacità")
plt.legend()
plt.grid(True)

# --- Tabella Punti Vicini ---
punti_tabella = []

# Aggiungi il punto ottimale
punti_tabella.append((Q_opt, profitto_opt))

# Punto al di sotto (intero)
Q_sotto = np.floor(Q_opt)
if Q_sotto < Q_opt and Q_sotto >= 0:
    punti_tabella.append(
        (Q_sotto, profitto(Q_sotto, prezzo_unitario, costo_quadratico))
    )

# Punto al di sopra (intero)
Q_sopra = np.ceil(Q_opt)
if Q_sopra > Q_opt and Q_sopra <= Q_max:
    punti_tabella.append(
        (Q_sopra, profitto(Q_sopra, prezzo_unitario, costo_quadratico))
    )

# Ordina i punti per quantità
punti_tabella.sort(key=lambda x: x[0])

# Stampa la tabella sotto il grafico come testo
fig = plt.gcf()
table_text = f"""--- Analisi Punti Vicini ---
{"Quantità (Q)":<20} | {"Profitto (€)":<20}
-------------------------------------------
{"\n".join([f"{q:<20.2f} | {p:<20.2f}" for q, p in punti_tabella])}"""
fig.text(
    0.5,
    -0.1,
    table_text,
    ha="center",
    va="top",
    fontsize=10,
    wrap=True,
    family="monospace",
)

plt.subplots_adjust(bottom=0.3)
plt.show()

