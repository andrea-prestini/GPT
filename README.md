# Massimizzazione del Profitto

Questo repository contiene uno script Python per calcolare la quantità di produzione ottimale che massimizza il profitto.

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