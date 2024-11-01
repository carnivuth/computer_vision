---
id: BINARIZATION
aliases: []
tags: []
index: 22
---

# BINARIZATION
## GRAY LEVEL HISTOGRAM

histogram of the number of pixel for each light intensity defined as:

$$
p =\begin{bmatrix}u \\ v\end{bmatrix}, \space
\forall \space p \in I \space H[I(p)]++\\
$$

![](Pasted_image_20240302130200.png)

This histogram does not contain spatial information so a **different arranged set of the same pixels produces the same histogram**

## BINARIZATION BY INTENSITY THRESHOLDING

Binarization can be computed by simply selected a threshold $T$ and splitting the points $I(p) \lt T | I(p) \gt T$

### THRESHOLD SELECTION

In real case scenarios the light stability of the image is not guaranteed so there is the need to select dynamically the threshold

#### DUMB APPROACH
#### $T=\mu$

This is the simplest threshold selection method, it works only if points are evenly distributed in the histogram

![](Pasted_image_20240302144849.png)

#### PEAKS METHOD

This method set T as the minimum of the function between the 2 main peaks

$$
T = argmin(h(i); i \in [i_1,i_2])
$$

![](Pasted_image_20240302145905.png)

This method need the histogram smoothing to avoid been trapped in local minimums

#### OTSU'S ALGORITHM

The idea behind this method is to divide the histogram into 2 main regions with the aim of **minimizing the within group variance**

so given the following definitions:

- $i =1...L$ -> gray levels
- $N$ -> Number of pixels
- $h(i)$ -> entry of the histogram
- $p(i)= h(i)/N$ -> probability of gray level $i$

The mean and variance could be calculated as follows

$$
\mu = \sum_{i=1}^{L}{i*p(i)}, \space \space \sigma^2 = \sum_{i=1}^{L}{(i-\mu)^2p(i)}
$$

Any given $t$ would split the histogram into 2 different regions with mean and variance defined as follows

$$
\mu_{1}(t) = \sum_{i=1}^{t}{i*\frac{p(i)}{q_1(t)}}, \space \space \sigma^2_{1} = \sum_{i=1}^{t}{(i-\mu_{1})^2\frac{p(i)}{q_1(t)}}
$$
$$
\mu_{2}(t) = \sum_{i=t+1}^{L}{i*\frac{p(i)}{q_2(t)}}, \space \space \sigma^2_{2} = \sum_{i=t+1}^{L}{(i-\mu_{2})^2\frac{p(i)}{q_2(t)}}
$$
$$
with:
$$
$$
q_1(t)= \sum_{i=1}^{t}p(i), \space \space q_2(t)= \sum_{i=t+1}^{L}p(i),
$$

The within group variance is defined as the weighted sum of the variance of the 2 regions

$$
\sigma^2_W(t) = \sigma_1^2*q_1(t) + \sigma_2^2*q_2(t)
$$

The algorithm aims to minimize this value with the assumption that the regions created from best $T$ will have all points concentrated in a relative small region (eg little variance)

## ADAPTIVE THRESHOLDING

Any global thresholding method rely on the assumption of uniform lighting across the scene, if this assumption is violated  it's necessary to compute the threshold in function of the spatial variation

The idea is to **compute the threshold at each point of the image** based on a neighborhood of pixels (threshold become a function of space $T(x,y)$), This introduce the problem of neighborhood dimension cause a too small one could lack of foreground pixels

[PREVIOUS](pages/image_segmentation_blob_analysis/COMPUTER_VISION_INDUSTRIAL_WORKFLOW.md) [NEXT](pages/image_segmentation_blob_analysis/COLOR_BASED_SEGMENTATION.md)
