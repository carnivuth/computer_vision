# CONVOLUTIONAL NEURAL NETWORKS (CNN)

## LIMITS OF FULLY CONNECTED LAYERS 

Let's assume that the feature detection layer need to compute some kind of local features (e.g. edges or keypoints) so the dimension of the $W$ array becomes:

$$
size(W_l)= (3\times M \times N) \times (M \times N)
$$

so the network's layer dimensions increase exponentially with the image dimensions and becomes computationally impossible

## CONVOLUTION TO THE RESCUE

Similarly to what is done in classical computer vision, where convolution is used to detect features in deep learning convolution can be used in layers to detect features with filters that are learned [minimizing a loss function](CREATING%20A%20CLASSIFIER.md#MINIMIZING%20THE%20LOSS%20FUNCTION)

## CONVOLUTIONAL LAYERS

So to achieve this in a convolutional layer input and output are not flatten and each output is connected only to a local set of the input that shares the weights thus reducing the weights array dimension of the layer

$$
\displaylines{
y(i,j) = w_1x(i-1,j-1) +w_2x(i-1,j) +w_3x(i-1,j+1)+ \\
w_4x(i,j-1) +w_5x(i,j) +w_6x(i,j+1)+\\
w_7x(i+1,j-1) +w_8x(i+1,j) +w_9x(i+1,j+1) \Rightarrow \\
}
$$
$$
y(i,j) = \sum_{m=-1}^{m=1}\sum_{l=-1}^{l=1} {w(m,l)x(i+m,j+l)}
$$

![](Pasted%20image%2020240504170704.png)

### COLOR IMAGE AS INPUTS

color images are represented as 3 channels input so convolution kernel must be 3-dimensional tensors

$$
[K\times I](i,j) = \sum_{n=1}^{3}\sum_{m}\sum_{l}K_n(m,l)I_n(i+m,j+l)+ b
$$

### OUTPUT ACTIVATION 

By sliding the kernel over the image, input channel are translated in a single channel output i.e. the output activation of the convolutional layer, they are also called feature maps because layers tend to specialize in detecting specific features/patterns

### MULTIPLE CHANNEL OUTPUT ACTIVATION

It can be useful to retrieve multiple channel output for detecting multiple features (e.g. horizontal and vertical edges)

$$
[K^2\times I](i,j) = \sum_{n=1}^{3}\sum_{m}\sum_{l}K^2_n(m,l)I_n(i+m,j+l)+ b^2
$$

### GENERAL STRUCTURE

This approach can be generalized, obtaining the **general structure of a convolutional layer**:

$$
[K^k\times I](i,j) = \sum_{n=1}^{C_{in}}\sum_{m}\sum_{l}K^k_n(m,l)I_n(i+m,j+l)+ b^k\space with \space k=1..C_{out}
$$
![](Pasted%20image%2020240504173105.png)

### CHAINING CONVOLUTIONAL LAYERS

Convolutional layers are a form of linear transformation (they can be expressed by matrix) so in order to take advantage of network depth there is the need to chain them with some form of non-linearity (e.g. [relu](DEEP%20LEARNING%20AND%20NEURAL%20NETWORKS.md#ACTIVATION%20FUNCTION))

![](Pasted%20image%2020240504173234.png)

The main advantage of chaining is that with each level of depth the number of input pixels that the layer takes into account (e.g. the **receptive field**) gets larger and larger enabling the network to detect larger patterns 

![](Pasted%20image%2020240504175829.png)

### STRIDED CONVOLUTION

Convolution can be computed every $S$ (stride) positions in both directions

![](Pasted%20image%2020240504180313.png )
## POOLING LAYERS

Pooling layers are layers with handcrafted functions that aggregates the input neighboring values in order to downsample the output

![](Pasted%20image%2020240504180153.png)

The pooling layer introduces some more hyperparameters such as dimensions of the kernel and stride

## CNN FINAL STRUCTURE

![](Pasted%20image%2020240504180437.png)

## NUMBER OF LEARNABLE PARAMETERS

For a single convolutional layer the number of learnable parameter depends on kernel dimensions and input and output activation dimensions so the size of the $W$ array can be obtained as:

$$
C_{out} \times (C_{in} \times H_k \times W_k +1)
$$

## THE PROBLEM WITH INCREASING DEPTH

Intuitively increasing depth should take better results at the price of computation cost but real testing as shown that this is not the case

![](Pasted%20image%2020240504181754.png)

### RESIDUAL LEARNING AS A SOLUTION

The idea is to add skip connection in order to fast forward the input to the deep nested layers

```mermaid
flowchart LR
A(input)
B[Conv]
C[BN]
D[ReLU]
E[Conv]
F[BN]
G((+))
H[ReLU]
A --> B --> C --> D --> E --> F --> G --> H
A --> G
```

So the output is given by:

$$
H(x) = F(x)+x
$$
