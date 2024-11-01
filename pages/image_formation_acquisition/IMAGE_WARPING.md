---
id: IMAGE_WARPING
aliases: []
tags: []
index: 14
---

# IMAGE WARPING

The image points are converted by a pair of functions $f_{u}(u,v),f_{v}(u,v)$ into a new image

![](Pasted_image_20240227160817.png)

$$
\begin{cases}
u^{'} = f_{u}(u,v) \\
v^{'} = f_{v}(u,v)
\end{cases}
$$

It's also possible to invert warping

$$
\begin{cases}
u = g_{u}(u^{'},v^{'}) \\
v = g_{v}(u^{'},v^{'})
\end{cases} \space \forall \space (u^{'},v^{'}): I^{'}(u^{'},v^{'}) = I(g_{u}(u^{'},v^{'}),g_{v}(u^{'},v^{'}))
$$

## WARPING TO COMPENSATE LENS DISTORTION

once the lens distortion parameter are computed by [camera calibration](CAMERA_CALIBRATION.md) it's possible to get back the un-distorted points by a backward warp

![](Pasted_image_20240227164313.png)

[PREVIOUS](pages/image_formation_acquisition/STEREO_CAMERA_CALIBRATION.md) [NEXT](pages/image_filtering/IMAGE_FILTERS.md)
