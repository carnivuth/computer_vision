---
id: STEREO_IMAGE_ACQUISITION
aliases: []
tags: []
index: 7
---

# STEREO IMAGE ACQUISITION

In order to address the loss of depth information, given 2 images of a 3D scene and correspondence in points the depth of a point can be recovered using triangulation.

so given the following model:

![](Pasted_image_20240221203033.png)

The relation between the 2 images is only an horizontal translation

$$
x_{l} - x_{r} = b
$$
$$
y_{l} = y_{r}= y
$$
$$
z_{l} = z_{r} = z
$$

The [perspective projection](PERSPECTIVE_PROJECTION.md) model the relation between image points and 3D ones can be described as follows:

$$
u_{L} = x_{L}*\frac{f}{z}
$$
$$
u_{R} = x_{R}*\frac{f}{z}
$$
computing the difference:

$$
u_{L} – u_{R} = b*\frac{f}{z}
$$

It's true to say that $u_{L} – u_{R}$ can be computed from image measurements

$$
u_{L} – u_{R} = d
$$

where $d$ is called **disparity**. than $z$ can be computed

$$
d = b*\frac{f}{z} \Rightarrow z = b*\frac{f}{d}
$$

## THE PROBLEM OF FINDING CORRESPONDENCES

In order to apply this model the **correspondences between the points of the 2 images need to be computed**, this is not an easy task nether computationally or conceptually, also the models **relays on the 2 images being horizontally aligned**, and to obtained this some computation is needed.

fortunately, the search space for correspondences is always 1 dimensional as 2 points share always the same $y$ coordinate.
To address the horizontal alignment problem a [homography](HOMOGRAPHY.md) called **rectification** is used on the images to warp them and obtain something horizontally aligned.

[PREVIOUS](pages/image_formation_acquisition/LENS_DISTORTION.md) [NEXT](pages/image_formation_acquisition/PERSPECTIVE_SPACE.md)
