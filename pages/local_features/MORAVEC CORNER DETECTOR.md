# MORAVEC CORNER DETECTOR

In this detector the measure of cornerness is given by 

$$
C(p) = \min_{q \in n_8(p)}{\Vert N(p)-N(q)\Vert^2}
$$

Where $N$ is the neighborhood around the point and its neighbors

The output is the lowest difference computed between the neighborhood of $p$ and the neighborhoods of the neighbor points $q$ 

![](Pasted%20image%2020240310153802.png)