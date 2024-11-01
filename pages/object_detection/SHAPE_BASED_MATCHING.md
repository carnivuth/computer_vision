---
id: SHAPE_BASED_MATCHING
aliases: []
tags: []
index: 42
---

# SHAPE BASED MATCHING

Shape based matching is a technique that involves matching a specific set of corner points and their gradients to find the model image in the target

![](Pasted_image_20240423154429.png)

First, a set of control points, $P_{k}$, is extracted from the model image by an Edge Detection operation and the gradient direction at each $P_{k}$ is recorded.

Then at each position the gradients of the $P_{k}$ are compared to the $\overset{\sim}P_k$ ones computed from the image in order to compute a similarity function

$$
S(i,j) = \frac{1}{n}\sum_{k=1}^{n} u_k(P_k)\ast \overset{\sim}u_k(\overset{\sim}P_k)
$$
with:

$$
u(P_k) = \frac{1}{\Vert G_k(P_k)\Vert }\ast \begin{bmatrix}I_x(P_k) \\ I_y(P_k)\end{bmatrix}
$$
$$
\overset{\sim}u(\overset{\sim}P_k) = \frac{1}{\Vert \overset{\sim}G_k(\overset{\sim}P_k)\Vert }\ast \begin{bmatrix}I_x(\overset{\sim}P_k) \\ I_y(\overset{\sim}P_k)\end{bmatrix}
$$
$$
,k = 1...n
$$

The upper function is limited in the interval $[-1,1]$ and it peaks when all model points are perfectly aligned with the target computed points, in this case a threshold can be set as the minimum number of model points to detect in the target image

## IMPROVEMENTS

### ROBUSTNESS

in some application is required to be invariant to global inversion of contrast polarity so a simple improvement of the similarity function can be deployed

$$
S(i,j) = \frac{1}{n}\vert \sum_{k=1}^{n} u_k(P_k)\ast \overset{\sim}u_k(\overset{\sim}P_k)\vert
$$
### PERFORMANCES

The computation of the similarity function can be improved once a threshold $S_{min}$ is chosen given the partial similarity function $S_p$ as:

$$
S_p(i,j) = \frac{1}{n}\sum_{k=1}^{p} u_k(P_k)\ast \overset{\sim}u_k(\overset{\sim}P_k)
$$

so the following relation can be established:

$$
S(i,j) \lt \frac{1}{n}( S_p(i,j) + (n -p))
$$

and given the fact that the value of the similarity function need to be lower than the $S_{min}$ threshold

$$
S(i,j)\lt S_{min}
$$

it can be said that

$$
S_p(i,j) \lt n \ast S_{min}  + (p-n)
$$

When the condition is verified the computation of the similarity function can be stopped

## PROPERTIES

- Intensity invariant as the similarity function is based on gradient direction only
- No need of computing the edges on the target image which is a risky procedure
- robustness to occlusion which can be tuned by the $S_{min}$ parameter

[PREVIOUS](pages/object_detection/TEMPLATE_PATTERN_MATCHING.md) [NEXT](pages/object_detection/HOUGH_TRANSFORM.md)
