# Massimizzazione del Profitto e Esempi di Lambda

Questo repository contiene script Python per calcolare la quantità di produzione ottimale che massimizza il profitto e per mostrare esempi creativi di funzioni lambda.

## `profitto.py`

Questo script calcola la quantità ottimale (`Q_opt`) per massimizzare il profitto (`P(Q)`) basandosi sulla seguente funzione:

P(Q) = prezzo_unitario * Q - costo_quadratico * Q^2

con il vincolo `Q <= Q_max`.

### Funzionalità

1.  **Input Dinamico**: Richiede all'utente di inserire i seguenti parametri:
    *   `prezzo_unitario`: Il prezzo di vendita per unità.
    *   `costo_quadratico`: Il coefficiente del costo quadratico.
    *   `Q_max`: La capacità massima di produzione.

2.  **Calcolo Ottimale**: Calcola la quantità ottimale (`Q_opt`) che massimizza il profitto, tenendo conto del vincolo di capacità.

3.  **Output dei Risultati**: Stampa a schermo la quantità ottimale e il profitto massimo corrispondente.

4.  **Visualizzazione Grafica**:
    *   Genera un grafico della funzione di profitto.
    *   Indica la quantità ottimale e il profitto massimo con linee tratteggiate.
    *   Mostra una tabella con un'analisi dei punti vicini al punto ottimale.

### Come eseguirlo

Per eseguire lo script, è necessario avere Python e le librerie `numpy` e `matplotlib` installate.

```bash
pip install numpy matplotlib
```

Eseguire lo script con il seguente comando:

```bash
python profitto.py
```

Lo script richiederà di inserire i parametri necessari e quindi visualizzerà il grafico con i risultati.

## `lambda.py`

Questo script fornisce una serie di esempi commentati per illustrare la versatilità e la potenza delle funzioni `lambda` in Python.

### Esempi Inclusi

1.  **Funzioni Anonime Semplici**: Uso base di una lambda per una semplice operazione.
2.  **Funzioni di Ordine Superiore**: Utilizzo con `map` e `filter`.
3.  **Ordinamento di Strutture Dati Complesse**: Ordinamento di liste di dizionari.
4.  **IIFE (Immediately Invoked Function Expression)**: Definizione ed esecuzione immediata di una lambda.
5.  **Logica Condizionale**: Utilizzo di espressioni ternarie all'interno di una lambda.
6.  **Function Factory**: Funzioni che restituiscono funzioni lambda (closure).
7.  **Dispatcher**: Utilizzo di lambda come valori in un dizionario per implementare uno switch.
8.  **UI Frameworks**: Esempio concettuale di utilizzo di lambda per callback.

### Come eseguirlo

Per eseguire lo script:

```bash
python lambda.py
```

Lo script stamperà a schermo una spiegazione di ogni esempio, seguita dal risultato.