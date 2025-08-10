# lambda.py: Esempi creativi di funzioni lambda in Python
import time

print("--- 1. Lambda come Funzioni Anonime Semplici ---")
# Le lambda sono funzioni anonime definite con la parola chiave `lambda`.
# Sintassi: lambda argomenti: espressione
saluto = lambda nome: f"Ciao, {nome}!"
print(f"Risultato: {saluto('Mondo')}")
print(
    "Spiegazione: Una semplice lambda che prende un argomento e restituisce una stringa formattata.\n"
)
time.sleep(5)

print("--- 2. Utilizzo con Funzioni di Ordine Superiore (map, filter) ---")
numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# `map` applica una lambda a ogni elemento di una lista.
quadrati = list(map(lambda x: x**2, numeri))
print(f"Numeri al quadrato (con map): {quadrati}")
time.sleep(5)

# `filter` crea una lista di elementi per i quali la lambda restituisce True.
pari = list(filter(lambda x: x % 2 == 0, numeri))
print(f"Numeri pari (con filter): {pari}")
print(
    "Spiegazione: `map` e `filter` sono usi classici, ma fondamentali per capire la potenza delle lambda.\n"
)
time.sleep(5)

print("--- 3. Ordinamento di Strutture Dati Complesse ---")
studenti = [
    {"nome": "Alice", "voto": 85},
    {"nome": "Bob", "voto": 92},
    {"nome": "Charlie", "voto": 78},
]
# Ordina la lista di dizionari in base al valore della chiave 'voto'.
studenti_ordinati = sorted(
    studenti, key=lambda studente: studente["voto"], reverse=True
)
print(f"Studenti ordinati per voto (decrescente): {studenti_ordinati}")
print(
    "Spiegazione: `key` accetta una funzione. Una lambda è perfetta per fornire una logica di ordinamento al volo.\n"
)
time.sleep(5)

print("--- 4. IIFE (Immediately Invoked Function Expression) ---")
# Una lambda che viene definita e chiamata immediatamente.
risultato_immediato = (lambda x, y: x * y)(5, 10)
print(f"Risultato di una IIFE: {risultato_immediato}")
print(
    "Spiegazione: Utile per calcoli veloci e monouso senza inquinare il namespace con un nome di funzione.\n"
)
time.sleep(5)

print("--- 5. Lambda con Logica Condizionale ---")
# Le lambda possono contenere un'espressione ternaria (if-else).
controllo_eta = lambda eta: "Maggiorenne" if eta >= 18 else "Minorenne"
print(f"Una persona di 25 anni è: {controllo_eta(25)}")
print(f"Una persona di 15 anni è: {controllo_eta(15)}")
print(
    "Spiegazione: Permette di incapsulare una semplice logica if-else in una singola riga.\n"
)
time.sleep(5)

print("--- 6. Function Factory: Funzioni che Restituiscono Lambda ---")


# Una funzione che, a seconda dell'input, restituisce una lambda configurata.
def crea_moltiplicatore(n):
    """Restituisce una funzione lambda che moltiplica per n."""
    return lambda x: x * n


moltiplica_per_3 = crea_moltiplicatore(3)
moltiplica_per_10 = crea_moltiplicatore(10)

print(f"3 moltiplicato per 5 fa: {moltiplica_per_3(5)}")
print(f"10 moltiplicato per 7 fa: {moltiplica_per_10(7)}")
print(
    "Spiegazione: Le lambda catturano il valore di 'n' dal loro ambiente di definizione (closure), creando funzioni specializzate.\n"
)
time.sleep(5)

print("--- 7. Lambda come Valori in un Dizionario (Dispatcher) ---")
# Usa un dizionario per mappare operazioni a delle lambda.
operazioni = {
    "somma": lambda x, y: x + y,
    "sottrai": lambda x, y: x - y,
    "moltiplica": lambda x, y: x * y,
    "dividi": lambda x, y: x / y if y != 0 else "Errore: divisione per zero",
}

a, b = 10, 5
print(f"10 + 5 = {operazioni['somma'](a, b)}")
print(f"10 * 5 = {operazioni['moltiplica'](a, b)}")
print(f"10 / 0 = {operazioni['dividi'](10, 0)}")
print(
    "Spiegazione: Un modo elegante per implementare un dispatcher o un costrutto 'switch' che non esiste nativamente in Python.\n"
)
time.sleep(5)

print("--- 8. Lambda in UI Frameworks (esempio concettuale) ---")
# In librerie come Tkinter o in framework web, le lambda sono usate per i callback.
# Esempio concettuale (non eseguibile senza una GUI):
#
# import tkinter as tk
#
# root = tk.Tk()
# button = tk.Button(root, text="Cliccami!",
#                    command=lambda: print("Pulsante cliccato!"))
# button.pack()
# # root.mainloop()
#
print(
    "Spiegazione: Le lambda sono perfette per creare piccole funzioni di callback che catturano lo stato necessario dal contesto in cui sono definite, senza bisogno di definire una funzione separata e completa.\n"
)
time.sleep(5)
