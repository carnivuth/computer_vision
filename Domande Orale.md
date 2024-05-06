---

---
**
# Filtro Bilaterale?

The BILATERAL FILTER is an advanced non linear filter used to accomplish denoising of Gaussian-like noise without blurring the image, it is a non linear filter that consider space distance and intensity differences during the processing.
![[Pasted image 20240505184308.png]]

space distance= distance between image pixels, mesured based on the position of the pixel in the image plane
intensity distance= difference of intensity between pixels measured based on the difference of the level of gray or change of color between pixels.
We use these distances to calculate the weight of the pixels during the process. (pixel that are closer and of similar intensity should weight more while pixels that are distant or with different intensities should be lighter)

When we consider a pixel we have a supporting window
q= running pixels
output= a weighted sum
H-> should be larger when q is close to p and Ip is similar to Iq , and small otherwise.

The Gaussian functions are for space and range
The first is a function for the distance between P and Q and it's small when the argument
is large-> DECREASING FUNCTION OF THE DISTANCE

The second have an argument that is the difference between Ip and Iq -> large weight if the pixel are close.

To garantee a unity gain we need to considere also W(p,q), that is a function that aims to normalize our coefficients-> sum of all H values of the 2 Gaussians.

So to conclude:
Neighbouring pixel take a larger weight as they get closer and similar to the central pixel. The neighbours falling on the other side of the edge look different and cannot contribute to the output=> asymmetric type of impulse response.

This type of filter is used in programs for photos but it's slow (it has to compute all pixels of the image before applying the algorithm)

###

USato per ridurre il rumore mantenendo i bordi e i dettagli dell'immagine, efficace nel ridurre il rumore gaussiano senza introdurre sfocature indesiderate, utile in app per miglioramento immagine segmentazione dell'immagine e visione robotica.

( rumore gaussiano= tipo comune di rumore presente nelle immagini digitali e in altri segnali elettronici. Questo tipo di rumore segue una distribuzione normale (o gaussiana) ed è caratterizzato da una distribuzione di probabilità simmetrica intorno a una media, con una varianza che determina la larghezza della distribuzione. )

(perchè importante similarità tra pixel? Determina i pesi usati durante il processo di filtraggio-> i pixel vicini nello spazio tendono ad avere caratteristiche visive simili, spesso rappresentano parti della stessa regione, i pixel con valori di intensità simili sono considerati più 'simili' rispetto a intensità diverse, si riferisce alla differenza luminosa o di colore tra pixel)

# Template Matching - con SSD SAD NCC ZNCC
Talking about object detection problems-> given a reference image of the object we need to determine if the object is in the image we analize, if found we need to estimate the pose of the object.

In template matching you:
1 create the template (an image of small dimensions that represents the model we are searching for)
2 pass the template on the scene image pixel by pixel or in multiple steps and compare the 2 in each position
3 calculate the similarity
4 localize the match

We can maximaze a similarityfunction or minimaze a dissimilarity one.
SDD and SAD are methods of valuation of the similaritybetween two blocks 

Let's consider ì(i,j) and T MxN dimensional vectors 
![[Pasted image 20240505184517.png]]
SSD Sum of Squared Differences = the squared L2 norm of their difference 
It calculates the similarity between two blocks of pixels by summing the squared differences pixel per pixel in the blocks
You obtain a measure of the distance between the blocks-> lower is the value of SSD higher the similarity, but it penalize more the differences because of the square

SAD Sum of Absolute Differences = L1 norm of the difference between the vectors 
it calculates the similarity between blocks of pixels summing the absolute differences pixel per pixel 
You obtain a measure of the distance between the blocks-> lower is the value of SAD higher the similarity
![[Pasted image 20240505184541.png]]
NCC Normalized CrossCorrelation = cosine of the angle between vectors, is invariant to linear intensity changes.
It votes the similarity between two blocks calculating the cross correlation between them and normalizing the result ( so the metric is indipendent from the scales and contrasts of the image)

So the result is a measure of the normalized similarity that vary from -1 to +1

