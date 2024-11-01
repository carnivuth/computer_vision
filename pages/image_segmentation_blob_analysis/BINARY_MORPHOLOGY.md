---
id: BINARY_MORPHOLOGY
aliases: []
tags: []
index: 24
---

# BINARY MORPHOLOGY

The binary morphology operators take as input a [binarized](BINARIZATION.md) image and make improvement before the labeling phase

The idea is to slide a small kernel called structuring element

## DILATION

The output image is obtained by sliding the kernel on each black element

![](Pasted_image_20240303171944.png)
## EROSION

The output image is obtained by sliding the kernel on the all image leaving only the black points that contain the kernel

![](Pasted_image_20240303172045.png)

## OPENING AND CLOSING

Erosion followed by dilation is called opening

$$
A \circ B = (A \ominus B) \oplus B
$$
Dilation followed by erosion is called closing

$$
A \bullet B = (A \oplus B) \ominus B
$$

[PREVIOUS](pages/image_segmentation_blob_analysis/COLOR_BASED_SEGMENTATION.md) [NEXT](pages/image_segmentation_blob_analysis/COMPONENTS_LABELING.md)
