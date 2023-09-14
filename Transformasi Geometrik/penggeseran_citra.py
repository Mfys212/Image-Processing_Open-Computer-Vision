import cv2
import numpy as np

filee = input("Masukkan Nama File Citra: ")
citra = cv2.imread(filee)
if citra is None:
    print("Tidak dapat membaca citra", filee)
    exit()
jum_baris = citra.shape[0]
jum_kolom = citra.shape[1]
hor = 100 # nilai pergeseran horizontal
ver = 50 # nilai pergeseran vertikal
matriks = np.float32([[1, 0, hor], [0, 1, ver]])
citra_tergeser = cv2.warpAffine(citra, matriks, (jum_kolom, jum_baris))
cv2.imshow("Citra Asli", citra)
cv2.imshow("Citra Tergeser", citra_tergeser)
cv2.waitKey()
cv2.destroyAllWindows()
