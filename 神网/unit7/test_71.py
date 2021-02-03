import matplotlib.pyplot as plt
from PIL import Image

plt.rcParams['font.sans-serif'] ="SimHei"
img=Image.open("lena512color.tiff")

plt.figure(figsize=(10,10))
plt.subplot(221)
plt.axis("off")
plt.imshow(img)
plt.title("原图",fontsize=20)

plt.subplot(222)
plt.axis("off")
img_flr=img.transpose(Image.FLIP_LEFT_RIGHT)
plt.imshow(img_flr)
plt.title("左右翻转",fontsize=20)

plt.subplot(223)
plt.axis("off")
img_r90=img.transpose(Image.ROTATE_90)
plt.imshow(img_r90)
plt.title("逆时针翻转90度",fontsize=20)

plt.subplot(224)
plt.axis("off")
img_tp=img.transpose(Image.TRANSPOSE)
plt.imshow(img_tp)
plt.title("转置",fontsize=20)

plt.show()