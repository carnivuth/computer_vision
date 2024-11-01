---
id: DOG_DETECTOR
aliases: []
tags: []
index: 36
---
# DOG DETECTOR

This detector relies on difference of Gaussian (DOG) in order to find keypoints

$$
DoG(x,y,\sigma) = (G(x,y,k\sigma) - G(x,y,\sigma))\ast I(x,y) = L(x,y,k\sigma) -L(x,y,\sigma)
$$

This approach is more computational efficient of computing [LOG](SCALE_NORMALIZED_LOG.md), and it's a good approximation of the results

![](Pasted_image_20240314102352.png)

## DOG COMPUTING

Computation of dog is done by down-sampling and [gaussian smoothing](GAUSSIAN_FILTER.md) the input image in order to obtain the scale space and then by computing differences between adjacent scale levels

![](Pasted_image_20240314103452.png)

The next scale level is computed by taking half of the columns and rows and computing the same filter (performance optimization)

a point is detected as a feature if it's DoG is an extreme of its 26 neighbors

![](Pasted_image_20240314103712.png)

## DOG IMPROVEMENTS WITH FILTERS

In order to localize keypoints in an accurate way and remove unstable point [filter procedures](IMAGE_FILTERS.md) are needed

[PREVIOUS](pages/local_features/SCALE_NORMALIZED_LOG.md) [NEXT](pages/local_features/CANONICAL_ORIENTATION.md)
