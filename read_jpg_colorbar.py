import random as rd
import pandas as pd
from skimage.color import rgba2rgb
import matplotlib.pyplot as plt
from skimage import io
img = io.imread("openworks_colorbar.jpg")

fig = plt.figure(figsize=(5,5))
p1 = plt.subplot(1, 1,1)
p1.imshow(img)

bar=img[0,:,:]

uni_clr=[]
temp=bar[0].tolist()
uni_clr.append(temp)

for i in range(bar.shape[0]):
    if (temp!=bar[i]).any():
        uni_clr.append(bar[i].tolist())
        temp=bar[i]
        
uni_clr=np.array(uni_clr)[:-1]
