# Generazione di Permutazioni, Disposizioni e Combinazioni

Questo progetto fornisce diverse funzioni per generare permutazioni, disposizioni e combinazioni da un insieme di elementi, con o senza ripetizioni, utilizzando una matrice di input. Le funzioni supportano vari tipi di operazioni combinatorie, e sono utili per applicazioni di teoria combinatoria, algoritmi, o altre applicazioni matematiche.

## Funzionalità

### 1. **Funzioni per Permutazioni, Disposizioni e Combinazioni**

- **Permutazioni senza ripetizioni (`permutazioni`)**: Restituisce le permutazioni senza ripetizioni di una matrice di input.
- **Permutazioni con ripetizioni (`permutazioniripetizione`)**: Restituisce le permutazioni con ripetizioni, eliminando eventuali duplicati.
- **Disposizioni senza ripetizioni (`disposizioni`)**: Restituisce le disposizioni senza ripetizioni, considerando solo i primi `k` elementi.
- **Disposizioni con ripetizioni (`disposizioniripetizione`)**: Restituisce tutte le disposizioni con ripetizioni.
- **Combinazioni senza ripetizioni (`combinazionisenzaripetizioni`)**: Restituisce le combinazioni senza ripetizioni per i primi `k` elementi.
- **Combinazioni con ripetizioni (`combinazioniripetizioni`)**: Restituisce tutte le combinazioni con ripetizioni.

### 2. **Generazione della Matrice di Permutazioni e Combinazioni**

Il codice costruisce una matrice contenente tutte le possibili permutazioni, disposizioni o combinazioni di un insieme dato. La matrice è costruita tramite un ciclo che distribuisce gli elementi in modo da formare tutte le combinazioni o permutazioni richieste.

## Funzioni Principali

### `permutazioni(Matrix, A)`
Genera le permutazioni senza ripetizioni di una matrice di input.

**Parametri**:
- `Matrix`: Una matrice di elementi da cui generare le permutazioni.
- `A`: L'insieme da cui generare le permutazioni.

**Descrizione**:
- Restituisce una lista di permutazioni uniche, escludendo quelle con ripetizioni.

**Restituisce**:
- Una lista di permutazioni uniche.

### `permutazioniripetizione(Matrix, A)`
Genera le permutazioni con ripetizioni, eliminando eventuali duplicati.

**Parametri**:
- `Matrix`: Una matrice di elementi da cui generare le permutazioni.
- `A`: L'insieme da cui generare le permutazioni.

**Descrizione**:
- Restituisce una lista di permutazioni con ripetizioni, escludendo quelle duplicate.

**Restituisce**:
- Una lista di permutazioni uniche con ripetizioni.

### `disposizioni(Matrix, A, k)`
Genera disposizioni senza ripetizioni considerando solo i primi `k` elementi.

**Parametri**:
- `Matrix`: La matrice da cui estrarre le disposizioni.
- `A`: L'insieme da cui generare le disposizioni.
- `k`: Il numero di elementi da considerare per le disposizioni.

**Descrizione**:
- Restituisce una lista di disposizioni senza ripetizioni.

**Restituisce**:
- Una lista di disposizioni senza ripetizioni.

### `disposizioniripetizione(Matrix)`
Genera disposizioni con ripetizioni.

**Parametri**:
- `Matrix`: La matrice di input.

**Descrizione**:
- Restituisce tutte le disposizioni con ripetizioni.

**Restituisce**:
- Una lista di disposizioni con ripetizioni.

### `combinazionisenzaripetizioni(Matrix, A, k)`
Genera combinazioni senza ripetizioni considerando solo i primi `k` elementi.

**Parametri**:
- `Matrix`: La matrice da cui estrarre le combinazioni.
- `A`: L'insieme da cui generare le combinazioni.
- `k`: Il numero di elementi da considerare per le combinazioni.

**Descrizione**:
- Restituisce una lista di combinazioni senza ripetizioni, escludendo quelle duplicate.

**Restituisce**:
- Una lista di combinazioni senza ripetizioni.

### `combinazioniripetizioni(Matrix, A, k)`
Genera combinazioni con ripetizioni.

**Parametri**:
- `Matrix`: La matrice da cui estrarre le combinazioni.
- `A`: L'insieme da cui generare le combinazioni.
- `k`: Il numero di elementi da considerare per le combinazioni.

**Descrizione**:
- Restituisce una lista di combinazioni con ripetizioni.

**Restituisce**:
- Una lista di combinazioni con ripetizioni.

## Esempio di utilizzo

```python
A = ['a', 'b', 'c']

matrice = []
length = len(A)

esponente = 1
inizio = 0

Matrix = []

matrice = [[] for n in range(length)]

while inizio != length:
    for x in A:
        for j in range(0, length**(length - esponente)):
            matrice[inizio].append(x)
    if inizio >= 1:
        while len(matrice[0]) != len(matrice[inizio]):
            for x in A:
                for j in range(0, length**(length - esponente)):
                    matrice[inizio].append(x)
                    if len(matrice[inizio]) == len(matrice[0]):
                        break
                if len(matrice[inizio]) == len(matrice[0]):
                    break
    inizio += 1
    esponente += 1

for col in range(len(matrice[0])):
    listina = []
    for row in range(len(matrice)):
        listina.append(matrice[row][col])
    Matrix.append(listina)

# Esempio di combinazioni senza ripetizioni
print(combinazionisenzaripetizioni(Matrix, A, 2))

# Esempio di combinazioni con ripetizioni
print(combinazioniripetizioni(Matrix, A, 2))
