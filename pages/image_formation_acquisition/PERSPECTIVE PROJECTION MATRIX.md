# PERSPECTIVE PROJECTION MATRIX (PPM)

The **PPM** it's the linear representation of the [perspective projection](PERSPECTIVE%20PROJECTION.md) in a [perspective space](PERSPECTIVE%20SPACE.md)

Let's take the relation between points of the 3D world and the 2D image representation:

$$
u=\frac{f}{z}*x
$$
$$
v=\frac{f}{z}*y
$$

and translate them in a perspective space, so given the vectors $\overset{\sim}m= [u,v,1]$ and $\overset{\sim}M= [x,y,z,1]$ the perspective projection matrix it's obtained as follows

$$
\begin{bmatrix}
u \\
v \\
1
\end{bmatrix} =
\begin{bmatrix}
f\frac{x}{z} \\
f\frac{y}{z} \\
1
\end{bmatrix} =
\begin{bmatrix}
f & 0 & 0 & 0 \\
0 & f & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z \\
1
\end{bmatrix}
$$

$$
PPM =\begin{bmatrix}
f & 0 & 0 & 0 \\
0 & f & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix} 

$$

we can also use a focal length based metric to express the **PPM**

$$
PPM = \begin{bmatrix}
f & 0 & 0 & 0 \\
0 & f & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix} =
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix} =
[I|0]
$$

This form of the PPM show it's basic operation which is to **translate point in a 3D space into a 2D space scaling them by distance**

we can represent it also in matrix notation:

$$
k\overset{\sim}m=\overset{\sim}P\overset{\sim}M \space or \space \overset{\sim}m \simeq \overset{\sim}P\overset{\sim}M 
$$

## ADJUSTING THE PPM MODEL

In this form the PPM does not take into account the space relation between the image plane and the 3D world (*rotation and translation*), also [digitizaiton](IMAGE%20DIGITIZATION.md) effects are not considered.


