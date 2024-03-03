# BINARY MORPHOLOGY

The binary morphology operators take as input a [binarized](BINARIZATION.md) image and make improvement before the labeling phase

The idea is to slide a small kernel called structuring element

## DILATION

The output image is obtained by sliding the kernel on each black element

![](Pasted%20image%2020240303171944.png)
## EROSION

The output image is obtained by sliding the kernel on the all image leaving only the black points that contain the kernel

![](Pasted%20image%2020240303172045.png)

## OPENING AND CLOSING

Erosion followed by dilation is called opening

$$
A \circ B = (A \ominus B) \oplus B
$$
Dilation followed by erosion is called opening

$$
A \bullet B = (A \oplus B) \ominus B
$$
