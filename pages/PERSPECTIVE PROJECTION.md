![](../assets/Pasted%20image%2020231005122554.png)

- the equation to map a 3D point to a 2D coordinate are as follow

```
u=f/z*x
v=f/z*y
```

## PROJECTIVE SPACE P^3

- in the 3D euclidean space **we can't rappresent a point that is infinitly distant from the image** 
- paralel lines do not intersect

### PROJECTIVE COORDINATES

 - a point is rappresented by a quadruplet of number which
 `(x y z 1)=(2x 2y 2z 2)=(kx ky kz k) for each k !=0`
 - so a point has a class of rappresentation  vectors 
 
 ```
 
 M = M0 + lD = [x0,y0,z0] + l[a,b,c] = [x0+la,y0+lb,z0+lc]
 
 in a P^3 space rappresentation it becomes

 ~M = [M,1] = [x0/l+a,y0/l+b,z0/l+c,1/l]

for l to infinity

 ~M = [a,b,c,0]
```

## PERSPECTIVE PROJECTION IN PROJECTIVE COORDINATES

- in the projective coordinates the image reference system and the real world reference system become as follows

```
~m = [u,v,1]
~M = [z,y,z,1]
```

- and perspective projection becomes a linear transformation

```
[u,v,1] = [f*x/z,f*y/z,1] = km = PM
```

![](../assets/Pasted%20image%2020231005125827.png)

## PERSPECTIVE PROJECTION MATRIX

- the matrix that describes the linear transformation is called perspective projection matrix (PPM) and it represent the geometric camera model

- if we represent it in `f` focal lenght units we get

![](../assets/Pasted%20image%2020231007102728.png)

- this form explains what is the core of the operations of perspective projection which is just to scale `x and y` coordinates by `f`  and the distance from the image plane `z`

- to get a useful camera model we need to account the [IMAGE DIGITALIZATION](IMAGE%20DIGITALIZATION.md) and the rigid motion (rotation and translation) between the camera reference frame and the real world reference frame

![](../assets/Pasted%20image%2020231007103848.png)

- to account for digitization can be accounted by including the scaling factor due to quantization along the 2 axis

![](../assets/Pasted%20image%2020231007104143.png)

```
u = f/z*x = 1/deltau*f/z*x = ku*f/z*x+u0 
v = f/z*y = 1/deltav*f/z*y = kv*f/z*y+v0 
```

- so the PPM becomes

![](../assets/Pasted%20image%2020231007104606.png)

- where matrix `A` is the model of the image sensing device called **intrinsic parameter matrix**

## RIGID MOTION BETWEEN CRF AND WRF

- the 2 reference systems are usually related by translation (`(3*1) vector T`) and rotation (`(3*3) matrix M`)

![](../assets/Pasted%20image%2020231007105154.png)

![](../assets/Pasted%20image%2020231007105216.png)

- matrix G is called the extrinsic parameter matrix

- so we can say that the general form of the PPM is obtained by encoding the camera position in matrix G the perspective projection of a pinhole camera into a PPM and the intrinsic characteristics  of the sensing device into A


