# TEMPLATE PATTERN MATCHING

The model image is slid across the target image till a dissimilarity or dissimilarity function is minimized/maximized 

![](Pasted%20image%2020240423114915.png)

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
\displaylines{
NCC(i,j) = \frac{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} I(i+m,j+n)\ast T(m,n)}}{
\sqrt{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} I(i+m,j+n)^2}}
\ast
\sqrt{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} I(m,n)^2}}
} \Rightarrow\\
NCC(i,j) = \frac{\overset{\sim}I(i,j)\ast T}{\Vert \overset{\sim}I(i,j)\Vert \ast \Vert T\Vert} \Rightarrow\\
NCC(i,j) = \frac{\Vert \overset{\sim}I(i,j)\Vert \ast \Vert T\Vert cos(\theta)}{\Vert \overset{\sim}I(i,j)\Vert \ast \Vert T\Vert} = \\
cos(\theta)
} 
$$

### ZERO MEAN NORMALIZED CROSS CORRELATION

This is a variant of the [NCC](#NORMALIZED%20CROSS%20CORRELATION) that takes in to account the mean value of the intensity

$$
NCC(i,j) = \frac{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} (I(i+m,j+n)-\mu(\overset \sim I))\ast (T(m,n)- \mu(T))}}{
\sqrt{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} (I(i+m,j+n)- \mu(\overset \sim I))^2}}
\ast
\sqrt{\sum_{m=0}^{M-1}{\sum_{m=0}^{M-1} (I(m,n)- \mu(T))^2}}
} 
$$

![](Pasted%20image%2020240423153625.png)

## PERFORMANCE

Template matching computation is too much slow for an industrial environment, in order to speed up computation an image pyramid is deployed

In order for this approximation to work levels need to be chosen empirically 