(we can notice that the SAD is the same as SSD but if we change the template the best match is given by a given factor xT => then we prefer to use NCC==> if we don't have variance of intensity we may use SAD or SDD)

ZNCC is a variant of NCC where the blocks of pixels are centrated in their zero mean before the cross correlation calculus. 
ZNCC Zero mean NCC = computed after subtraction of the means
mu(ì) = zero mean normalized crosscorrelation
mu(T) = correation coefficient
![[Pasted image 20240505184438.png]]
The result is a measure of the normalized similarity that vary from -1 to +1 but the blocks are centrated.

ZNCC is more robust in terms of brightness and can be prefered in some cases.

##
1 crei il template = immagine di piccole dimensioni che rappresenta il modello che cerchiamo dalla scena input 
2 scorrimento dell'immagine input = il template viene scorso sull'immagine in modo sistemico spostandosi pixel per pixel o a passi multipli, ogni posizione del template viene confrontata
3 calcola la similarità = per valutare quanto un template assomiglia a una regione viene usata una metrica di similarità (somma dei quadrati delle differenze o cross-correlazione normalizzata). Queste metriche calcolano la discrepanza tra template e regione dell'immagine in input 
4 localizzazione del match = nello scorrimento del template sull'immagine di input la posizione con massima similarità viene identificata come la posizione in cui il template corrisponde più strettamente all'immagine di input 

Ampiamente usato in diversi contesti di riconoscimento, rilevamento, tracking o altro.

Può però essere sensibile a variazioni di scala, rotazione, illuminazione e ombreggiatura-> importante progettare template robusti e usare metodi avanzati per migliorare la precisione e l'affidabilità del matching.

# Shape Matching
The tecnique is used to compare and find corrispondences between shapes or regions in images (understanding if two shapes are similar or are the same but in different sizes or rotations)
The shape based matching can be though of as 'edge-based template matching approach'
-> a set of control points is extracted from the model image by an Edge Detection operation and the gradient orientation at each Pk is recorded, then at each position of the target image the recorded gradient orientations associated with the control points are compared to those at their corresponding image points to compute a similarity function, we slide a window and compare in each position the points of the position of the edge pixel in the template.
If we consider only the blue arrows we don't consider all the positions.
If we compute the black gradients we obtain the blue arrow and they are perfectly aligned, we assess also the similarity with the red arrow= match the shape of the contour and the current sub image.

![[Pasted image 20240505184635.png]]
![[Pasted image 20240505184700.png]]

The similarity function span the interval [-1,1] and takes its max when all the gradients at the control points in the current window are perfectly aligned to those at the control points of the model image.
Choose a detection threshold is specifying the fraction of model points that must be seen in the image to trigger the detection

![[Pasted image 20240505184731.png]]
The function doesn't change with lighting changes we have derivatives and we are not considering magnitude so its invariant to light. 
We extract edges in the template and perform edge detection only in the template and not in the image.

another answer:

1 estrarre le caratteristiche: trovare le caratteristiche discriminative dalle forme delle regioni o ogeetti nelle immagini, queste possono includere contorni, punti chiave, descrittori di forma o altro
2 normalizzare le forme: le forme estratte vanno normalizzate per ridurre gli effetti di scala rotazione e traslazione. Ciò si può fare allineando le forme rispetto un sistema di coordinate comune o normalizzando le dimensioni delle forme
3 calcolo della similarità: estratte e normalizzate le caratteristiche delle forme si calcola una misur di similarità per confrontare le forme, questa può essere basata su diverse tecniche come distanza euclidea, funzioni di distanza o uso di descrittori di forma ecc
4 cerca la migliore corrispondenza: usando la misura di similarità calcolata vengono cercate le corrispondenze più significative tra le forme, a seconda del contesto dell'applicazione possono essere adottati diversi approcci per la ricerca delle corrispondenze ottimali come l'uso di algoritmi di ricerca delle corrispondenze ottimali o di ricerca locale o globale.


----- 

come hai implementato la color specification?

qual'è la differenza tra l'approccio F2R e F2F? (basta dirgli quello che ha scritto lui nel documento con la descrizione del progetto) in particolare, nel F2F alla fine concateno omografie e, quindi, propago errore

hai dato un'occhiata al ransac? --> basta una descrizione di 4 parole

perchè nelle varie iterazioni RANSAC stima omografia usando solo 4 dei punti a disposizione e non tutti ? 

perchè i punti potrebbero essere affetti da rumore. Così facendo, invece, calcolando l'errore gemetrico in base all'omografia stimata, riesce prima a trovare un certo numero di INLIER e, all'ultima iterazione, stima l'omografia usando tutti gli inlier trovati

  

parlami della trasformata di HOUGH

importante ricordarsi di dirgli che viene applicata solo agli EDGE POINT (quindi devo prima applicare un edge detection) e non a tutti i pixel dell'immagine

  

quando gli ho detto che HOUGH è robusto al rumore mi chiede:

le immagini hanno sempre rumore? se sì come possiamo stimarlo? e a cosa è dovuto?

le immagini hanno sempre rumore ovvero, prendendo due immagini di una stessa scena perfettamente statica (quindi anche illuminazione costante), lo stesso pixel avrà valori diversi nelle due immagini. questo è dovuto al DARK CURRENT NOISE e, quindi, glie elettroni vengono convertiti in fotoni (o qualcosa del genere)

  

hough generalizzata, come cambia l'AA se voglio tenere in considerazione le rotazioni ? (diventa 3D, ogni livello dell'AA corrisponde a una data rotazione)

  

