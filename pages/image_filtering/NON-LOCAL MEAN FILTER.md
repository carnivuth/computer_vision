# NON-LOCAL MEAN FILTER

Non linear filter which exploits similarities between different patches of the image

![](Pasted%20image%2020240302112646.png)

$$
O(p) = \sum_{p\in S}w(p,q)I_{q} \space where
$$
$$
\displaylines{w(p,q) = \frac{1}{Z(p)}e^{-\frac{\Vert N_p -N_q\Vert_2^2}{h^2}} \\
Z(p)= \sum_{q \in I} e^{\frac{\Vert N_p -N_q\Vert_2^2}{h^2}} }
$$
![](Pasted%20image%2020240302112706.png)
