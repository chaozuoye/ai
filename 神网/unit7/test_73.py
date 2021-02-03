import matplotlib.pyplot as plt

from PIL import Image

img=Image.open("lena.tiff")
r,g,b=img.split()

plt.figure(figsize=(10,10))

plt.subplot(221)
plt.imshow(r,cmap='Reds')
plt.title("R",fontsize=20)

plt.subplot(222)
plt.imshow(g,cmap='Greens')
plt.title("G",fontsize=20)

plt.subplot(223)
plt.imshow(b,cmap='Blues')
plt.title("B",fontsize=20)

rgb=Image.merge("RGB",[r,g,b])
plt.subplot(224)
plt.imshow(rgb)
plt.title("RGB",fontsize=20)

plt.show()