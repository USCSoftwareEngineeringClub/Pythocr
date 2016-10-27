import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi

from skimage import feature
import skimage.external.tifffile
import skimage.color
import sys


# Generate noisy image of a square
im = skimage.external.tifffile.imread(sys.argv[1])
im = skimage.color.rgb2grey(im)
print(im)
print(type(im))
print(im.shape)

# im[32:-32, 32:-32] = 1

# im = ndi.rotate(im, 15, mode='constant')
# im = ndi.gaussian_filter(im, 4)
# im += 0.2 * np.random.random(im.shape)

# Compute the Canny filter for two values of sigma
edges1 = feature.canny(im)
edges2 = feature.canny(im, sigma=3)

# display results
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3), sharex=True, sharey=True)

ax1.imshow(im, cmap=plt.cm.jet)
ax1.axis('off')
ax1.set_title('noisy image', fontsize=20)

ax2.imshow(edges1, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)

ax3.imshow(edges2, cmap=plt.cm.gray)
ax3.axis('off')
ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                    bottom=0.02, left=0.02, right=0.98)

plt.show()