shape-based matching

tutto, in particolare 

- dove applico l'edge detection? (solo al template)

-quando due gradienti coincidono? cos(TETA)=1

-punti di forza

  

  

Esame 2

(Progetto "Motorcycle Rods")

Domande varie sul progetto del tipo perchè hai usato questa funzione o spiegami l'algoritmo che hai usato...

  

Algoritmo di Otsu per la scelta delle soglie: quale è l'idea di fondo e quale è la formula che cerca di minimizzare (quella canonica delle varianze all'interno dei gruppi, non quella ottimizzata)

  

Parlami dello shape matching e di quali sono le sue caratteristiche. 

Formula della similarità usata per lo shape matching, come posso renderla più robusta (valore assoluto) e come posso velocizzarla (considero solo i primi p punti per fare un primo controllo)

  

Dimmi cosa si intende per orientamento di un oggetto e come si può trovare il valore dell'angolo sfruttando la matrice di covarianza.

  

Cosa sono i punti di fuga di una retta, come si calcolano visivamente, in coordinate euclidee e in coordinate del projective space.

  

Totale circa un ora di orale, cerca di venire abbastanza incontro, ma vuole risposte precise e possibilmente motivate da formule. 

  

  

ESAME 3

Progetto Reltà aumentata: Differenze tra F2F e F2R pro e contro; algoritmo di ExtractFeatures, di MatchFeatures e RANSAC.

  

Shape Matching, 

-formula, 

-tutto in particolare e perchè è robusto alle occlusioni, 

-perchè l'edge detection applicato solo alla model image è un punto di forza. 

-Come si calcola il coseno (della formula) tra due gradienti.

  

Edge detection con sogliatura del gradiente, sempre la formula.

  

Filtro Bilaterale, 

-formula e tutto ciò che riguarda il filtro. 

-In più nella formula spiegargli bene perchè normalizzo e cosa vuol dire mantenere unitario il guadagno di un filtro.

  

Un'ora di orale, mette a prioprio agio e fa ragionare senza pressioni. Vuole risposte dettagliate e motivate da formule

che chiede anche quelle nel dettaglio per vedere se la formula l'hai capita e non solo imparata a memoria.

  

  
  
  
  
  

- 22 gennaio 2016
    

  

- Domande varie sul progetto presentato (Aumented reality).

- template matching come si fa, 

-le funzioni di similarità, 

-descrizione delle differenze e perchè usare una piuttosto che un'altra (robustezza a cambi di intensità).

- NCC, come implementarla in modo più efficiente? Trasformata di Fourier.

- Un metodo per velocizzare in generale? Ho spiegato l'algoritmo che usa il bound

- Filtro bilaterale. 

