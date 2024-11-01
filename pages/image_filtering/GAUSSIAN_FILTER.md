---
id: GAUSSIAN_FILTER
aliases: []
tags: []
index: 17
---

# GAUSSIAN FILTER

Gaussian filter is an [LTE operator](LTE_OPERATORS.md) with a 2D Gaussian function as a impulse response (with $\mu = 0$ and a constant diagonal covariance matrix)

$$
G(x,y) = G(x)G(y) = \frac{1}{2\pi\sigma^2}e^{-\frac{x^2+y^2}{2\sigma^2}}
$$

![](Pasted_image_20240229123834.png)

The effect of increasing $\sigma$ can be seen as reducing the importance of the closest points and increasing the importance of farther points smoothing the image

## CHOOSING KERNEL SIZE

In a real implementation the Gaussian function need to be approximated by a discrete representation by sampling the function in a kernel matrix, so the matrix size need to be set

- with higher size matrix becomes more accurate
- computational cost grows with matrix size

so a rule of thumb is to select the **kernel size based on the $\sigma$ value as**

$$
kernel \space size = (2k+1) \times (2k +1) \space where \space k = 3\sigma
$$

as $3\sigma$ covers the 99% of the area of the function (energy)

## EXPLOITING SEPARABILITY TO IMPROVE PERFORMANCE

To improve the computational complexity, the separability of the 2D Gaussian function can be used as $G(x,y) = G(x)G(y)$

$$
I(x,y)\ast G(x,y) = I(x,y)\ast G(x)\ast G(y) =I(x,y)\ast G(y)\ast G(x)
$$

The speedup improvements of this process can be expressed as

$$
S =\frac{2(2k+1)^2}{4(2k + 1)} = k +\frac{1}{2} \space with
$$
$$
NOPS_{2D \space filter} =2(2k+1)^2\\
$$
$$
NOPS_{1D \space filter} =4(2k+1)\\
$$

[PREVIOUS](pages/image_filtering/MEAN_FILTER.md) [NEXT](pages/image_filtering/MEDIAN_FILTER.md)
