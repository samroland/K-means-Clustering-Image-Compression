# K-means-Clustering-Image-Compression
This Python script implements the K-means clustering algorithm to compress a square image (N x N pixels). This form of compression is lossy.

The user may select the value of k (the number of clusters), and M (the size of each block). The compression involves replacing each M x M block of the image by one of k blocks. The goal of the algorithm is to optimally choose those k blocks. Details of how this algorithm is implemented, and the objective function which is being minimized, may be found in chapter 9.1 of “Pattern Recognition and Machine Learning” by Christopher M. Bishop.

This program may be used simply to reduce the size of an image file, or to create a posterized version of the original image.
The output image is saved in the same directory, with the file name "compressed_image_M_k.png", where M and k are set by the user. 

An example image has been included, along with the output for two choices of (k,M).

