---
id: OBJECT_DETECTION_PIPELINE
aliases: 
tags: 
index: 6
---

# OBJECT DETECTION PIPELINE

```mermaid
flowchart LR

subgraph online phase
direction LR
B[DETECTION\n DESCRIPTION\n AND MATCHING]
C[GHT]
D[LS POSE\n ESTIMATION]
B --> C --> D
end

subgraph offline phase
direction RL
A[MODEL GALLERY]
A --> B & C
end
```

[PREVIOUS](GENERALIZED_HUGH_TRANSFORM.md)