Concetti chiave, a cosa serve, 

formula e grafico di uno edge dove ti fa domande e devi mostrare sul disegno quali pixel influenzano e perché quindi il contorno non subisce smooth. 

Cosa serve il fattore di standardizzazione?

  

Orale durato più di un'ora. Lui è tranquillo, ma vuole sapere se hai capito bene le cose, per esempio ad un certo punto mi ha chiesto come si fa il prodotto scalare tra due vettori in R3. Le formule ovviamente le devi sapere ma l'importante è che tu abbia capito a fondoo i concetti.

Voto alto, andate tranquilli.

------------------------------------------------------------------------------------------------------------------

- 22 febbraio 2016
    

-Domande sul progetto (Agumented Reality): perchè utilizzare i corner come feature points, descrizione di Ransac, perchè ransac inizialmente utilizza solo 4 corrispondenze, approccio F2F e F2R, algoritmo di color spcification;

-Shape Based Matching (tutto e nei dettagli);

-Sistema di visione stereo: 

come determinare i punti omologhi, 

sistema stereo laterale e geometria epipolare (con tanto di disegni), 

che cos'è e come si determina la disparità. 

------------------------------------------------------------------------------------------------------------------

- Orale 04/03/2016
    

Progetto "Motorcycle Rods"

Domande varie sul progetto, tipo "perchè hai usato questo filtro? Perchè lo hai utilizzato in questa fase e non in quest'altra?", domande su eventuali algoritmi implementati.

  

Filtro bilatelare: 

-concetto fondamentale e formula, com tutte le spiegazioni e gli esempi del caso. 

-Come nel caso di un esame precedente, ha voluto sapere perchè c'è bisogno della normalizzazione (per avere il guadagno unitario), 

-e cosa significa quindi guadagno unitario e perchè è necessario averlo.

  

Altri tipi di filtri non lineari, quindi 

filtro mediano 

-(mi ha chiesto anche perchè il filtro mediano non è adatto per il rumore di tipo gaussiano: perchè il mediano non crea nuovi valori, ma ne seleziona uno tra quelli dell'immagine, quindi il valore scelto manterrà comunque il rumore, che è presente su tutti i pixel) 

- e non local mean (ultima pagina delle slide sui filtri). Per quest'ultimo gli ho subito detto che non ricordavo nello specifico la formula ma si è accontentato del concetto che c'è sotto.

  

Trasformata di Hough con spegazione dettagliata e anche 

trasformata generale di hough,

- comprensiva di gestione delle rotazioni e della scala.

  

Orale di circa 30 minuti, professore mooolto tranquillo e voti alti. Basta aver capito bene gli argomenti e si va lisci.

--------------------------------------------------------------------

- 5 aprile 2016
    

_image warping

- filtri non lineari

-shape based

-vanishing points

  

--------------------------------------------------------------------

- 15 aprile 2016
    

-Domande sul progetto (codebar)

-Hough Transform Generalizzata nel dettaglio

-Shape Based Matching nel dettaglio

-Zhang in generale 

-più la dimostrazione sulla parte della distorsione delle lenti

  

--------------------------------------------------------------------

  

- 3 Maggio 2016
    

Progetto "Motorcycle Rods"

-Domande varie sul progetto, spiegami l'algoritmo usato in questo punto. Secondo te la funzione findcontours di opencv come fa ad individuare i contorni? Altri metodi alternativi per la ricerca del contorno in un immagine binarizzata (utilizzare l'erosione)? La funzione matchShapes di opencv come lavora al suo interno? E' invariante per scala? Altri metodi alternativi?

  

-Calibrazione e distorsione delle lenti. 

Domande varie del tipo: 

-Quando andiamo a calcolare i coefficenti di distorsione? 

-Perche' e' importante effettuare il passaggio dal sistema di riferimento mondo al s.d.r. della camera?

  

-Trasformata di hough per rette e generalizzata in dettaglio

  

--------------------------------------------------------------------

  

- 8 Giugno 2016
    

