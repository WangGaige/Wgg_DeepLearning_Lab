x0=seisline0
size=128
i_block=x0.shape[0]//size
j_block=x0.shape[1]//size
cavepred=np.zeros([(i_block+1)*size,(j_block+1)*size,1])

from skimage.transform import rescale, resize, downscale_local_mean
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

# display amp and pred seperately
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(20,20))
p1 = plt.subplot(1, 2, 1)
p1.imshow(x0,aspect=1)
p1 = plt.subplot(1, 2, 2)
p1.imshow(cavepred,aspect=1)


# stack amp and pred transparent
# Create an alpha channel of linearly increasing values moving to the right.
#v0
alphas=0.5

# Create the figure and image
fig, ax = plt.subplots(figsize=(20,20))
ax.imshow(x0)
ax.imshow(cavepred, alpha=alphas)
ax.set_axis_off()
