---
id: MEDIAN_FILTER
aliases: 
tags: 
index: 5
---

# MEDIAN FILTER

Median filter is a non linear filter which replace the intensity value with the median of the neighborhood.
Note that this is not a liner filter because

$$
median(A(x)+B(x)) \neq median(A(x)) + median(B(x))
$$

So with a neighborhood like this:

$$
\begin{bmatrix}
124 & 126 &127 \\
120 & 150 &125 \\
115 & 119 &123 \\
\end{bmatrix}
$$

The median value is the value in the middle of the range ($124$)

The median filter is good at removing impulse noise from an image as the noise point frequently fall into the higher or lower range

![](Pasted_image_20240229174319.png)
[PREVIOUS](GAUSSIAN_FILTER.md) [NEXT](BILATERAL_FILTER.md)
