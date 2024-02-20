[PERSPECTIVE PROJECTION MATRIX](PERSPECTIVE%20PROJECTION.md#PERSPECTIVE%20PROJECTION%20MATRIX) is obtained trough the matrix $A,R,T$ that describes intrinsic parameter of the lens rotation and translation of the camera

camera calibration is the process which estimates this parameter, there are a lot of algorithms that rely on setup a linear system of equations with 3D-2D correspondences in order to obtained the PPM

## ZHANG'S METHOD

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

### ESTIMATING H

this is done exploiting the facts that the calibration pattern is planar so the mapping between 3D and 2D coordinates is a [HOMOGRAPHY](HOMOGRAPHY.md)

![](Pasted%20image%2020231031120750.png)

![](Pasted%20image%2020231031120909.png)

only 2 of the previous equation are linear independent

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


