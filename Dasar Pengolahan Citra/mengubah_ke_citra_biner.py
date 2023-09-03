import cv2
import numpy as np

filee = input("Masukkan Nama File Citra: ")
citra = cv2.imread(filee)
if citra is None:
    print("Tidak dapat membaca citra", filee)
    exit()
citra_ = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)
threshold = float(input("Threshold: "))
citra_biner = np.where(citra_ > threshold, 255, 0).astype(np.uint8)
cv2.imshow("Citra Asli", citra)
cv2.imshow("Citra Biner", citra_biner)
cv2.waitKey()
cv2.destroyAllWindows()