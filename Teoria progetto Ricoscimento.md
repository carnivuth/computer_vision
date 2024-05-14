Il progetto chiede di riconoscere delle scatole di cereali poste su degli scaffali, vengono fornite le immagini di scena degli scaffali e il dataset con le immagini delle varie scatole di cereali da riconoscere nelle immagini di scena.

Il primo punto del problema si pone come obbiettivo il semplice rilevamento delle immagini nella scena.

Lo implementiamo intanto caricando le immagini di test e applicando l'argoritmo SIFT (Scale Invariant Feature Transform) per estrarre i 'punti salienti' dalle immagini, (ovvero caratteristiche chiave di una immagine, invarianti rispetto la scala, rotazione, traslazione, cambi di luce o deformazioni).
SIFT usa una piramide gaussiana per individuare e descrivere le caratteristiche a  diverse scale dell'immagine, che ci consente di rilevare e abbinare le caratteristiche anche se gli oggetti sono di dimensioni diverse, poi calcola l'orientazione locale delle caratteristiche, descrivendole in modo invariante rispetto rotazioni. Inoltre le caratteristiche SIFT sono descritte usando un vettore numerico dettagliato che codifica info sulla forma locale la distribuzione di intensità e l'orientazione delle caratteristiche. Questi descrittori sono robusti ai cambiamenti di illuminazione e alle deformazioni geometriche. Il processo rileva punti chiave nell'immagine con estremi di scala e localizzazione tramite la piramide gaussiana. Le caratteristiche vengono descritte con le direzioni  dei gradienti intorno ai punti chiave. 

poi usiamo il KnnMatch per trovare i match tra le immagini di scena e quelle di test

il knnMatch è una funzione usata per effettuare ricerca di vicinato tra le caratteristiche estratte da due diverse immagini, per determinare corrispondenze tra keypoints estratti dalle immagini.

Il concetto è trovare k punti più vicini (simili) di ciascuna caratteristica di una lista rispetto un'altra lista di caratteristiche. Il metodo è utileper stabilire corrispondenze tra le caratteristiche estrate da due diverse immagini.

sintassi: matches= bf.knnMatch(descriptor1, descr2, k=2)
dove descr1= descrittori delle caratteristiche estratte dall'immagine 1
descr2= descrittori delle caratteriscvhe estratte dall'immagine 2
k numero vicini più prossimi da cercare.

l'output è una lista di corrispondenze tra le caratteristiche delle due immagini, per ogni caratteristica nell'insieme descr1 vengono restituiti k punti più simili in descr2 insieme al relativo valore di distanza.

ogni elemento in matches è una lista lungha k dove ciascun elemento è un oggetto DMatch che contiene info di: 
- DMatch.queryIdx: indice della caratteristica nell'insieme descr1
- DMatch.trainIdx: indice del vicino più prossimo nell'insieme descr2
- DMatch.distance: distanza tra la caratteristica e il suo più vicino 