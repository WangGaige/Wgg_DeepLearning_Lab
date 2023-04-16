nparray_pred=nparray.copy()
nparray_1=nparray.copy()
import time
import matplotlib.image as im
import matplotlib.pyplot as plt
from tqdm import tqdm
size=128
maxv_cut=1200

maxv=maxv_cut
maxcondition=(nparray_1>=maxv)
a=np.where(maxcondition)
minv=-maxv_cut
mincondition=(nparray_1<=minv)
b=np.where(mincondition)
nparray_1[a]=maxv_cut
nparray_1[b]=-maxv_cut
nparray_1=np.interp(nparray_1, (nparray_1.min(),nparray_1.max()), (0, uni_clr.shape[0]-1))
nparray_1=nparray_1.astype(dtype='int64')

nparray_1=uni_clr[nparray_1]


import scipy.ndimage as ndimage
for line in tqdm(range(nparray_1.shape[0])):
    seisline =nparray_1[line,:,:]
    #print("{}-{}".format(line,nparray.shape[0]))
    seisline=seisline.transpose(1,0,2)
    seisline=seisline.astype(np.uint8)

    iblock=seisline.shape[0]//size
    jblock=seisline.shape[1]//size
    cavepred=np.zeros([(i_block+1)*size,(j_block+1)*size,1])

    for i in range(i_block+1):
        for j in range(j_block+1):
            ll=seisline[i*size:(i+1)*size,j*size:(j+1)*size]
            
            x = cv2.resize(ll, (W, H))
            x = x / 255.0
            x = x.astype(np.float32)
            p = model.predict(np.expand_dims(x, axis=0))[0]
            p = np.argmax(p, axis=-1)
            p = np.expand_dims(p, axis=-1)
            p = p * (255/num_classes)
            p = p.astype(np.uint8)
            p = ndimage.gaussian_filter(p, sigma=(2, 2, 2), order=0)
            p = cv2.resize(p, (size,size))
            cavepred[i*size:(i+1)*size,j*size:(j+1)*size,0]=p
    cavepred=cavepred[0:x0.shape[0],0:x0.shape[1],:]
    nparray_pred[line,:,:]=cavepred.transpose()
