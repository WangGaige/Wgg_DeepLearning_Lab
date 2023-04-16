seiscut=nparray[350,:,:]

#cut amp value
max_v=2000
maxcondition=(seiscut>=max_v)
a=np.where(maxcondition)

min_v=-2000
mincondition=(seiscut<=min_v)
b=np.where(mincondition)

seiscut[a]=max_v
seiscut[b]=min_v

data=np.interp(seiscut, (seiscut.min(), seiscut.max()), (0, 565))
data=data.astype(dtype='int64')
bb=uni_clr[data.transpose()]

fig = plt.figure(figsize=(15,15))
p1 = plt.subplot(1, 1,1)
seisline0 = bb[:,:,:3]
p1.imshow(seisline0)
