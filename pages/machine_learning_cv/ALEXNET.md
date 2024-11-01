---
id: ALEXNET
aliases: []
tags: []
index: 51
---

# ALEXNET

[CNN](CONVOLUTIONAL_NEURAL_NETWORKS.md) that won the [ILSVRC](https://www.image-net.org/challenges/LSVRC/2012/)2012, powerfull network trained on 2 gpus

![](Pasted%20image%2020241001102840.png)

## STRIDE PARAMETER

first conv layer has a [stride](CONVOLUTIONAL_NEURAL_NETWORKS.md#STRIDED%20CONVOLUTION) of 4 to reduce the spatial dimension of input e reduce the computational costs, other layers as a stride of 1

## [POOLING LAYERS](CONVOLUTIONAL_NEURAL_NETWORKS.md#POOLING%20LAYERS)

the first 2 layers of the network are intervaled from a max pooling layer

## IMPLEMENTATION OF NON LINEARITY

All layers (*Conv and FC*) deploy [ReLU](DEEP_LEARNING_AND_NEURAL_NETWORKS.md#ACTIVATION%20FUNCTION), non-linearities which yield faster training compared to saturating non-linearities

## [FULLY CONNECTED LAYERS](DEEP_LEARNING_AND_NEURAL_NETWORKS.md#FULLY%20CONNECTED%20LAYERS) SETUP

Last FC layer has 1000 units (as many as the [ILSVRC](https://www.image-net.org/challenges/LSVRC/2012/) classes), the penultimate FC layer is the feature/representation layer and has a cardinality of $4096$.

## CHARACTERISTICS

**Local Response Normalization** (*after conv1 and conv2*): **activations are normalized** by the sum of those at the same spatial position in a few ($n=5$) adjacent channels (mimics lateral inhibition in real neurons).


in the FC6 FC7 layers **Dropout** is performed which means that  at training time the output of each unit is set to zero with probability 0.5. This forces units to learn more
robust features since none of them can rely on the presence of particular other ones.

## TRAINING PHASE

Training was performed using random-cropping of $224\times 224$ patches (*and their* *horizontal reflections*) from the $256\times 256$ RGB input images and colour jittering (*massive [data augmentation](MACHINE_LEARNING_IN_COMPUTER_VISION.md#DATA%20AUGMENTATION)*).

At test time, averaging predictions (*i.e. softmax*) across 10 patches (*central + 4 corner alongside their horizontal reflections*).

| HYPERPARAMETER        | VALUE                                                                           |
| --------------------- | ------------------------------------------------------------------------------- |
| Optimizer             | SGD with $B=128$                                                                |
| Epochs                | $90$                                                                            |
| Learning Rate         | $0.01$, divided 3 times by 10 when the validation error stopped to improve      |
| Weight Decay          | $0.0005$                                                                        |
| Momentum              | $0.9$                                                                           |
| Data Augmentation     | Colour Jittering, Random Crop,Horizontal Flip                                   |
| InitializationWeights | $~N(0,0.01)$, Biases: 1 (*conv2,conv4,conv5, fc6,fc7,fc8*) or 0 (*conv1,conv3*) |
| Normalization         | Centering (Subtraction of the Mean RGB colour in the training set)              |

[PREVIOUS](pages/machine_learning_cv/LENET.md) [NEXT](pages/machine_learning_cv/VGG.md)
