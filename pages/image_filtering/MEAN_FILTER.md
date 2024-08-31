---
id: MEAN_FILTER
aliases: []
tags: []
---

# MEAN FILTER

It's one of the simplest and fastest way to de-noise an image, it consist to replace the intensity of the pixel with the mean of the neighborhood of a given size.

The kernel of the mean filter can be expressed by a $n\times n$ matrix

$$
\frac{1}{n\times n}\begin{bmatrix}
1 & 1 & .... & 1 \\
1 & ... & .... & ... \\
... & ...  & .... & ... \\
1 & ...  & .... & 1 \\
\end{bmatrix}
$$

The purpose of this filter is often to de-noise the image but it can be used also for removed some unwanted details that could arm the image analysis task.

The implementation can be performed with an incremental approach (box-filtering) to improve the performance

## BOX FILTERING

Let's take the mean across a given point of the image


$$
\mu(i,j)= \frac{\sum_{m=-k}^{m=k}{\sum_{n=-k}^{n=k}{I(i+m,j+n)}}}{(2k+1)^2} = \frac{s(i,j)}{(2k+1)^2}
$$

![](Pasted_image_20240229121850.png)

Now it's true to say that the $s(i,j+1)$ value is obtainable by the precedent value by adding and subtracting differences in the box

$$
\displaylines{
s(i,j+1) = s(i,j) + V^{+}(i,j+1)- V^{-}(i,j+1) \space with \\
\\
V^{+}(i,j+1) =V^{+}(i-1,j+1)+a-b \\
V^{-}(i,j+1) =V^{-}(i-1,j+1)+c-d \\
}
$$

So the new value can be computed as
$$
\displaylines{
s(i,j+1) = s(i,j) + \Delta(i-1,j-1) +a -b -c +d\space with \\
\\
\Delta(i-1,j-1) = V^{+}(i,j+1) - V^{-}(i-1,j+1)\\
}
$$

![](Pasted_image_20240229122932.png)
