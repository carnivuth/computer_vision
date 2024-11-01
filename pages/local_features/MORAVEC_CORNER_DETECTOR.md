---
id: MORAVEC_CORNER_DETECTOR
aliases: []
tags: []
index: 31
---

# MORAVEC CORNER DETECTOR

In this detector the measure of cornerness is given by

$$
C(p) = \min_{q \in n_8(p)}{\Vert N(p)-N(q)\Vert^2}
$$

Where $N$ is the neighborhood around the point and its neighbors

The output is the lowest difference computed between the neighborhood of $p$ and the neighborhoods of the neighbor points $q$

![](Pasted_image_20240310153802.png)

[PREVIOUS](pages/local_features/ZERO_CROSSING_EDGE_DETECTION.md) [NEXT](pages/local_features/HARRIS_CORNER_DETECTOR.md)
