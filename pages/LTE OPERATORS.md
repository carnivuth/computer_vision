
operators $T(.)$ that take a 2D input signal $i(x,y)$ that are:

- linear so:

$T(ai1(x,y) + bi2(x,y)) = ao1(x,y) + bo2(x,y)$ 

with

$o1(.) = T(i1(.)), o2(.) = T(i2(.))$

- transation equivalent:

$T(i (x − x0 , y − y0 )) = o(x − x0 , y − y0 )$

if the operator has this characteristics then the output is given by the convolution  between the input response function $h( x, y ) = T(delta( x, y ))$ and the input signal

$o(x,y) =T(i(x,y)) = \int_{\inf}^{\inf}{\int_{\inf}^{\inf}{i(\alpha,\beta)*h(x-\alpha, y-\beta)}\,d\alpha}\,d\beta$

