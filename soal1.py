
# Data awal)
siswa = ["Alya", "Budi", "Citra", "Deni", "Eva"]
siswa.append("Fahri")
index_citra = siswa.index("Citra")
siswa[index_citra] = "Chandra"
siswa.remove("Budi")
print("Jumlah total siswa:", len(siswa))
print("Daftar siswa:")
for nama in siswa:
    print("-", nama)