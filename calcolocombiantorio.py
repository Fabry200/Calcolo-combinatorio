
def permutazioni(Matrix,A):
  permnorep=[]

  for x in range(len(Matrix)):
    if len(set(Matrix[x]))==len(A):
      permnorep.append(Matrix[x])
  return permnorep

def permutazioniripetizione(Matrix,A):
  perm=[]

  for x in range(len(Matrix)):
    if sorted(Matrix[x]) == sorted(A):
      perm.append(Matrix[x])
  permrip=[]
  for x in perm:
    if x not in permrip:
      permrip.append(x)
  return permrip

def disposizioni(Matrix,A,k):
  disp=[]

  for x in range(len(Matrix)):
    disp.append(Matrix[x][0:k])

  disp2=[]
  for x in disp:
    if x not in disp2:
      disp2.append(x)

  return disp2
def disposizioniripetizione(Matrix):
  return Matrix
def combinazionisenzaripetizioni(Matrix,A,k):
  comb=[]
  for x in range(len(Matrix)):
    if len(set(Matrix[x][0:k])) == k :
      comb.append(Matrix[x][0:k])
  combinazioni=[]
#con questo ciclo elimino gli elementi duplicati. Anche facendo il sorted di x elimino quelli che sono uguali ma scritti al contrario
  for x in comb:
    if x not in combinazioni and sorted(x) not in combinazioni:
      combinazioni.append(x)
  return combinazioni

def combinazioniripetizioni(Matrix, A,k):
  comb=[]
  for x in range(len(Matrix)):
    #prendo paro paro il codice dlele combinazioni senza ripetizioni e ci tolgo questa condizione (if len(set(Matrix[x][0:k])) == k) che mi condannava ad usare solo gli elementi in cui non vi erano duplicati
    comb.append(Matrix[x][0:k])

  combinazioni=[]
  for x in comb:
    if x not in combinazioni and sorted(x) not in combinazioni:
      combinazioni.append(x)

  return combinazioni



A=['a',"b", "c"]

matrice=[]
length=len(A)

esponente=1
inizio=0

Matrix=[]

matrice=[[] for n in range(length)]

""""
La mia variabile di controllo e'
inizio che si riferisce alla riga della matrice colonna in cui devo posizionare i valori.
la prima parte di questo ciclo crea delle colonne ma non le crea tutte complete ma solo la prima.
se prendessimo solo la prima parte avremmo per un insieme di tre elementi qualcosa del tipo  [a,a,b,b] [a,b,a,b]
"""
while inizio != length:
  for x in A:
    for j in range(0,length**(length-esponente)):
      matrice[inizio].append(x)
  if inizio >= 1:
    while len(matrice[0]) != len(matrice[inizio]):
      for x in A:
        for j in range(0,length**(length-esponente)):
          matrice[inizio].append(x)
          if len(matrice[inizio]) == len(matrice[0]):
            break
        if len(matrice[inizio]) == len(matrice[0]):
            break
  inizio+=1
  esponente+=1


for col in range(len(matrice[0])):
    listina=[]
    for row in range(len(matrice)):
        listina.append(matrice[row][col])
    Matrix.append(listina)
"""
quindi, so che la prima volta che si avvia questo ciclo iterativo, ho esattamente il numero di elementi esatto
affinche' si possa costruire una matrice n per n. e nonostante il pattern seguente sia quello giusto [a,b], bisogna
estendere quel pattern affinche' sia associato a tutti gli elementi della matrice di riga[0]
"""

#combinazioniripetizioni(Matrix,A,2)
#combinazionisenzaripetizioni(Matrix,A,2)