jumlahMahasiswa = 0
jumlah_a = 0
jumlah_b = 0
jumlah_c = 0
jumlah_d = 0
jumlah_e = 0
total_nilai = 0

nilai_tertinggi = -1
nama_tertinggi = ""

nilai_terendah = 101
nama_terendah = ""

for i in range(1, 11):
    print("--- Mahasiswa ke-%d ---" % i)
    nama = input("Nama        : ")

    while True:
        nilai_tugas = int(input("Nilai tugas : "))
        if 0 <= nilai_tugas <= 100:
            break
        print("Nilai harus 0-100!")

    while True:
        nilai_uts = int(input("Nilai UTS   : "))
        if 0 <= nilai_uts <= 100:
            break
        print("Nilai harus 0-100!")

    while True:
        nilai_uas = int(input("Nilai UAS   : "))
        if 0 <= nilai_uas <= 100:
            break
        print("Nilai harus 0-100!")

    nilai_akhir = (nilai_tugas * 30 + nilai_uts * 30 + nilai_uas * 40) / 100

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_a += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_b += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_c += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_d += 1
    else:
        kategori = "E"
        jumlah_e += 1

    print(">>", nama)
    print("   Tugas %d | UTS %d | UAS %d" % (nilai_tugas, nilai_uts, nilai_uas))
    print("   Nilai akhir %.2f | Kategori %s" % (nilai_akhir, kategori))

    total_nilai += nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama
    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

print("=== REKAP KELAS ===")
print("Jumlah A:", jumlah_a)
print("Jumlah B:", jumlah_b)
print("Jumlah C:", jumlah_c)
print("Jumlah D:", jumlah_d)
print("Jumlah E:", jumlah_e)
print("Tertinggi : %.2f (%s)" % (nilai_tertinggi, nama_tertinggi))
print("Terendah  : %.2f (%s)" % (nilai_terendah, nama_terendah))
print("Rata-rata : %.2f" % (total_nilai / 10))
