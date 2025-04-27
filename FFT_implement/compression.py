import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np

A = imread('FFT_implement/SAMPLE_IMG.png')  # Load the image
print(A.shape)  # Print the shape of the image
B = np.mean(A, -1)  # Convert to grayscale
print(B.shape)  # Print the shape of the grayscale image
n, m = B.shape

print(B)


plt.figure()
plt.imshow(256-B, cmap='gray')  # Display the grayscale image
plt.axis('off')  # Turn off the axis
plt.show()  # Show the image

F = np.fft.fft2(B)  # Tính FFT 2D
# F_shifted = np.fft.fftshift(F)  # Dịch chuyển thành phần tần số thấp vào giữa
magnitude_spectrum = 20 * np.log(np.abs(F))  # Tính biên độ phổ

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(B, cmap='gray')
plt.title('Ảnh gốc (grayscale)')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Phổ Fourier (magnitude)')
plt.axis('off')

plt.show()

