---
id: CANNY_EDGE_DETECTOR
aliases: []
tags: []
index: 29
---

# CANNY EDGE DETECTOR

A first formal definition of the characteristics of a strong edge detection system was given by John F. Canny, according to this definition a strong edge detection algorithm must:

-  correctly extract edges in noisy images.(**Good Detection**)
-  minimize distance between the found edge and the “true” edge. (**Good Localization**)
-  detect one single edge pixel at each “true” edge.(**One Response to One Edge**)

A good implementation of the Canny edge detector is obtained by [Gaussian filtering](GAUSSIAN_FILTER.md) followed by [gradient computation](EDGES.md#GRADIENT_APPROXIMATION) and [NMS](EDGES.md#NON_MAXIMA_SUPRESSION_(NMS)) along the gradient direction

```mermaid
flowchart LR
A[GAUSSIAN FILTERING]
B[GRADIENT COMPUTATION]
C[NMS]
A --> B
B --> C
```

A possible improvement can be done by [exploiting the separability](GAUSSIAN_FILTER.md#EXPLOITING_SEPARABILITY_TO_IMPROVE_PERFORMANCE) of the 2D Gaussian function

## NMS EDGE DETECTION IMPROVEMENTS

In order to improve the **NMS** process Canny propose a 2 threshold approach $T_h$ $T_l$ where a pixel is considered an edge if it's magnitude it's above $T_h$ or it's above $T_l$ and it's a neighbor of an already edge detected pixel

![](Pasted_image_20240309145141.png)

## FINAL PIPELINE

![](Pasted_image_20240309145554.png)

## IMPLEMENTATION

There is an implementation of Canny edge detector in the `opencv2` library follows an example for reference

```python
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# read image
img = cv.imread('image.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"

# compute canny edge detection
edges = cv.Canny(img,100,200)
```

This implementation does not perform [Gaussian smoothing](GAUSSIAN_FILTER.md) before

[PREVIOUS](pages/local_features/EDGES.md) [NEXT](pages/local_features/ZERO_CROSSING_EDGE_DETECTION.md)
