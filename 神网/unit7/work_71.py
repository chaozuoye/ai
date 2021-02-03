import matplotlib.pyplot as plt

from PIL import Image
plt.rcParams['font.sans-serif'] ="SimHei"
img=Image.open("lena.tiff")
img_r, g, b=img.split()



plt.subplot(221)
rs=img_r.resize((50, 50))
plt.imshow(rs, cmap='gray')
plt.title("R-缩放",fontsize=14)
plt.axis("off")

plt.subplot(222)
g_frl=g.transpose(Image.FLIP_LEFT_RIGHT)
g_frl_cw90=g_frl.transpose(Image.ROTATE_270)
plt.imshow(g_frl_cw90,cmap='gray')
plt.title("G-镜像+旋转",fontsize=14)

plt.subplot(223)
b_crop=b.crop((0,0,300,300))
plt.imshow(b_crop,cmap='gray')
plt.title("B-裁剪",fontsize=14)
plt.axis("off")
b_crop.save("test.png")

rgb=Image.merge("RGB", [img_r, g, b])
plt.subplot(224)
plt.imshow(rgb)
plt.title("RGB",fontsize=20)

plt.suptitle("图像基本操作",fontsize=20,color="blue")
plt.tight_layout(rect=[0,0,1,0.9])
plt.show()