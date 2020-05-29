import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('9.jpg',cv2.IMREAD_GRAYSCALE)
f1=np.fft.fft2(img)
fshift=np.fft.fftshift(f1)
mag1=20*np.log(np.abs(fshift))
mag1=np.asarray(mag1,dtype=np.uint8)
phase1=np.angle(f1)
phase1=np.asarray(f1,dtype=np.uint8)
cv2.imshow('img',img)
cv2.imshow('Magnitude Spectrum 1',mag1)
cv2.imshow('Phase Spectrum 1',phase1)

img=cv2.imread('10.jpg',cv2.IMREAD_GRAYSCALE)
f2=np.fft.fft2(img)
fshift=np.fft.fftshift(f2)
mag2=20*np.log(np.abs(fshift))
mag2=np.asarray(mag2,dtype=np.uint8)
phase2=np.angle(fshift)
phase2=np.asarray(fshift,dtype=np.uint8)
cv2.imshow('img',img)
cv2.imshow('Magnitude Spectrum 2',mag2)
cv2.imshow('Phase Spectrum 2',phase2)
cv2.imwrite('magspec2.png',mag2)
cv2.imwrite('phasespec2.png',phase2)
cv2.imwrite('magspec1.png',mag1)
cv2.imwrite('phasepec1.png',phase1)
cv2.waitKey(0)
cv2.destroyAllWindows()

g1= np.multiply(np.abs(f1),np.exp(1j)*np.angle(f2))
g_ifft = np.real(np.fft.ifft2(g1))

plt.figure('1')
plt.imshow(g_ifft,cmap='gray')
plt.show()
plt.savefig('mag1ph2.png')

g2= np.multiply(np.abs(f2),np.exp(1j)*np.angle(f1))
g_ifft2 = np.real(np.fft.ifft2(g2))

plt.figure('2')
plt.imshow(g_ifft2,cmap='gray')
plt.show()
plt.savefig('mag2ph1.png')
