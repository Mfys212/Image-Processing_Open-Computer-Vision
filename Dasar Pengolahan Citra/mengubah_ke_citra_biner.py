import cv2
import numpy as np

filee = input("Masukkan Nama File Citra: ")
citra = cv2.imread(filee)
if citra is None:
    print("Tidak dapat membaca citra", filee)
    exit()
citra_ = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)
a = input("Threshold (0 untuk default): ")
if a == None or a == "":
    threshold = None
else:
    threshold = float(a)
if threshold == None or threshold == 0:
    thr, citra_biner = cv2.threshold(citra_, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
else:
    thr, citra_biner = cv2.threshold(citra_, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow("Citra Asli", citra)
cv2.imshow("Citra Biner", citra_biner)
cv2.waitKey()
cv2.destroyAllWindows()
