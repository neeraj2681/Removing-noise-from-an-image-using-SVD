import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np
import os
import scipy.io

A = imread('rect_6.jpg')
X = np.mean(A,-1)
m,n = X.shap
img = plt.imshow(X)
img.set_cmap('gray')
plt.show()
print(m)
print(n)

noise_image = X + 1.5*X.std()*np.random.random(X.shape)
print(np.std(X-noise_image))
img = plt.imshow(noise_image)
img.set_cmap('gray')
plt.show()

U,S,VT = np.linalg.svd(noise_image,full_matrices=False)
plt.plot(S,"D")

result = []
freq = []

for i in range(100,10000,50):
	U,S,VT = np.linalg.svd(noise_image,full_matrices=False)
	S = np.array([si if si > i else 0 for si in S])
	S = np.diag(S)
	img_denoised = U@S@VT
	result.append(np.std(X-img_denoised))
	freq.append(i)

plt.plot(freq,result,"D")
plt.show()
print(max(result))

minV = 0
for i in range(len(result)):
	if(result[i]==min(result)):
		minV = freq[i]

U,S,VT = np.linalg.svd(noise_image,full_matrices=False)
S = np.array([si if si > minV else 0 for si in S])
S = np.diag(S)
img_denoised = U@S@VT
img = plt.imshow(img_denoised)
img.set_cmap('gray')
plt.show()

print(minV)
print(min(result))
