---
id: BILATERAL_FILTER
aliases: 
tags: 
index: 19
---

# BILATERAL FILTER

This filter aims to reduce the Gaussian noise without blurring the image, the filter is inversely proportional to distance  and proportional with the pixel intensity

$$
O(p) = \sum_{q\in S}H(p,q)I_{q} \space where
$$

$$
H(p,q) = \frac{1}{W(p)}G_{\sigma_{S}}(d_S(p,q))G_{\sigma_r}(d_r(I_p,I_q))
$$
- $d_S(p,q)= \Vert  p -q \Vert_2= \sqrt{(u_p-u_q)^2 + (v_p+v_q)^2}$ -> Spatial distance
- $d_r(p,q)= \vert  p -q \vert$ -> Range (intensity) distance
- $W(p)= \sum_{q\in S}{G_{\sigma_{S}}(d_S(p,q))G_{\sigma_r}(d_r(I_p,I_q))}$ -> normalization factor

This filter takes into account the bi-dimensional distance and the difference in pixel intensity of the points in the $S$ neighborhood

![](Pasted_image_20240302110646.png)

![](Pasted_image_20240302112042.png)

As shown in the image this filter is good in the edges cause it does not introduce blur in the image cause it takes into account range distance

[PREVIOUS](pages/image_filtering/MEDIAN_FILTER.md) [NEXT](pages/image_filtering/NON-LOCAL_MEAN_FILTER.md)
