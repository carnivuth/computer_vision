---
id: SIFT_DESCRIPTOR
aliases: []
tags: []
index: 38
---

# SIFT DESCRIPTOR

This descriptor is based on the gradient direction contribution of a neighborhood of the keypoint, SIFT descriptor is computed as follows

```mermaid
flowchart TD
A[select neighborhood of size 16x16]
B[split in regions of size 4x4]
C[compute gradient orientation histogram for each pixel]
A --> B --> C
```

![](Pasted_image_20240314124330.png)

The descriptor is given by all of the histogram of the regions so the dimension space of a SIFT descriptor is $R^{128}$

The gradient are rotated according to the canonical orientation of the gradient and each pixel is weighted by a Gaussian centered at the keypoint

[PREVIOUS](pages/local_features/CANONICAL_ORIENTATION.md) [NEXT](pages/local_features/MATCHING_PROCESS.md)
