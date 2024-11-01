---
id: CAMERA_PARAMETERS
aliases: []
tags: []
index: 2
---

# CAMERA PARAMETERS

here are some camera parameters, formal definition can be found at the [EMVA standard 1288](https://www.emva.org/standards-technology/emva-1288/)

## signal-to-noise-ratio (SNR)

intensity of pixel measured varies under the same condition due to noise expressed in decibels or bits, it can be express in decibels or bits

$$
SNR_{dB} = 20 \times log_{10} (SNR )
$$

$$
SNR_{bit} = log_{2}(SNR)
$$

## photon shot noise

time between two photons hit the light sensor governed by a Poisson distribution

## electronic circuit noise

generated  by the electronics

## quantization noise

noise due to quantization phase

## dark circuit noise

even when the sensor is not expose to light there are some charges due to thermal excitement

## dynamic range

range between maximum capacity of the photo-sensors and the minimum power require to distinguish a signal from noise, an higher dynamic range improves the light management of the camera

$E_{min}$ -> minimal detectable irradiation
$E_{max}$ -> saturation irradiation

dynamic range can be express like follow

$$
DR=\frac{E_{max}}{E_{min}}
$$

## quantum efficiency

ratio between photons that are collected by the camera and  photons that hit the sensors

[PREVIOUS](pages/image_formation_acquisition/PERSPECTIVE_PROJECTION.md) [NEXT](pages/image_formation_acquisition/IMAGE_DIGITIZATION.md)
