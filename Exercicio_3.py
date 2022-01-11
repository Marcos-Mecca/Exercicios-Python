import numpy as np
import cv2
import matplotlib.pyplot as plt

file = cv2.imread("img_teste.jpg", 0)
Row, Column = file.shape
mat_size = Row * Column


file_mat = []
for a in range(Row):
    for b in range(Column):
        file_mat.append(file[a][b])

freq = np.bincount(file_mat)
copy = np.copy(freq)
freq_accumulated = []
for k in range(len(freq)):
    if k == 0:
        copy[k] = copy[k]
        freq_accumulated.append(copy[k])
    else:
        copy[k] = copy[k] + copy[k - 1]
        freq_accumulated.append(copy[k])

max = np.max(file_mat)
img_eq = []
for x in range(Row):
    mat = []
    for y in range(Column):
        a = freq_accumulated[file[x][y]]
        final_value = freq_accumulated[file[x][y]] /mat_size * 255
        mat.append(int(final_value))
    img_eq.append(mat)
img_eq = np.array(img_eq)

hist = []
for i in range(Row):
    for j in range(Column):
        hist.append(img_eq[i][j])


hist_value = np.bincount(hist)/mat_size

plt.subplot(121).imshow(img_eq, cmap="gray", vmin=0, vmax=255)
plt.subplot(122).plot(hist_value)
plt.show()

cv2.imwrite('exercicio3_img.jpg', img_eq)
np.savetxt("exercicio3_hist.csv", [hist_value], delimiter=",")
