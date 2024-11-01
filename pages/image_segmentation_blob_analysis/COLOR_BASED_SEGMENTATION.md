---
id: COLOR_BASED_SEGMENTATION
aliases: []
tags: []
index: 23
---

# COLOR BASED SEGMENTATION

Given a pixel $p$, and the color intensity is defined as $I(p) = \begin{bmatrix}I_r(p)\\ I_g(p)\\ I_b(p)\\ \end{bmatrix}$ the segmentation can be done by calculating the distance from each color vector from a reference background color $\mu$

$$
\forall \space p \in I \begin{cases}
d(I(p),\mu)\leq T \rightarrow O(p) = Background \\
d(I(p),\mu)\gt T \rightarrow O(p) = Foreground\\
\end{cases}
\space with
$$
$$
d(I(p),\mu) = \sqrt{(I_r(p)-\mu_r)^2+ (I_g(p)-\mu_g)^2 + (I_b(p)- \mu_b)^2}
$$

the $\mu$ vector can be obtained by a set of training images as the mean of the samples:

$$
\mu = \begin{bmatrix}\mu_r \\ \mu_g \\ \mu_b\end{bmatrix} = \frac{1}{N}\sum_{k=1}^{N}I(p_k)
$$

and then the segmentation become a classification task where the foreground pixels are the ones in a 3d sphere with center $\mu$

![](Pasted_image_20240303160809.png)

## MAHALANOBIS DISTANCE

A more precise way of making color based segmentation is to consider the covariance also with means, the covariance matrix is obtained in the training phase as follows

$$
\Sigma = \begin{bmatrix}
\sigma^2_{rr} &&\sigma^2_{rg} &&\sigma^2_{rb} \\
\sigma^2_{gr} &&\sigma^2_{gg} &&\sigma^2_{gb} \\
\sigma^2_{br} &&\sigma^2_{bg} &&\sigma^2_{bb} \\
\end{bmatrix} \space with
$$
$$
\sigma^2_{ij} = \frac{1}{N}\sum_{k=1}^{N}(I_i(p_k) - \mu_j)(I_j(p_k) - \mu_j)
$$
$$
i,j \in \{r,g,b\}
$$
The new distance measure is given by the inclusion of the covariance matrix in the euclidean distance

$$
d_M(I(p),\mu) = \sqrt{(I(p)-\mu)^T \Sigma^{-1}(I(p)-\mu)}
$$

That in the case of a diagonal covariance matrix becomes

$$
d_M(I(p),\mu) = (\frac{(I_r(p) - \mu_r)^2}{\sigma^2_{rr}} + \frac{(I_g(p) - \mu_g)^2}{\sigma^2_{gg}} +\frac{(I_b(p) - \mu_b)^2}{\sigma^2_{bb}})
$$

The mahalanobis distance weights the differences between the color components unequally (inversely proportional to the learned variances ), This as the effect of lower the consideration of sparse components

[PREVIOUS](pages/image_segmentation_blob_analysis/BINARIZATION.md) [NEXT](pages/image_segmentation_blob_analysis/BINARY_MORPHOLOGY.md)
