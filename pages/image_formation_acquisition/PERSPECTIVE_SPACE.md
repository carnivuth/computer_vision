---
id: PERSPECTIVE_SPACE
aliases:
  - point-to-infinity
tags: 
index: 8
---

# PERSPECTIVE SPACE

In a $R_{3}$ euclidean space such as the 3D world there is no way to represent a point to infinity and parallel lines does not intersect or intersect to infinity.

To address this the **perspective space**  $P_{3}$ is created, inside  this space each $R_{3}$ point is mapped to a class of points defined as follows:

$$
(x,y,z) = (x,y,z,k) \space \forall \space k \in \neq 0
$$

## POINT TO INFINITY REPRESENTATION

In this space points to infinity can be represented, so given a line equation like this:

$$
\begin{bmatrix}
x_{0}  \\
y_{0}  \\
z_{0}
\end{bmatrix} +
\lambda \times
\begin{bmatrix}
a  \\
b  \\
c
\end{bmatrix} =
\begin{bmatrix}
x_{0} + \lambda a  \\
y_{0} + \lambda b  \\
y_{0} + \lambda c
\end{bmatrix}
$$

we can represent a point to infinity by the limit $\lambda \to \infty$ as follows (here it's used the value $1$ for the $k$ coordinate):

$$
lim_{\lambda \to \infty}
\begin{bmatrix}
x_{0}  \\
y_{0}  \\
z_{0}  \\
1
\end{bmatrix} +
\begin{bmatrix}
\lambda a  \\
\lambda b  \\
\lambda c  \\
1
\end{bmatrix} =
\begin{bmatrix}
\frac{x_{0}}{\lambda} + a  \\
\frac{y_{0}}{\lambda} + b  \\
\frac{y_{0}}{\lambda} + c  \\
\frac{1}{\lambda}
\end{bmatrix} =
\begin{bmatrix}
a  \\
b  \\
c  \\
0
\end{bmatrix}
$$

The class $(x,y,z,0)$ represents all of the possible points to infinity. This representation it's not possible in the $R_{3}$

## DEFINITION EXTENSION

The perspective space definition can be extended to a $N$-dimensional space $R_{n}\rightarrow P_{n}$

[PREVIOUS](pages/image_formation_acquisition/STEREO_IMAGE_ACQUISITION.md) [NEXT](pages/image_formation_acquisition/PERSPECTIVE_PROJECTION_MATRIX.md)
