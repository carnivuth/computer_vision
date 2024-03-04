# IMAGE WARPING

The image points are converted by a pair of functions $f_{u}(u,v),f_{v}(u,v)$ into a new image

![](Pasted%20image%2020240227160817.png)

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

once the lens distortion parameter are computed by [camera calibration](CAMERA%20CALIBRATION.md) it's possible to get back the un-distorted points by a backward warp

![](Pasted%20image%2020240227164313.png)