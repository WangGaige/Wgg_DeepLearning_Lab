nparray_pred=nparray.copy()

import time
import matplotlib.image as im
import matplotlib.pyplot as plt
from tqdm import tqdm
size=128
maxv_cut=1200
for line in tqdm(nparray.shape[0]):
    seisline =nparray[line,:,:]
    print("{}-{}".format(line,nparray.shape[0]))
    
    maxv=maxv_cut
    maxcondition=(seisline>=max)
    a=np.where(maxcondition)
    minv=-maxv_cut
    mincondition=(seisline<=min)
    b=np.where(mincondition)
    seisline[a]=maxv_cut
    seisline[b]=-maxv_cut
    
    seisline=np.interp(seisline, (seisline.min(), seisline.max()), (0, uni_clr.shape[0]-1))
    seisline=seisline.astype(dtype='int64')
    seisline=uni_clr[seisline.transpose()]
    seisline=seisline.astype(np.uint8)

    iblock=seisline.shape[0]//size
    jblock=seisline.shape[1]//size
    cavepred=np.zeros([(i_block+1)*size,(j_block+1)*size,1])

    for i in range(i_block+1):
        for j in range(j_block+1):
            ll=x0[i*size:(i+1)*size,j*size:(j+1)*size]
            ll = np.array(ll, dtype='uint8')
            x = cv2.resize(ll, (W, H))
            x = x / 255.0
            x = x.astype(np.float32)
            p = model.predict(np.expand_dims(x, axis=0))[0]
            p = np.argmax(p, axis=-1)
            p = np.expand_dims(p, axis=-1)
            p = p * (255/num_classes)
            p = p.astype(np.uint8)
            p = cv2.resize(p, (size,size))
            cavepred[i*size:(i+1)*size,j*size:(j+1)*size,0]=p
    cavepred=cavepred[0:x0.shape[0],0:x0.shape[1],:]
    nparray_pred[line,:,:]=cavepred.transpose()
