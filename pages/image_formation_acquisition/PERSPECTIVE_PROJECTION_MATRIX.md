---
id: PERSPECTIVE_PROJECTION_MATRIX
aliases: []
tags: []
index: 9
---

# PERSPECTIVE PROJECTION MATRIX ($PPM$)

The $PPM$ it's the linear representation of the [perspective projection](PERSPECTIVE_PROJECTION.md) in a [perspective space](PERSPECTIVE_SPACE.md)

Let's take the relation between points of the 3D world and the 2D image representation:

$$
u=\frac{f}{z}*x
$$
$$
v=\frac{f}{z}*y
$$

and translate them in a perspective space ($\overset{\sim}m=\begin{bmatrix}  u \\ v \\ 1 \end{bmatrix}$ and $\overset{\sim}M= \begin{bmatrix}x \\ y \\ z \\ 1\end{bmatrix}$), in this representation the relation between points of the real world and the image plane became a **linear transformation** (the **PPM**):

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

we can also use a focal length based metric to express the $PPM$

$$
PPM = \begin{bmatrix}
f & 0 & 0 & 0 \\
0 & f & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix} \rightarrow
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix} =
[I|0]
$$

This form of the $PPM$ show it's basic operation which is to **translate point in a 3D space into a 2D space scaling them by distance**

we can represent it also in matrix notation:

$$
k\overset{\sim}m=\overset{\sim}P\overset{\sim}M \space or \space \overset{\sim}m \simeq \overset{\sim}P\overset{\sim}M
$$

## ADJUSTING THE $PPM$ MODEL

In this form the $PPM$ does not take into account the space relation between the image plane and the 3D world (*rotation and translation*), also [digitizaiton](IMAGE_DIGITIZATION.md) effects are not considered.

### ACCOUNTING FOR [DIGITIZATION](IMAGE_DIGITIZATION.md)

In order to account for digitization the image coordinates are scaled by the pixel dimensions

$$
u = f\frac{x}{z} \rightarrow u = \frac{1}{\Delta u}f\frac{x}{z} = k_{u}f\frac{x}{z} + u_{0}
$$
$$
v = f\frac{y}{z} \rightarrow v = \frac{1}{\Delta v}f\frac{y}{z} = k_{v}f\frac{y}{z} + v_{0}
$$

![](Pasted_image_20240221201431.png)

Based on this equation the $PPM$ becomes as follows

$$
PPM = \begin{bmatrix}
fk_{u} & 0 & u_{0} & 0 \\
0 & fk_{v} & v_{0} & 0 \\
0 & 0 & 1 & 0
\end{bmatrix} =
\begin{bmatrix}
fk_{u} & 0 & u_{0} \\
0 & fk_{v} & v_{0} \\
0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0
\end{bmatrix} =
A[I|0]
$$

the $A$ matrix is called the **intrinsic parameter matrix**, it represents the parameter

### ACCOUNTING FOR ROTATION AND TRANSLATION

In the previous models the camera and the 3D world point where assumed to refer to the same reference frame, in real case application this is impossible and the camera reference frame (*CRF*) and the world reference frame (*WRF*) are related by a rotation $R$ and a translation $T$.

So the relation between a point in the real world $W = \begin{bmatrix} X \\ Y \\ Z \end{bmatrix}$ the correspondent image point $M = \begin{bmatrix} x \\ y\\ z\end{bmatrix}$ can be expressed as follows:

$$
M = RW + T
$$

where $R$ is a $3\times3$ matrix which represents the rotational component and $T$ is a $1\times 3$ vector which represent the translation component.

In the perspective space the relation becomes:

$$
\overset{\sim}W = \begin{bmatrix}
X \\
Y \\
Z \\
1
\end{bmatrix} ,
\overset{\sim}M = \begin{bmatrix}
x \\
y \\
z \\
1
\end{bmatrix} \Rightarrow
\overset{\sim}M =
\begin{bmatrix}
R & T \\
0 & 1 \\
\end{bmatrix} \times \overset{\sim}W = G\overset{\sim}W
$$

The $G$ matrix that represents the translation and rotation between the two reference frame is called **extrinsic parameter matrix**

## FINAL FORM OF A $PPM$

putting together the equation the final form of a $PPM$ matrix looks like follows


$$
k\overset{\sim}m = [A|I]\times
\begin{bmatrix}
R & T \\
0 & 1 \\
\end{bmatrix} \times \overset{\sim}W
$$

So the general form of the $PPM$ can be described as follows


$$
\overset{\sim}P = A\times[I|0]\times G \space or \space \overset{\sim}P = A \times [R | T]
$$

So in conclusion a $PPM$ can be thought as 3 separate components:

- the $A$ matrix which represents **the intrinsic properties of the image sensor**
- the $G$ matrix which represents **the relation between the 2 different reference frames**
- the $[I|0]$ matrix which represents **the perspective projection carried out by the pinhole camera model**

[PREVIOUS](pages/image_formation_acquisition/PERSPECTIVE_SPACE.md) [NEXT](pages/image_formation_acquisition/HOMOGRAPHY.md)
