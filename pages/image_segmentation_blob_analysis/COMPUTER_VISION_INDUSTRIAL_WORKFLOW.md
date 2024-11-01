---
id: COMPUTER_VISION_INDUSTRIAL_WORKFLOW
aliases: []
tags: []
index: 21
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

[PREVIOUS](pages/image_filtering/NON-LOCAL_MEAN_FILTER.md) [NEXT](pages/image_segmentation_blob_analysis/BINARIZATION.md)
