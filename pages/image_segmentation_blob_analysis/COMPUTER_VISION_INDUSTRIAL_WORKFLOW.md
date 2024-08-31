---
id: COMPUTER_VISION_INDUSTRIAL_WORKFLOW
aliases: []
tags: []
---

# COMPUTER VISION INDUSTRIAL WORKFLOW

Computer vision processes in industrial environment follow this schema

```mermaid
flowchart TD
A[Grab image]
B[ROI]
subgraph segmentation
C[Binarization]
D[Labeling]
end
E[Blob analysis]
A --> B
B --> C
C --> D
D --> E
```

## BINARIZATION

It's the process of separating the foreground points from the background point in order to detect blobs in the labeling phase. This process is based on the fact that background points are usually darker then the foreground ones

## LABELING

In this step objects are detected from the binarized image

## BLOB ANALYSIS
