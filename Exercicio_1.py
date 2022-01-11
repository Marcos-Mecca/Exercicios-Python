import numpy as np
import cv2
import matplotlib.pyplot as plt

file = cv2.imread("img_teste.jpg", 0)
Row, Colum = file.shape
mat_size = Row * Colum
hist = []

for i in range(Row):
    for j in range(Colum):
        hist.append(file[i][j])

hist_vals = np.bincount(hist)/mat_size

plt.plot(hist_vals)
plt.show()

np.savetxt("exercicio1_hist.csv", [hist_vals], delimiter=",")
