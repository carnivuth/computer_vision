# ZHANG'S METHOD

The zhang's method relies in getting a series of n images of a chessboard patterns where are known

- $n,m$ number of internal corners of the pattern, different in the 2 directions
- $k$ size of squares of the pattern

from this images the goal is to extract the $PPM$ matrix parameters:

```mermaid
flowchart TD

	A[Acquire n images of a planar pattern \n with m internal corners];
	B[For each such image compute an initial \n guess for homography Hi];
	C[Refine each Hi by minimizing \n the reprojection error];
	D[Get an initial guess for A given the homographies Hi];
	E[Given A and Hi , get an initial guess for Ri and T];
	F[Compute an initial guess for lens distortion parameters k];
	G[Refine all parameters A, Ri, Ti, k by minimizing the reprojection error];
	A-->B
	B-->C
	C-->D
	D-->E
	E-->F
	F-->G
```

## SETTING A WRF

so given a set of images the WRF is taken with origin at the top-left corner of the patter(that could easily be detected)

![](Pasted%20image%2020240222173836.png)

Given this setup with the **WRF** parallel to the $Z$ axis we can consider the control point to have $z=0$ so the relation with the image points **became a [HOMOGRAPHY](HOMOGRAPHY.md)**

## DISCOVERING $H$

so given a pattern with $m$ corners it's possible to write $m$ sets of 3 linear equations where 2D and 3D coordinates are known so we can compute the $H$ matrix

$$
k\overset{\sim}m = H\overset{\sim}w_{'}\Rightarrow \overset{\sim}m\times H\overset{\sim}w_{'}\Rightarrow
\begin{bmatrix}
vh_{3}^T\overset{\sim}w_{'}- h_{2}^{T}\overset{\sim}w_{'}\\
h_{1}^T\overset{\sim}w_{'}- uh_{3}^{T}\overset{\sim}w_{'}\\
uh_{2}^T\overset{\sim}w_{'}- vh_{1}^{T}\overset{\sim}w_{'} 
\end{bmatrix}=0
$$

So extracting the $h$ vector from the system:

$$
\begin{bmatrix}
0^T & -\overset{\sim}w^{'T} & v\overset{\sim}w^{'T}\\
 \overset{\sim}w^{'T} &0^T & -u\overset{\sim}w^{'T}\\
 -v\overset{\sim}w^{'T}  & u\overset{\sim}w^{'T}&0^T \\
\end{bmatrix}\times
\begin{bmatrix}
h_{1}\\
h_{2}\\
h_{3}\\
\end{bmatrix}=Ah=0
$$

From this system in 3 equations in 9 unknowns only 2 equation are linear independent, the 3 equation is discarded.
For each image a similar system of equations is built in order to minimize the algebraic error due to the norm of $Ah$


--------------------------------


### ESTIMATING H
now we can use singolar value decomposition to estimate homography H

![](Pasted%20image%2020231031121132.png)

### NON LINEAR REFINEMENT

with the previous estimation of H we can minimize the reprojection error with the Levenberg-Marquardt (LM) algorithm

![](Pasted%20image%2020231031122648.png)

### ESTIMATING INTRINSIC PARAMETERS

we can say that the previous homography and the PPM are related as follows

![](Pasted%20image%2020231031123135.png)

because R is orthonormal we can  say that:

![](Pasted%20image%2020231031123453.png)

so if `B=A^-T*A^-1` we can say that

![](Pasted%20image%2020231031123632.png)

therefore any calibration image provides 2 linear independent equations so we can estimate the A matrix with minimum 3 images

### ESTIMATING EXTRINSIC PARAMETERS

with H and A we can estimate the R and T matrix as follow

![](Pasted%20image%2020231031134750.png)

![](Pasted%20image%2020231031135036.png)

and then r3 can be derived form r1 and r2 exploiting orthonormality

![](Pasted%20image%2020231031135134.png)


