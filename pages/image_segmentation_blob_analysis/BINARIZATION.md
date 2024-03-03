# BINARIZATION
## GRAY LEVEL HISTOGRAM

histogram of the number of pixel for each light intensity defined as:

$$
p =\begin{bmatrix}u \\ v\end{bmatrix}, \space 
\forall \space p \in I \space H[I(p)]++\\
$$

![](Pasted%20image%2020240302130200.png)

This histogram does not contain spatial information so a **different arranged set of the same pixels produces the same histogram** 

## BINARIZATION BY INTENSITY TRHESHOLDING

Binarization can be computed by simply selected a threshold $T$ and splitting the points $I(p) \lt T | I(p) \gt T$  

### THRESHOLD SELECTION

In real case scenarios the light stability of the image could not be guaranteed so there is the need to select dynamically the threshold

#### $T=\mu$

This is the simplest threshold selction method, it works only if points are evenly distributed in the histogram

![](Pasted%20image%2020240302144849.png)

#### PEAKS METHOD

This method set T as the minimum of the function between the 2 main peaks

$$
T = argmin(h(i); i \in [i_1,i_2])
$$

![](Pasted%20image%2020240302145905.png)

This method need the histogram smoothing to avoid been trapped in local minimums

#### OTSU'S ALGORITHM

The idea behind this method is to divide the histogram into 2 main regions with the aim of **minimizing the within group variance**

so given the following definitions:
$i =1...L$ -> gray levels
$N$ -> Number of pixels
$h(i)$ -> entry of the histogram
$p(i)= h(i)/N$ -> probability of gray level $i$ 

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
\displaylines{
with: \\
q_1(t)= \sum_{i=1}^{t}p(i), \space \space q_2(t)= \sum_{i=t+1}^{L}p(i),
}
$$

The within group variance is defined as the weighted sum of the variance of the 2 regions

$$
\sigma^2_W(t) = \sigma_1^2*q_1(t) + \sigma_2^2*q_2(t)
$$

The algorithm aims to minimize this value with the assumption that the regions created from best $T$ will have all points concentrated in a relative small region (eg little variance)

## ADAPTIVE THRESHOLDING

Any global thresholding method rely on the assumption of uniform lighting across the scene, if this assumption is violated  it's necessary to compute the threshold in function of the spatial variation

The idea is to **compute the threshold at each point of the image** based on a neighborhood of pixels (threshold become a function of space $T(x,y)$), This introduce the problem of neighborhood dimension cause a too small one could lack of foreground pixels 

## COLOR BASED SEGMENTATION

So given a pixel $p$, the color intensity is defined as $I(p) = \begin{bmatrix}I_r(p)\\ I_g(p)\\ I_b(p)\\ \end{bmatrix}$ The segmentation can be done by calculating the distance from each color vector from a reference background color $\mu$

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

![](Pasted%20image%2020240303160809.png)

### MAHALANOBIS DISTANCE

A more precise way of making color based segmentation is to consider the covariance also with means, the covariance matrix is obtained in the training phase as follows

$$
\Sigma = \begin{bmatrix}
\sigma^2_{rr} &&\sigma^2_{rg} &&\sigma^2_{rb} \\
\sigma^2_{gr} &&\sigma^2_{gg} &&\sigma^2_{gb} \\
\sigma^2_{br} &&\sigma^2_{bg} &&\sigma^2_{bb} \\
\end{bmatrix} \space with
$$
$$
\displaylines{
\sigma^2_{ij} = \frac{1}{N}\sum_{k=1}^{N}(I_i(p_k) - \mu_j)(I_j(p_k) - \mu_j) \\
i,j \in \{r,g,b\}
}
$$
The new distance measure is given by the inclusion of the covariance matrix in the euclidean distance

$$
d_M(I(p),\mu) = \sqrt{(I(p)-\mu)^T \Sigma^{-1}(I(p)-\mu)} 
$$

The mahalanobis distance weights the differences between the color components unequally (inversely proportional to the learned variances ), This as the effect of lower the consideration of sparse components 

