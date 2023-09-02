import cv2

filee = input("Masukkan Nama File Citra: ")
citra = cv2.imread(filee)
if citra is None:
  print("Tidak dapat membaca citra", filee)
  exit()
x = int(input("Koordinat x: "))
y = int(input("Koordinat y: "))
width = int(input("Koordinat Lebar: "))
height = int(input("Koordinat Tinggi: "))
area = citra[x:width, y:height]
try:
  cv2.imshow("Citra Asli", citra)
  cv2.imshow("Area Terpilih", area)
except:
  print("index input salah")
  exit()
cv2.waitKey()
cv2.destroyAllWindows()