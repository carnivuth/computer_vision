---
id: MATCHING_PROCESS
aliases: []
tags: []
---

# MATCHING PROCESS

In this phase keypoint descriptor are compared in order to find correspondences, this is the **find the nearest neighbor** problem

*Given a set $S$ of points $p_i$ in a metric space $M$ and a query point $q \in M$, find the $p_i$ closest to $q$*

So in this iteration of the problem the keypoints  computed on a target image T are the query point and the $S$ set of point is given by the keypoint learned from a set of training images, the metric space $M$ is the space of the [sift descriptor](SIFT_DESCRIPTOR.md) with a distance metric (usually euclidean distance)
