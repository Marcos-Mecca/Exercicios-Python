import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

file = cv2.imread("img_teste.jpg", 0)
Row, Column = file.shape
mat_size = Row * Column

min = np.min(file)
max = np.max(file)
point_mat = []
for m in range(Row):
    mat = []
    x = 0
    for n in range(Column):
        x = file[m][n]
        n_linear = int(math.pow(x, 1.00175))
        func = int(255 * ((n_linear - min) / (max - min)))
        if func > 255:
            func = 255
            mat.append(func)
        elif func < 0:
            func = 0
            mat.append(func)
        mat.append(func)
    point_mat.append(mat)

negative_img = []
for m in range(Row):
    mat1 = []
    for n in range(Column):
            func = 255 - point_mat[m][n]
            mat1.append(func)
    negative_img.append(mat1)

negative_img = np.array(negative_img)

hist = []
for i in range(Row):
    for j in range(Column):
        hist.append(negative_img[i][j])


hist_value = np.bincount(hist)/mat_size

plt.subplot(121).imshow(negative_img, cmap="gray", vmin=0, vmax=255)
plt.subplot(122).plot(hist_value)
plt.show()

cv2.imwrite('exercicio4_img.jpg', negative_img)
np.savetxt("exercicio4_hist.csv", [hist_value], delimiter=",")