-Progetto "Motorcycle Rods": domande varie sul progetto, perchè ho usato un determinati filtri o algoritmi nelle varie parti, quanto le soluzioni che ho fornito fossero robuste a vari cambiamenti di forma delle bielle, idee e tentativi effettuati per separare le bielle che si toccano.

  

-trasformata di Hough generalizzata, come funziona precisamente, 

-rotazione e scala, 

-robustezza all'offuscamento, 

vantaggi

-shape based matching, 

-l'idea, come funziona (ovvero sempre "sliding window", non di tutto ma solo dei punti di controllo sull'immagine I), 

-quali vantaggi comporta, 

-importanza di fare edge detection solo su template e non sull'immagine I

-canny, 

-giusto un ragionamento veloce sui parametri customizzabili, ovvero la sigma della gaussiana e i due valori di soglia dell'isteresi 

-filtro bipolare, a cosa serve, qual'è l'idea che c'è dietro, che miglioramenti comporta, perchè è strutturato in quel modo 

(forse intende bilaterale)

  

circa 45minuti di orale, docente veramente gentile, mette a proprio agio e non incute fretta. Più che la formula a memoria richiede ragionamenti per vedere se si è capito il concetto.

--------------------------------------------------------------------

  

- ORALE DEL 24/02/2017
    

  

Il prof   molto tranquillo, parte dal progetto ed in particolare dalla relazione per fare domande sugli approcci adottati per risolverlo e/o eventuali approcci alternativi che possono venire in mente.

Poi si concentra sulla teoria. A me in particolare ha chiesto:

1. Trasformata di Hough, sia quella relativa al riconoscimento di rette, 
    

1. sia a quella generalizzata 
    
2. ed in particolare domande su tutto ci  che riguarda quella parte (robustezza al rumore, resistenza alle occlusioni, problema della quantizzazione)
    

3. Punto di fuga: definizione 
    

1. e calcolo del VP di una retta generica ricorrendo alla PPM e allo spazio proiettivo.
    

Un’ora circa di orale, con domande anche abbastanza incalzanti ma non mette fretta ed   molto tranquillo.

  

----------------------------------------------------------------------

- ORALE DEL 14/02/2018
    

  

1. Domande sul progetto (connecting rods), abbiamo guardato insiemi alcuni punti della relazione, non è entrato nel dettaglio del codice, mi ha fatto notare che ho gestito in modo poco efficiente l’eliminazione del rumore, cioè dopo il labeling. Andava fatto prima o con un opening con elemento strutturale piccolo o con un filtro mediano.
    
2. LOG, dove si usa (edge detection non semplicemente sugli zeri ma sugli zero crossing), 
    

1. come si implementa 
    
2. e com’è possibile trasformare la convoluzione bidimensionale in 4 convoluzioni unidimensionali (con notevole risparmio computazionale), con formule e passaggi.
    

4. Calcolo del punto di fuga:
    

1. partire dall’equazione della retta col vettore di coseni direttori per
    
2. passare allo spazio proiettivo e ottenere il punto improprio per λ→∞
    
3. usare la matrice PPM per proiettare il punto improprio sul piano immagine
    
4. tornare allo spazio euclideo dividendo per la terza coordinata, far presente che se fosse uguale a zero le rette sono parallele al piano immagine e quindi il VP è all’infinito
    

----------------------------------------------------------------------

- ORALE del 03/09/2021
    

Domande sul progetto Augmented Reality: 

- Mi spieghi in generale come avete risolto il problema proposto
    
- Perché si usa RANSAC? Che vantaggio ha?
    

Domande di teoria:

- Generalized Hough Transform NON riferita agli edge, ma riferita ai descrittori SIFT (ultimissimo argomento del corso, con fase online e fase offline da spiegare bene nel dettaglio)
    
- Punto di fuga di una retta 3D in coordinate omogenee (partire dalla definizione di punto di fuga e poi ricondursi alle coordinate omogenee)
    

  

Un’ora di orale, esame online. 

Bisogna sapere bene i termini delle formule e perché si fa così o cosà, non gli va bene sapere le formule a memoria senza averne compreso il significato.

--------------------------------------------------------------------------------

ORALE DEL 2021 DI C:

