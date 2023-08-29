import cv2

filee = input("Masukkan Nama File Citra: ")
citra = cv2.imread(filee)

tebal = 10
if citra is None:
  print("Tidak dapat membaca citra", filee)
  exit()
else:
  shp = citra.shape
  if len(shp) == 2:
    warna = 0
  else:
    warna = [0, 0, 0]

citra_bingkai = citra.copy()
jum_baris = citra.shape[0]
jum_kolom = citra.shape[1]

# Atas
for baris in range(tebal):
  for kolom in range(jum_kolom):
    citra_bingkai[baris, kolom] = warna

# Bawah
for baris in range(jum_baris - tebal, jum_baris):
  for kolom in range(jum_kolom):
    citra_bingkai[baris, kolom] = warna

# Kiri
for baris in range(jum_baris):
  for kolom in range(tebal):
    citra_bingkai[baris, kolom] = warna

# Kanan
for baris in range(jum_baris):
  for kolom in range(jum_kolom - tebal, jum_kolom):
    citra_bingkai[baris, kolom] = warna

cv2.imshow("Citra Asli", citra)
cv2.imshow("Citra Bingkai", citra_bingkai)
cv2.waitKey(0)
cv2.destroyAllWindows()