---
id: PERSPECTIVE_PROJECTION
aliases: 
tags: 
index: 1
---

# PERSPECTIVE PROJECTION

The model that rules the conversion from a 3D scene  to an image is called perspective projection, it's based on the [pinhole camera model](https://en.wikipedia.org/wiki/Pinhole_camera_model) and it goes like follow:

![](Pasted_image_20231005122554.png)

from this model are derived the equation to map a 3D point to a 2D coordinate are as follow

$$
u=\frac{f}{z}*x
$$
$$
v=\frac{f}{z}*y
$$

It's important to notice that this equations are **inversely proportional** in respect to the depth of the point in the 3D world

## INFORMATION LOSS

This set of equation is not bidirectional as we are representing a 3D world with a 2D image, so the information loss is inevitable, in the process the following informations are lost:

- ratios of lenghts (*unless they are paralel to the image plane*)
- parallelism between line (*unless they are paralel to the image plane*)
- depth of a point

In order to recover the depth information [stereo image acquisition](STEREO_IMAGE_ACQUISITION.md) can be used

## VANISHING POINTS

The vanishing point of a 3D line is the image of the point at infinity of the line (i.e. the image
of the point on the line which is infinitely distant from the optical center).

![](Pasted_image_20240221202839.png)

with such definition all 3D lines in the image will **share the same vanishing point**

in a real case application this model alone it's not sufficient, there are [real camera parameters](CAMERA_PARAMETERS.md) and  [lens effects](LENS.md) to take into account. In order to apply some computation to an image [digitization](IMAGE_DIGITIZATION.md) is also needed.

 [NEXT](pages/image_formation_acquisition/CAMERA_PARAMETERS.md)
