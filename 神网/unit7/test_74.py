import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
img=Image.open("lena.tiff")
arr_img=np.array(img)
print(arr_img)

plt.figure(figsize=(5,5))
img_small=img.resize((64,64))

plt.imshow(img_small)
plt.show()

img_region=img.crop((100,100,400,400))
img_region.save("lena剪切图.tiff")
plt.imshow(img_region)
plt.show()
