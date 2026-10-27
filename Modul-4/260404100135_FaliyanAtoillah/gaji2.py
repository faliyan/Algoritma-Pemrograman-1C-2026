gaji_harian = 100000
gaji_shift_malam = 50000
total_gaji = 0

for hari in range(1,8):
    print(f"Hari ke-{hari}")

    while True:
        jam_lembur = int(input("Masukkan jam lembur (0/1/2/3/4/6/8): "))
        if jam_lembur > 8 or jam_lembur == 5 or jam_lembur == 7 or jam_lembur < 0:
            print("Jam lembur tidak tidak sesuai ketentuan, ulangi.")
        else:
            break

    if jam_lembur >= 1 and jam_lembur <= 3:
        upah_lembur = 25000 * jam_lembur
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:                   
        upah_lembur = 0

    shift_malam = str(input("Shift malam(y/n): "))
    if shift_malam == "y":
        upah_shift_malam = gaji_shift_malam
    else:
        upah_shift_malam = 0

    gaji_perhari = gaji_harian + upah_lembur + upah_shift_malam
    total_gaji += gaji_perhari
    print(f"Gaji hari ke-{hari}: Rp{gaji_perhari}")

print("Total gaji mingguan: Rp", total_gaji)