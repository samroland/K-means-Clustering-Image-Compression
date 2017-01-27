from scipy.ndimage import imread
import numpy as np
from matplotlib import pyplot as plt
import random

# Load input_image.png as an NxNx3 array. Values range from 0.0 to 255.0.
raw_image = imread('input_image.png', mode='RGB').astype(float)
N = int(raw_image.shape[0])

#compression function
#input is the original image, block size M, and number of clusters k
#output is NxNx3 array
def comp(image, M, k):
    Ntot = N**2//M**2

    # Store each MxM block of the image as a row vector of X
    X = np.zeros((Ntot, 3*M**2))
    for i in range(N//M):
        for j in range(N//M):
            X[i*N//M+j,:] = image[i*M:(i+1)*M,j*M:(j+1)*M,:].reshape(3*M**2)


    #initialize with random choice of cluster centers, selected from X
    rand_index = random.sample(range(Ntot), k)
    mu = np.array([X[i] for i in rand_index])
    
    #initialize old choice of cluster centers, and iteration counter   
    mu_old = np.zeros((k,3*M**2))
    count=0


    #update cluster centers until there is no more change    
    while(not np.array_equal(mu,mu_old)):    
        r = np.zeros((Ntot,k))
        for n in range(Ntot):
            x = X[n]
            diff = np.linalg.norm(x-mu, axis = 1)**2
            min_index = np.argmin(diff)
            r[n,min_index] = 1
        mu_old = mu
        mu = np.dot(r.T,X)/np.sum(r,axis=0).reshape(k,1)
        count+=1
            
    X_comp = np.dot(r,mu)
            
    #initalize and build compressed image
    image_comp = np.zeros((N,N,3))
    for i in range(N//M):
        for j in range(N//M):
            image_comp[i*M:(i+1)*M,j*M:(j+1)*M,:] = X_comp[i*N//M+j,:].reshape(M,M,3)
            
    #return compressed image, normalized to [0,1] range
    return image_comp/255


#set block size M, and number of clusters k
M = 1
k = 32

#save compressed image
image_name = 'compressed_image_' + str(M) + '_' + str(k) + '.png'
image_out = comp(raw_image, M, k)
plt.imsave(image_name, image_out)






