---
id: SCALE_INVARIANCE
aliases: []
tags: []
index: 34
---

# SCALE INVARIANCE

A problem for all keypoints detectors is that at different scales some features are detectable as others are not

![](Pasted_image_20240310173759.png)

One of the main concept for dealing with this problem is to compute the keypoints on a set of images down-sampled from the original one and smoothed in order to change the scale of the detected features

If some mathematical properties are satisfied this set of images is called **scale space**

## SCALE SPACE

A Scale-Space is a one-parameter family of images created from the original one so that the **structures at smaller scales are successively suppressed by smoothing operations**. Moreover, one would not wish to create new structures while smoothing the images. In other words, a scale-space should continuously simplify the image **without introducing artifacts**.

A scale space can be obtained by [Gaussian smoothing](GAUSSIAN_FILTER.md) as:
$$
L(x,y,\sigma)= G(x,y,\sigma)\ast I(x,y)
$$

So each level of the Gaussian scale space is obtained by tuning the $\sigma$ parameter (eg smoothing the image with larger Gaussian functions)

The Gaussian scale space does not give ways to find features nor their characteristic scale

[PREVIOUS](pages/local_features/SHI_TOMASI_CORNER_DETECTOR.md) [NEXT](pages/local_features/SCALE_NORMALIZED_LOG.md)
