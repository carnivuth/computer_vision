---
id: TEMPLATE_PATTERN_MATCHING
aliases: []
tags: []
index: 41
---

# TEMPLATE PATTERN MATCHING

The model image is slid across the target image till a dissimilarity or similarity function is minimized/maximized

![](Pasted_image_20240423114915.png)

## SIMILARITY AND DISSIMILARITY FUNCTIONS

### SUM OF SQUARE DIFFERENCES

Sum of square differences can be deployed as dissimilarity function

$$
SSD(i,j) = \sum_{m=0}^{M-1}{\sum_{m=0}^{M-1}(I(i+m,j+n)-T(m,n))^2}
$$

### SUM OF ABSOLUTE DIFFERENCES

$$
SAD(i,j) = \sum_{m=0}^{M-1}{\sum_{m=0}^{M-1}\vert I(i+m,j+n)-T(m,n)\vert^2}
$$
### NORMALIZED CROSS CORRELATION

This measure is invariant to intensity light changes

$$
NCC(i,j) = \frac{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} I(i+m,j+n)\ast T(m,n)}}{
\sqrt{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} I(i+m,j+n)^2}}
\ast
\sqrt{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} T(m,n)^2}}
} \Rightarrow
$$
$$
NCC(i,j) = \frac{\overset{\sim}I(i,j)\ast T}{\Vert \overset{\sim}I(i,j)\Vert \ast \Vert T\Vert} \Rightarrow
$$
$$
NCC(i,j) = \frac{\Vert \overset{\sim}I(i,j)\Vert \ast \Vert T\Vert cos(\theta)}{\Vert \overset{\sim}I(i,j)\Vert \ast \Vert T\Vert} =
$$
$$
cos(\theta)
$$

The NCC represents the cosine between the vectors $\Vert \overset{\sim}I(i,j)\Vert$ and $\Vert T \Vert$ (*max when the vectors are aligned*)

### ZERO MEAN NORMALIZED CROSS CORRELATION

This is a variant of the [NCC](#NORMALIZED_CROSS_CORRELATION) that takes in to account the mean value of the intensity

$$
NCC(i,j) = \frac{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} (I(i+m,j+n)-\mu(\overset \sim I))\ast (T(m,n)- \mu(T))}}{
\sqrt{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} (I(i+m,j+n)- \mu(\overset \sim I))^2}}
\ast
\sqrt{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} (I(m,n)- \mu(T))^2}}
}
$$

## SAD vs SDD vs NCC vs ZNCC

[ZNCC](#ZERO%20MEAN%20NORMALIZED%20CROSS%20CORRELATION) and [NCC](#NORMALIZED%20CROSS%20CORRELATION) are more robust to intensity changes

![](Pasted_image_20240423153625.png)

## PERFORMANCE

Template matching computation is too much slow for an industrial environment, in order to speed up computation an image pyramid is deployed

In order for this approximation to work levels need to be chosen empirically

[PREVIOUS](pages/object_detection/INSTANCE_LEVEL_OBJECT_DETECTION.md) [NEXT](pages/object_detection/SHAPE_BASED_MATCHING.md)
