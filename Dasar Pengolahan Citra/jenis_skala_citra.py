import cv2

filee = input("Masukkan Nama File Citra: ")

citra = cv2.imread(filee, cv2.IMREAD_UNCHANGED)
if citra is None:
  print("Tidak dapat membaca citra", filee)
else:
  shp = citra.shape
  if len(shp) == 2:
    print("Citra Berskala Abu-Abu")
  else:
    print("Citra Berwarna")