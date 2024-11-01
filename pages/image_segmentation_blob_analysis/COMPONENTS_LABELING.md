---
id: COMPONENTS_LABELING
aliases: []
tags: []
index: 25
---

# COMPONENTS LABELING

In this process elements that belongs to different connected component are given different labels

## CONNECTIVITY AND CONNECTED COMPONENTS

given a connectivity neighborhood defined as follows

$$
\begin{bmatrix}
&n & \\
n&p&n \\
&n & \\
\end{bmatrix} \rightarrow n_4(p)
$$
$$
\begin{bmatrix}
n&n &n \\
n&p&n \\
n&n &n \\
\end{bmatrix} \rightarrow n_8(p)
$$
A path from pixel $p$ to pixel $q$ is a sequence of pixels $p=p_1, p_2,…,p_n=q$ such that $p_i$ and $p_{i+1}$ are neighbors according to the chosen connectivity.

A set $R$ of pixel is a connected region if all pixels are connected

A connected region is a connected (foreground/background) region if all pixels in the region are (foreground/background)

**A connected component of a binary image is a maximal connected foreground region**

## LABELING BY FLOOD-FILL

A new label is propagated throughout a connected component starting from a “seed” pixel. Propagation is typically carried out by a iterative procedure which requires scanning the image multiple times.this solution is not efficient

![](Pasted_image_20240303174654.png)

[PREVIOUS](pages/image_segmentation_blob_analysis/BINARY_MORPHOLOGY.md) [NEXT](pages/image_segmentation_blob_analysis/BLOB_ANALYSIS.md)
