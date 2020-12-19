import numpy as np

import matplotlib.pyplot as plt

np.random.seed(3)
traing =[]

long = 50000
xp = (np.random.rand(long,1) )*3
# d# plt.plot(xp,np.ones(long),'yo',alpha = .5)
yp = np.random.rand(long,1) *3
dis = np.concatenate((xp,yp),axis=1)

# plt.plot(dis[:,0],dis[:,1],'yo',alpha = .5)
# pr(multi)
multi = np.dot([[2,0],[0,2]],dis.T)
plt.style.use('dark_background')
plt.figure(figsize=(14,14))
ttarget = []
for x,y in zip(multi[0],multi[1]):
    if x-y <0 :
        ttarget.append(0)
    else:
        ttarget.append(1)
#     pb(x,'  ',y)
    pass
# pr(multi)


ddata = np.reshape(multi,(long,2))

# pb(multi.shape)



for p in zip(xp,xp):
    if p[0]!=p[0]:
        pr('what')
# plt.figure(figsize=(18,18))
targ = []
for x,y in dis:
    if x-y <=0 :
        targ.append(0)
    else:
        targ.append(1)
        
# plt.scatter(dis[:,0],dis[:,1],cmap='cool',alpha = .5,s=7,c=targ)
new =  np.asarray(targ).reshape((long,1))
ttarget=  np.asarray(targ).reshape((long,1))
# pb(dis)
# dis[:,:-1]=new
traing = np.hstack((dis,new))
np.set_printoptions(formatter={'float': lambda x: "{0:0.1}".format(x)})
# print(multi)
multi = multi.T
# pb(len(multi))
# py(multi[:3])
multi[:,1] +=2
# plt.scatter(multi[:,0],multi[:,1],c=ttarget[:],cmap='spring',alpha = .5,s=7)

multi = np.hstack((multi,ttarget))
plt.xlim(-1, 9)
plt.ylim(-1, 9)
normal_dist = np.random.randn(long,2)
norm_targ = []
for x,y in normal_dist:
    if x-y <=0 :
        norm_targ.append(0)
    else:
        norm_targ.append(1)
        
# plt.scatter(multi[:,0],multi[:,1],c=multi[:,2],cmap='spring',alpha = .3,s=70)

norm_shit2 = normal_dist.copy()
norm_shit2[:,1] +=2

# plt.scatter(normal_dist[:,0],normal_dist[:,1],c=norm_targ,cmap='spring',alpha = .5,s=7)
plt.scatter(norm_shit2[:,0],norm_shit2[:,1],c=norm_targ,cmap='gist_rainbow',alpha = .05,s=40)

plt.show()
def hot_one_converter(number,classificatoin_count=10):
        """ Takes a number and return a hot one array
        Hot one array: is an array of zeros and single one
        
        Args:
            number (int): number to be converted to array the number will represented as the only one in the array
            classificatoin_count (int, optional): Size of the array. Defaults to 10.
        """
        hot_one = np.zeros((classificatoin_count,1))
        #if number > -1 and number < classificatoin_count:
        hot_one[number] = 1
        return hot_one



norm_shit2_shape21 = [  np.array(point).reshape(2,1) for     point in norm_shit2  ]
# py(norm_shit2_shape21[0],norm_shit2[0])

# nett = Network((2,2))
# display(Matrix(nett.weights[0]))
# display(Matrix(nett.weights[1]))
# nett.SGD(zip(norm_shit2_shape21,norm_targV),20, 10, .01, test_data=zip(norm_shit2_shape21,norm_targ))

# train_yv = [hot_one_converter(res) for res in train_y]
# train_Xv = [np.reshape( res.flatten() /np.max(res) , (784,1)) for res in train_X]


# test_yv = [hot_one_converter(res) for res in test_y]
# test_Xv = [np.reshape( res.flatten() /np.max(res) , (784,1)) for res in test_X]
# train_X = [np.clip(np.reshape( res.flatten() /np.max(res) , (784,1)) for res in train_X]
def getdata():
    return norm_shit2_shape21 , norm_targV , norm_shit2_shape21 ,norm_targ