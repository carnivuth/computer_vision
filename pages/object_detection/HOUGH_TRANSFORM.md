---
id: HOUGH_TRANSFORM
aliases: []
tags: []
index: 43
---

# HOUGH TRANSFORM

The Hough Transform can detect analytical shapes in an image such as line, circles or ellipses and is based on the concept of mapping the input data in a parameter space called **HOUGH SPACE**

## CONCEPT

The basic idea relies on mapping point of the input image in the parameter space which is created by using the points coordinates as fixed coefficients of the equation of a line, so given the line equation

$$
y -\hat{m}x -\hat{c} = 0
$$

The mapping is expressed by setting the $y,x$ values to the image point.

Accordingly if we compute the lines in the parameter space of 2 image point the intersection represents the line that intersects those 2 points in the image

$$
\begin{cases}
y_1 -mx_1 -c = 0 \\
y_2 -mx_2 -c = 0 \\
\end{cases} \Rightarrow
\begin{cases}
m  = \frac{ y_2 - y-1}{x_2 -x_1} \\
c = \frac{ x_2y_1 - y_2x_1}{x_2 -x_1} \\
\end{cases}
$$

![](Pasted_image_20240427142752.png)

More in general with $n$ image points we get the $n(n-1)/2$  points that represents all the lines between the points

### WHAT IF POINTS ARE IN THE SAME LINE?

In the case of **image points that are in the same line** the projections in the parameter space  will met at the same point

![](Pasted_image_20240427155224.png)

So the problem of finding a line in the image can be translated in **finding the intersection of lines in the parameter space**

So given an analytic description of a shape the HT maps the image point (usually edge points ) so to create curves in the parameter space. **The intersection in the parameter space means that there is an instance of the shape in the image**

So the problem become **finding parameter space points in which many curves intersects**

### IMPLEMENTATION

The implementation relies on a discrete representation of the parameter space as an **accumulator array** (**AA**) in which the curves are drawn in order to increment the values in the bins of the array, **an high number in one of the bins means that there is a high number of line passing trough that point**

![](Pasted_image_20240427162503.png)

In order to compute non analytical shapes the [GENERALIZED HUGH TRANSFORM](GENERALIZED_HUGH_TRANSFORM.md) is deployed

[PREVIOUS](pages/object_detection/SHAPE_BASED_MATCHING.md) [NEXT](pages/object_detection/GENERALIZED_HUGH_TRANSFORM.md)
