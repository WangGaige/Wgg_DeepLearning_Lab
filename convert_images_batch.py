#convert input png to jpg
from PIL import Image
import os
path=r"E:\wgaigeTfProjects\UNET\Multiclass-Segmentation-in-Unet-master\oxford-iiit-pet\images"
path1=r"E:\wgaigeTfProjects\UNET\Multiclass-Segmentation-in-Unet-master\oxford-iiit-pet\imgjpg"
arr = os.listdir(path)
for i in arr:
    im = Image.open(path+"\{}".format(i))
    rgb_im = im.convert('RGB')
    j=i.replace("png","jpg")
    rgb_im.save(path1+"\{}".format(j))
    
    
    
#map color value to 123
from PIL import Image
import os
path=r"E:\wgaigeTfProjects\UNET\Multiclass-Segmentation-in-Unet-master\oxford-iiit-pet\annotations\trimaps1"
path1=r"E:\wgaigeTfProjects\UNET\Multiclass-Segmentation-in-Unet-master\oxford-iiit-pet\annotations\trimaps"
arr = os.listdir(path)
for i in arr:
    x = cv2.imread(path+"\{}".format(i), cv2.IMREAD_GRAYSCALE)
    distinct_vals=np.unique(x)
    x[x==distinct_vals[0]] = 0
    x[x==distinct_vals[1]] = 2
    x[x==distinct_vals[2]] = 1
    x = x.astype(np.int32)
    cv2.imwrite(path1+"\{}".format(i), x)
