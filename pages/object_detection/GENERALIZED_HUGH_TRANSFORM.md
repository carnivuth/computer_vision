---
id: GENERALIZED_HUGH_TRANSFORM
aliases: []
tags: ["ght process","sift descriptor","object detection"]
index: 44
---

# Generalized Hough transform

The Generalized Hough transform (**GHT**) is a generalization aimed to apply **[HT](HOUGH_TRANSFORM.md)** to non analytical shapes.

```mermaid
flowchart LR
subgraph online phase
f[detect edges in the target image]
g[compute gradient direction]
h[quantize the gradient to index the R table]
i[compute the position of the reference point]
j[ cast a vote in the accumulator array]

f --> g --> h --> i --> j --repeat for all r vectors\n in the indexed row--> i
j --repeat for all edges--> g
end

subgraph offline phase

a[detect edeges in the model image]
b[choose a reference point e.g. the baricentre of the shape]
c[compute vector R for each edge point]
d[compute gradient direction]
e[store R in a table indexed by the quantized gradient direction]

a --> b --> c --> d --> e --repeat for all edges--> c
end
```

![](Pasted_image_20240427172424.png)

## GHT with local invariant features

The most popular computer vision pipeline relies on combining GHT with local invariant features such as the [SIFT DESCRIPTOR](SIFT_DESCRIPTOR.md). In this pipeline Local invariant features are used instead of edges.

### GHT: offline phase

Detect keypoints (e.g. [DOG](DOG_DETECTOR.md)) and compute descriptors (e.g. [SIFT](SIFT_DESCRIPTOR.md)) in the model image:

$$
F = \{F_1,F_2,...,F_n\}
$$
$$
F_i = (P_i,D_i,\phi_i,S_i)
$$

Choose a reference point (eg the [barycentre](BLOB_ANALYSIS.md#BARYCENTRE))

$$
P_C = \frac{1}{N}\sum_{i=1}^{N}P_i
$$
Compute the joining vectors between the features and the reference point:

$$
\forall F_i \in F \rightarrow V_i= P_C -P_i
$$

The Star Model consist of the features and their joining vectors (no need of the R Table):

$$
F_i = (P_i,D_i,\phi_i,S_i,V_i)
$$

### GHT: online phase

Detect [keypoints](FINDING_CORRESPONDENCES.md#KEYPOINTS) on the target image and compute descriptors :

$$
\overset{\sim}F = \{\overset{\sim}F_1,\overset{\sim}F_2,...,\overset{\sim}F_n\}
$$
$$
\overset{\sim}F_i = (\overset{\sim}P_i,\overset{\sim}D_i,\overset{\sim}\phi_i,\overset{\sim}S_i)
$$

Match descriptor between target and model image

$$
\forall \overset{\sim}F_i \in \overset{\sim}F \rightarrow \overset{\sim}D_j = D_j
$$

for each keypoint on the target image that matches his descriptor with a keypoint in the model image compute the reference point and cast a vote in the accumulator array

$$
\overset{\sim}P_{C_j} = \overset{\sim}P_j + \overset{\sim}V_j
$$
$$
A[\overset{\sim}P_{C_j} ] ++
$$
## 2D accumulator array issues

A 2D accumulator array is not sufficient to account for rotation and scale, the solution is to use a 4D accumulator array in order to account for scale and rotation

![](Pasted_image_20240428143913.png)

[PREVIOUS](pages/object_detection/HOUGH_TRANSFORM.md) [NEXT](pages/object_detection/OBJECT_DETECTION_PIPELINE.md)
