imroute = 'C:/Users/usuario/Downloads/jpeg444.jpg'

import cv2
import numpy as np

img = cv2.imread(imroute,1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)

img = img.transpose((1,0,2))

# img_zeros = np.zeros((256,256,3))

# img = np.row_stack((img,img_zeros))

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