-Zhang x2, però chiedendomi proprio le dimensioni di ciascuna matrice e cose simili, 

- Omografie

  

Orali vari 2021:

-lens distortion e come lo si modellava e si teneva in considerazione in Zhang

-

  
  

1° capitolo) chiesto in 8 esami: 

5 Punto di fuga, 

1 omografie

8 Zhang in generale e Distorsione lenti

2° capitolo) chiesto in 4 esami: 

1 warping, 

2 mediano, 

6  bilaterale, 

2 Non-Local

3° capitolo) chiesto in 1 esame: 

1 erosion

4° capitolo) chiesto in 2 esami: 

1 Edge detection, 

1 Canny, 

1 LOG

5° capitolo) chiesto in 9 esami: 

2 Template M, 

8 Shape-Based Matching, 

4 HT, 

6 GHT, 

1 Star Model 

  

Info raccolte su 16 esami totali

**
-------------------------------------------

**

- Domande varie sul progetto presentato (Aumented reality).

- template matching come si fa, le funzioni di similarità, descrizione delle differenze e perchè usare una piuttosto che un'altra (robustezza a cambi di intensità).

- NCC, come implementarla in modo più efficiente? Trasformata di Furier.

- Un metodo per velocizzare in generale? Ho spiegato l'algoritmo che usa il bound

- Filtro bilaterale. Concetti chiave, a cosa serve, formula e grafico di uno edge dove ti fa domande e devi mostrare sul disegno quali pixel influenzano e perché quindi il contorno non subisce smooth. Cosa serve il fattore di standardizzazione?

  

Orale durato più di un'ora. Lui è tranquillo, ma vuole sapere se hai capito bene le cose, per esempio ad un certo punto mi ha chiesto come si fa il prodotto scalare tra due vettori in R3. Le formule ovviamente le devi sapere ma l'importante è che tu abbia capito a fondoo i concetti.

Voto alto, andate tranquilli.

------------------------------------------------------------------------------------------------------------------

22 febbraio 2016

-Domande sul progetto (Agumented Reality): perchè utilizzare i corner come feature points, descrizione di Ransac, perchè ransac inizialmente utilizza solo 4 corrispondenze, approccio F2F e F2R, algoritmo di color spcification;

-Shape Based Matching (tutto e nei dettagli);

-Sistema di visione stereo: come determinare i punti omologhi, sistema stereo laterale e geometria epipolare (con tanto di disegni), che cos'è e come si determina la disparità. 

  

-----  Orale 25/02/2015

Filtro Bilaterale

Template Matching - con SSD SAD NCC ZNCC

Shape Matching

  

----- 

(progetto AUGMENTED REALITY)

come hai implementato la color specification?

qual'è la differenza tra l'approccio F2R e F2F? (basta dirgli quello che ha scritto lui nel documento con la descrizione del progetto) in particolare, nel F2F alla fine concateno omografie e, quindi, propago errore

hai dato un'occhiata al ransac? --> basta una descrizione di 4 parole

perchè nelle varie iterazioni RANSAC stima omografia usando solo 4 dei punti a disposizione e non tutti ? 

perchè i punti potrebbero essere affetti da rumore. Così facendo, invece, calcolando l'errore gemetrico in base all'omografia stimata, riesce prima a trovare un certo numero di INLIER e, all'ultima iterazione, stima l'omografia usando tutti gli inlier trovati

  

parlami della trasformata di HOUGH

importante ricordarsi di dirgli che viene applicata solo agli EDGE POINT (quindi devo prima applicare un edge detection) e non a tutti i pixel dell'immagine

  

quando gli ho detto che HOUGH è robusto al rumore mi chiede:

le immagini hanno sempre rumore? se sì come possiamo stimarlo? e a cosa è dovuto?

le immagini hanno sempre rumore ovvero, prendendo due immagini di una stessa scena perfettamente statica (quindi anche illuminazione costante), lo stesso pixel avrà valori diversi nelle due immagini. questo è dovuto al DARK CURRENT NOISE e, quindi, glie elettroni vengono convertiti in fotoni (o qualcosa del genere)

  

