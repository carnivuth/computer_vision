## P AS A HOMOGRAPHY

- if the camera is imaging a planar scene we can assume the Z coordinate to be zero so we have:

![](../assets/Pasted%20image%2020231007105935.png)

- `H` is called a homography , it can be seen as a semplification of `P`
- akin to `P`, `H` is known up to an arbitrary scale factor

## THEOREMS

- any two images of a planar scene are related by homography

![](Pasted%20image%2020231021104828.png)

- Any two images taken by a camera rotating about the optical center are related by homography

![](Pasted%20image%2020231021104939.png)

- any two images taken by two different cameras (different `A` matrix so different intrinsic parameters) in a fixed pose are related by homography

![](Pasted%20image%2020231021105132.png)

- if we rotate the camera about the optical center or if we change the `A` matrix the resulting image is related to the first one by homography

![](Pasted%20image%2020231021105558.png)



