# Fourier transform on images

The objective was to see how Fourier transform can be used on images to get useful information about images that can be used for various image processing purposes.

## Phase swapping 

To swap the phase information of images, we use Fourier transform to calculate the magnitude and phase of each image, the magnitude of one image is multiplied with the phase of other image.
Inverse Fourier transform is then performed on this result so that results of this phase swapping on both the images can be displayed as images.

The original images are- 
<p align="center">
  <img src="images/9n10.png">
</p>

After swapping the phases, the images look like-
<p align="center">
  <img src="images/ph2ph1.png">
  The left image here contains the phase of original right image and vice versa for the right image here.
</p>

From these results it can be said that phase information contains the location of the features as we can partially the rail tracks in the left image of the result and very little 
information of the original image on the left. Similarly, we can see the 'Stanley' hoarding in the right image of the result which was originally present in the left image. 

## Hybrid images

