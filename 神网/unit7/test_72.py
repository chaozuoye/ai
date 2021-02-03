import matplotlib.pyplot as plt

from PIL import Image

image1=Image.open("lena.tiff")
image2=Image.open("lena.bmp")

print("image1 format:"+str(image1.format)+"size:"+str(image1.size)+"mode:"+str(image1.mode))
print("image2 format:"+str(image2.format)+"size:"+str(image2.size)+"mode:"+str(image2.mode))

plt.figure(figsize=(6,6))
plt.imshow(image1)
plt.show()

image_gray=image1.convert("1")
print("mode=",image_gray.mode)

plt.figure(figsize=(5,5))
plt.imshow(image_gray)
plt.show()