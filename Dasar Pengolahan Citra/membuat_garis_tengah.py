import cv2

filee = input("Masukkan Nama File Citra: ")
citra = cv2.imread(filee)
if citra is None:
    print("Tidak dapat membaca citra", filee)
    exit()
else:
    shp = citra.shape
    if len(shp) == 2:
        warna = 0
    else:
        warna = [0, 255, 0]
tebal = 2
x = citra.shape[0] // 2
y = citra.shape[1] // 2
citra = cv2.line(citra, (x, 0), (x, citra.shape[1]), warna, tebal)
citra = cv2.line(citra, (0, y), (citra.shape[0], y), warna, tebal)
cv2.imshow("Citra dengan Garis Tengah", citra)
cv2.waitKey()
cv2.destroyAllWindows()


