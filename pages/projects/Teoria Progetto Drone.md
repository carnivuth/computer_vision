---
id: Teoria Progetto Drone
aliases: []
tags: []
---

Il progetto si basa sulla realizzazione di un algoritmo per il riconoscimento della distanza,
Dati due video (robotL e robotR) girati da una stereo camera montata su un veicolo mobile, dobbiamo capire le informazioni riguardanti lo spazio di fronte l'oggetto.

I parametri necessari per misurare la distanza sono dati dal problema ( f e b )

Il progetto implementa la tecnica di stereo matching (che serve ad ottonere una mappa di disparità da coppie di immagini) della libreria OpenCV grazie alla classe stereBM che implementa l'algoritmo di block matching ( principio di base: dividere le immagini in blocchi di pixel e cercare la corrispondenza cercando il blocco più simile nella seconda immagine(tipi di algoritmi che possono essere usati SSD e NCC))
	ovviamente potevano essere usati altri algoritmi, come SGM (semi-global matching(che rappresenta lo stereo come un problema di minimizzazione dell'energia e usa la programmazione dinamica per trovare la disparity map globale)) , Graph Cuts (che modella il problema di corrispondenza stereo come un problema di taglio minimo in un grafo, minimizzando una funzione di energia che tiene conto delle differenze di intensità e coerenza spaziale), o il Matching basato su Caratteristiche (come SIFT o SURF, che estraggono caratteriche basate su descrittori invece di pixel diretti) o ancora deep learning based matching (usa reti neurali profonde per apprendere le corrispondenze stereo da coppie di immagini), ma noi abbiamo deciso che nel nostro caso era più appropriato lo stereoBM

Quello che avviene nel programma è che prendiamo i frames dai video, visionandoli col metodo di OpenCV VideoCapture e li controlliamo, nel caso ci siano problemi (come file corrotti), successivamente dandoli in pasto all'algoritmo calcoliamo la disparity map.

Dopo tagliamo l'immagine in una porzione centrale, per semplificare il calcolo della distanza, e calcoliamo un valore medio per la disparità.

Nel mentre identifichiamo la chessboard nell'immagine e troviamo i punti salienti (gli angoli) della chessboard, facciamo ciò tramite il metodo fornito da OpenCV findChessboardCorners e li disegniamo nell'immagine tramite il metodo drawChessboardCorners

Allora calcoliamo la distanza dalla chessboard in ogni frame, creiamo un allarme che che ci notificherà quando il valore riscontrato sarà inferiore ad un valore soglia da noi deciso.

Infine confrontiamo i parametri della chessboard trovati con quelli reali, forniti dal testo, e stampiamo un grafico delle differenze tra i valori.

La calibrazione stereo è un processo per determinare i parametri intrinseci ed estrinseci delle due fotocamere che compongono un sistema stereo (due fotocamere in posizioni leggermente diverse per catturare una scena tridimensionale).
Processo fondamentale per misurare la distanza tra gli oggetti nella scena con la stereovisione.

Gli obiettivi della stereo calibrazione sono correggere le distorsioni, determinare i parametri intrinseci della fotocamera (lunghezza focale, punto principale e coefficienti di distorsione) e quelli estrinseci (posizione e orientamento delle due fotocamere sono determinati e descrivono la trasformazione geometrica tra i due sistemi di coordinate delle fotocamere).

Come avviene la calibrazione stereo?
I passaggi da implementare comprendono l'acquisizione delle immagini di calibrazione, ovvero immagini di un oggetto noto (spesso una scacchiera) da 2 fotocamere diverse in posizioni e orientamento, successivamente si devono individuare i punti chiave sulla scacchiera (come gli angoli dei quadrati), poi si passa alla stima dei parametri intrinsici usando le immagini di calibrazione e i punti chiave, vengono stimate lunghezza focale, punto principale e coefficienti di distorsione usando algoritmi di calibrazione, inoltre si calcolano i parametri estrinseci unendo i punti chiave rilevati e i parametri intrinseci, stimiamo posizione e orientamento relative. Infine si valuta la precisione misurando l'errore di riproiezione (discrepanza tra punti stimati e punti osservati sulle immagini)

Un metodo per la calibrazione della fotocamera è il metodo di Zhang, che si basa sull'uso di una ampia serie di immagini di un oggetto noto catturato da diverse angolazioni.

I passagi sono 5:
1. preparare le immagini di calibrazione: acquisizione insieme di immagini contenenti pattern noto ripreso da diverse angolazioni e posizioni con fotocamere da calibrare.
2. individuare punti chiave sul pattern noto.
3. stimare i parametri intrinseci della fotocamera
4. stimare i parametri di distorsione (tenendo conto della distorsione ottica della fotocamera stimando i parametri di distorsione che descrivono la deformazione delle immagini causate dalle caratteristiche ottiche della fotocamera stessa)
5. ottimizzazione e valutazione dei parametri stimati per ridurre l'errore di riproiezione (discrepanza tra punti stimati e punti osservati sulle immagini)

I vantaggi del metodo sono l'automazione del processo di calibrazione, che riduce la necessità di misurazioni manuali complesse, la precisione, visto che tiene conto di molteplici immagini e punti chiave. Infine il metodo può gestire distorsioni e variazioni nelle condizioni di illuminazione, produce quindi risultati più robusti e affidabili.

