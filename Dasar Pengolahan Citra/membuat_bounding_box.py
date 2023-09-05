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
# pojok kiri atas
x = int(input("Koordinat x: "))
y = int(input("Koordinat y: "))
# pojok kanan bawah (x+lebar, y+tinggi)
width = int(input("Lebar: "))
height = int(input("Tinggi: "))
citra = cv2.rectangle(citra, (x, y), (x+width, y+height), warna, tebal)
cv2.imshow("Citra dengan bounding box", citra)
cv2.waitKey()
cv2.destroyAllWindows()
