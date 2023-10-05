![](../assets/Pasted%20image%2020231004100201.png)

## SAMPLING
- the image is divided in small a 2D matrix of point known as pixels
![](../assets/Pasted%20image%2020231004100324.png)

## QUANTIZATION
- like audio signals, the pixels is quantized into `l=2^m` levels called gray levels where m is the number of bits used to rappresent a level
- the occupance of the image (in bits) is given by `B=N*M*m` (m=8 in digital gray images)
- bigger m, M,N= better image
### CAMERA PARAMETERS
- **signal-to-noise-ratio (SNR)**
	- intensity of pixel measured varies under the same condition due to noise
	- expressed in decibels or bits 
-  **photon shot noise**
	- time between two photons hit the light sensor governed by a poisson distribution
- **electronic circuit noise** 
	- generated  by the electronics
- **quantization noise**
	- noise due to quantization fase
- **dark circuit noise**
	- even when the sensor is not expose to light there are some charges due to thermal excitement
- **dynamic range**
	- range between maximum capacity of the photosensors and the minimum power require to distinguish a signal from noise
	- `Emin` minimal detectable irradiation `Emax` saturation irradiation so `DR=Emax/Emin`
	- expressed in decibel or bits
	- higher dynamic range = better light management in the image
-  **High dynamic range**
	- it's nedeed in autonomous drive
- quantum efficiency
	- ratio between photons that are collected by the camera and  photons that hit the sensors 
## CMOS VS CCD
![](../assets/Pasted%20image%2020231004102609.png)
