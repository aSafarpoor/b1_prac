# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# img = cv2.imread('Q4.jpg',0)


# f = np.fft.fft2(img)

# fshift = np.fft.fftshift(f)
# magnitude_spectrum = 20*np.log(np.abs(fshift))

# # plt.imshow(magnitude_spectrum, cmap = 'gray')
# # plt.show()


# signalFFT = fshift

# ## Get Power Spectral Density
# signalPSD = np.abs(signalFFT) ** 2
# signalPhase = np.angle(signalFFT)

# fshift = np.fft.fftshift(signalPSD)
# f = 20*np.log(np.abs(fshift))

# # plt.imshow(f, cmap = 'gray')
# # plt.show()

# # plt.imshow(signalPhase, cmap = 'gray')
# # plt.show()

# f2=signalPhase
# combined = np.multiply(np.abs(f), f2)
# plt.imshow(combined, cmap = 'gray')
# plt.show()

import numpy as np
import cv2
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt

# lol=cv2.imread('Untitled.png',0)
# # print(lol)
# plt.imshow(lol, cmap='gray')
# plt.show()


img = cv2.imread('Q4.jpg',0)

f = np.fft.fft2(img)

fshift1 = np.fft.fftshift(f)

phase_spectrumA = np.angle(fshift1)
magnitude_spectrumB = 20*np.log(np.abs(fshift1))



# print(f[0][0])
# print(np.abs(f))
# print(np.exp(1j*np.angle(f)))
# z=f[0][0]
# print(z,z.real,z.imag)

# ff=f
# x=ff.real
# y=ff.imag

# print(x[10][10],y[10][10],ff[10][10])

# x[0][0]=0

# combined = np.multiply(x, y)

# imgCombined = np.real(np.fft.ifft2(combined))


# plt.imshow(imgCombined, cmap='gray')
# plt.show()


# print(np.angle(f))
c=np.abs(f)

ma=-111111111111111111
mi=-ma
for i in range(256):
    for j in range(256):
        if ma < c[i][j]:
            ma=c[i][j]
        if mi >  c[i][j]:
            mi=c[i][j]
print(ma, " ------------------------------------------- ", mi)
#         c[i][j]=-0

# print(c)

for i in range(25):
    for j in range(25):
        c[i][j]=-mi
for i in range(225,255):
    for j in range(25):
        c[i][j]=mi
for i in range(25):
    for j in range(225,256):
        c[i][j]=mi
for i in range(225,256):
    for j in range(225,256):
        c[i][j]=mi

c[0][0]=mi

# for i in range(256):
#     c[i][i]=mi
#     c[i][-i]=mi

# print(c)

combined = np.multiply(c, np.exp(1j*np.angle(f)))

imgCombined = np.real(np.fft.ifft2(combined))


plt.imshow(img, cmap='gray')
plt.show()
plt.imshow(imgCombined, cmap='gray')
plt.show()


# plt.imshow(phase_spectrumA, cmap='gray')
# plt.show()

# plt.imshow(magnitude_spectrumB, cmap='gray')
# plt.show()

# plt.imshow(magnitude_spectrumB, cmap='gray')
# plt.show()

# plt.imshow(imgCombined, cmap='gray')
# plt.show()

fshift1 = np.fft.fftshift(c)
m = 20*np.log(np.abs(fshift1))

plt.imshow(m, cmap='gray')
plt.show()
