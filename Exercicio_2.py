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
        func = 255 * ((n_linear - min) / (max - min))
        if func > 255:
            func = 255
            mat.append(func)
        elif func < 0:
            func = 0
            mat.append(func)
        mat.append(func)
    point_mat.append(mat)


point_mat = np.array(point_mat)


hist = []
for i in range(Row):
    for j in range(Column):
        hist.append(point_mat[i][j])


hist_vals = np.bincount(hist)/mat_size

plt.subplot(121).imshow(point_mat, cmap="gray", vmin=0, vmax=255)
plt.subplot(122).plot(hist_vals)
plt.show()

cv2.imwrite('exercicio2_img.jpg', point_mat)
np.savetxt("exercicio2_hist.csv", [hist_vals], delimiter=",")