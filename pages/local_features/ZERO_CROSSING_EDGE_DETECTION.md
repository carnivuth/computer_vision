---
id: ZERO_CROSSING_EDGE_DETECTION
aliases: []
tags: []
index: 30
---

# ZERO CROSSING EDGE DETECTION

Edge detection can also be done by detecting the zero crossing point of the second derivative

![](Pasted_image_20240309153449.png)

The second derivative can be computed by the Hessian matrix as $n^THm$ with

$$
n = \frac{\nabla I(x,y)}{\Vert \nabla I(x,y) \Vert}, \space \space and \space \space
H = \begin{bmatrix}
\frac{\delta^2 I(x,y)}{\delta x^2} & \frac{\delta^2 I(x,y)}{\delta x \delta y} \\
\frac{\delta^2 I(x,y)}{\delta y \delta x} & \frac{\delta^2 I(x,y)}{\delta y^2 } \\
\end{bmatrix}
$$
This implementation is too computational expensive so another solution is to use the Laplacian

$$
\nabla^2I(x,y) = \frac{\delta^2 I(x,y)}{\delta x^2} + \frac{\delta^2 I(x,y)}{\delta y^2} = I_{xx} + I_{yy}
$$

This solution needs to filter out the noise, this is done through convolution with Gaussian function

$$\overset{\sim}I(x,y) = I(x,y)\ast G(x,y)$$

[PREVIOUS](pages/local_features/CANNY_EDGE_DETECTOR.md) [NEXT](pages/local_features/MORAVEC_CORNER_DETECTOR.md)
