
jarak=100
Konsumsi_motor=40
Isi_indikator_bensin=1.5
Harga_bahan_bakar=10000

total_jarak_pp=jarak + jarak

total_kebutuhan_bensin=total_jarak_pp / Konsumsi_motor

jumlah_bensin_yang_dibeli=total_kebutuhan_bensin - Isi_indikator_bensin

total_harga_bahan_bakar=jumlah_bensin_yang_dibeli * Harga_bahan_bakar

print("total jarak pp: ", total_jarak_pp, "km")
print("total kebutuhan bensin: ", total_kebutuhan_bensin, "liter")
print("jumlah bensin yang dibeli: ", jumlah_bensin_yang_dibeli, "liter")
print("total harga bahan bakar: ", total_harga_bahan_bakar, "rupiah")