hough generalizzata, come cambia l'AA se voglio tenere in considerazione le rotazioni ? (diventa 3D, ogni livello dell'AA corrisponde a una data rotazione)

  

shape-based matching

tutto, in particolare 

- dove applico l'edge detection? (solo al template)

quando due gradienti coincidono? cos(TETA)=1

punti di forza

  

--------------------------------------------------

(Progetto "Motorcycle Rods")

Domande varie sul progetto del tipo perchè hai usato questa funzione o spiegami l'algoritmo che hai usato...

  

Algoritmo di Otsu per la scelta delle soglie: quale è l'idea di fondo e quale è la formula che cerca di minimizzare (quella canonica delle varianze all'interno dei gruppi, non quella ottimizzata)

  

Parlami dello shape matching e di quali sono le sue caratteristiche. 

Formula della similarità usata per lo shape matching, come posso renderla più robusta (valore assoluto) e come posso veloccizzarla (considero solo i primi p punti per fare un primo controllo)

  

Dimmi cosa si intende per orientamento di un oggetto e come si può trovare il valore dell'angolo sfruttando la matrice di covarianza.

  

Cosa sono i punti di fuga di una retta, come si calcolano visivamente, in coordinate euclidee e in coordinate del projective space.

  

Totale circa un ora di orale, cerca di venire abbastanza incontro, ma vuole risposte precise e possibilmente motivate da formule. 

  

--------------------------------------------------------

Progetto Reltà aumentata: Differenze tra F2F e F2R pro e contro; algoritmo di ExtractFeatures, di MatchFeatures e RANSAC.

  

Shape Matching, formula, tutto in particolare e perchè è robusto alle occlusioni, perchè l'edge detection applicato solo

                alla model image è un punto di forza. Come si calcola il coseno (della formula) tra due gradienti.

  

Edge detection con sogliatura del gradiente, sempre la formula.

  

Filtro Bilaterale, formula e tutto ciò che riguarda il filtro. In più nella formula spiegargli bene perchè normalizzo 

                e cosa vuol dire mantenere unitario il guadagno di un filtro.

  

Un'ora di orale, mette a prioprio agio e fa ragionare senza pressioni. Vuole risposte dettagliate e motivate da formule

che chiede anche quelle nel dettaglio per vedere se la formula l'hai capita e non solo imparata a memoria.

---------------------------------------------------------

Orale 04/03/2016

Progetto "Motorcycle Rods"

Domande varie sul progetto, tipo "perchè hai usato questo filtro? Perchè lo hai utilizzato in questa fase e non in quest'altra?", domande su eventuali algoritmi implementati.

  

Filtro bilatelare: concetto fondamentale e formula, com tutte le spiegazioni e gli esempi del caso. Come nel caso di un esame precedente, ha voluto sapere perchè c'è bisogno della normalizzazione (per avere il guadagno unitario), e cosa significa quindi guadagno unitario e perchè è necessario averlo.

  

Altri tipi di filtri non lineari, quindi filtro mediano (mi ha chiesto anche perchè il filtro mediano non è adatto per il rumore di tipo gaussiano: perchè il mediano non crea nuovi valori, ma ne seleziona uno tra quelli dell'immagine, quindi il valore scelto manterrà comunque il rumore, che è presente su tutti i pixel) e non local mean (ultima pagina delle slide sui filtri). Per quest'ultimo gli ho subito detto che non ricordavo nello specifico la formula ma si è accontentato del concetto che c'è sotto.

  

Trasformata di Hough con spegazione dettagliata e anche trasformata generale di hough, comprensiva di gestione delle rotazioni e della scala.

  

Orale di circa 30 minuti, professore mooolto tranquillo e voti alti. Basta aver capito bene gli argomenti e si va lisci.

--------------------------------------------------------------------

  

15 aprile 2016

-Domande sul progetto (codebar)

-Hough Transform Generalizzata nel dettaglio

-Shape Based Matching nel dettaglio

-Zhang in generale più la dimostrazione sulla parte della distorsione delle lenti

  

--------------------------------------------------------------------

  

5 aprile 2016

_image warping

- filtri non lineari

-shape based

-vanishing points

  

--------------------------------------------------------------------

  

3 Maggio 2016

Progetto "Motorcycle Rods"

-Domande varie sul progetto, spiegami l'algoritmo usato in questo punto. Secondo te la funzione findcontours di opencv come fa ad individuare i contorni? Altri metodi alternativi per la ricerca del contorno in un immagine binarizzata (utilizzare l'erosione)? La funzione matchShapes di opencv come lavora al suo interno? E' invariante per scala? Altri metodi alternativi?

  

