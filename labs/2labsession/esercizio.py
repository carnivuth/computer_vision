import cv2
import numpy as np
from matplotlib import pyplot as plt

def linearStretch(image, Pmin, Pmax):
    
    return image*(255/(Pmax-Pmin))*(image-Pmin)

img = cv2.imread("ex/image.png", cv2.IMREAD_GRAYSCALE)

hist, bins = np.histogram(linearStretch(img.flatten(),0,40), 256, [0,256])
plt.stem(hist)
plt.show()