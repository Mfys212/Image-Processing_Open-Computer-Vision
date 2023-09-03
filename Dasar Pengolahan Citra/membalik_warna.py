import cv2

filee = input("Masukkan Nama File: ")
citra = cv2.imread(filee)
if citra is None:
    print("Tidak dapat membaca citra", filee)
    exit()
shp = citra.shape
jum_baris = shp[0]
jum_kolom = shp[1]
invers_citra = 255 - citra
cv2.imshow("Citra Asli", citra)
cv2.imshow("Citra Invers", invers_citra)
cv2.waitKey(0)
cv2.destroyAllWindows()