-Calibrazione e distorsione delle lenti. Domande varie del tipo: Quando andiamo a calcolare i coefficenti di distorsione? Perche' e' importante effettuare il passaggio dal sistema di riferimento mondo al s.d.r. della camera?

  

-Trasformata di hough per rette e generalizzata in dettaglio

  
  

--------------------------------------------------------------------

  

8 Giugno 2016

-Progetto "Motorcycle Rods": domande varie sul progetto, perchè ho usato un determinati filtri o algoritmi nelle varie parti, quanto le soluzioni che ho fornito fossero robuste a vari cambiamenti di forma delle bielle, idee e tentativi effettuati per separare le bielle che si toccano.

  

-trasformata di Hough generalizzata, come funziona precisamente, rotazione e scala, robustezza all'offuscamento, vantaggi

-shape based matching, l'idea, come funziona (ovvero sempre "sliding window", non di tutto ma solo dei punti di controllo sull'immagine I), quali vantaggi comporta, importanza di fare edge detection solo su template e non sull'immagine I

-canny, giusto un ragionamento veloce sui parametri customizzabili, ovvero la sigma della gaussiana e i due valori di soglia dell'isteresi 

-filtro bipolare, a cosa serve, qual'è l'idea che c'è dietro, che miglioramenti comporta, perchè è strutturato in quel modo 

  

circa 45minuti di orale, docente veramente gentile, mette a proprio agio e non incute fretta. Più che la formula a memoria richiede ragionamenti per vedere se si è capito il concetto.

  

--------------------------------------------------------------------

  

ORALE DEL 24/02/2017

  

Il prof   molto tranquillo, parte dal progetto ed in particolare dalla relazione per fare domande sugli approcci adottati per risolverlo e/o eventuali approcci alternativi che possono venire in mente.

Poi si concentra sulla teoria. A me in particolare ha chiesto:

1) Trasformata di Hough, sia quella relativa al riconoscimento di rette, sia a quella generalizzata ed in particolare domande su tutto ci  che riguarda quella parte (robustezza al rumore, resistenza alle occlusioni, problema della quantizzazione)

2) Punto di fuga: definizione e calcolo del VP di una retta generica ricorrendo alla PPM e allo spazio proiettivo.

UnÕora circa di orale, con domande anche abbastanza incalzanti ma non mette fretta ed   molto tranquillo.

  

----------------------------------------------------------------------

  

ORALE DEL 14/02/2018

  

1. Domande sul progetto (connecting rods), abbiamo guardato insiemi alcuni punti della relazione, non è entrato nel dettaglio del codice, mi ha fatto notare che ho gestito in modo poco efficiente l’eliminazione del rumore, cioè dopo il labeling. Andava fatto prima o con un opening con elemento strutturale piccolo o con un filtro mediano.
    
2. LOG, dove si usa (edge detection non semplicemente sugli zeri ma sugli zero crossing), come si implementa e com’è possibile trasformare la convoluzione bidimensionale in 4 convoluzioni unidimensionali (con notevole risparmio computazionale), con formule e passaggi.
    
3. Calcolo del punto di fuga:
    

1. partire dall’equazione della retta col vettore di coseni direttori per
    
2. passare allo spazio proiettivo e ottenere il punto improprio per
    
3. usare la matrice PPM per proiettare il punto improprio sul piano immagine
    
4. tornare allo spazio euclideo dividendo per la terza coordinata, far presente che se fosse uguale a zero le rette sono parallele al piano immagine e quindi il VP è all’infinito
    



**

-----------------------------------------------------------------

--------------------------------------------------------------------------
