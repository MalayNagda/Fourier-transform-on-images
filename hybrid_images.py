import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('5.jpg',cv2.IMREAD_GRAYSCALE)
height, width = img.shape
img1=np.fft.fft2(img)
fshift=np.fft.fftshift(img1)

r = 35
h_Filter_Low_Pass = np.zeros(img.size, img.dtype).reshape(img.shape)
for icounter in range(1, height):
    for jcounter in range(1, width):
        if ((icounter - height/2)**2 + (jcounter - width/2)**2) < r**2:
            h_Filter_Low_Pass[icounter, jcounter] = 1

LPF_img = fshift*h_Filter_Low_Pass
ishi=np.fft.ifftshift(LPF_img)
g_ifft1 = np.abs(np.fft.ifft2(ishi).real)
plt.imshow(g_ifft1,cmap='gray')
plt.title(''), plt.xticks([]), plt.yticks([])
plt.show()

img=cv2.imread('6.jpg',cv2.IMREAD_GRAYSCALE)
height, width = img.shape
img2=np.fft.fft2(img)
fshift=np.fft.fftshift(img2)

r = 20
h_Filter_Low_Pass = np.zeros(img.size, img.dtype).reshape(img.shape)
for icounter in range(1, height):
    for jcounter in range(1, width):
        if ((icounter - height/2)**2 + (jcounter - width/2)**2) < r**2:
            h_Filter_Low_Pass[icounter, jcounter] = 1

HPF_img = fshift*(1-(h_Filter_Low_Pass))
ishi=np.fft.ifftshift(HPF_img)
g_ifft2 = np.abs(np.fft.ifft2(ishi).real)
plt.imshow(g_ifft2,cmap='gray')
plt.title(''), plt.xticks([]), plt.yticks([])
plt.show()

final=g_ifft1+g_ifft2
plt.imshow(final,cmap='gray')
plt.title(''), plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('hybrid.png',final)
