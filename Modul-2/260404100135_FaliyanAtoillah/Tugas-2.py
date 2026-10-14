total_belanja = int(input("Masukkan total belanja: Rp"))

if total_belanja % 100000 == 0:
    total_diskon = total_belanja * 100/100
    total_bayar = total_belanja - total_diskon
elif total_belanja % 50000 == 0:
    total_diskon = total_belanja * 50/100
    total_bayar = total_belanja - total_diskon
elif total_belanja % 10000 == 0:
    total_diskon = total_belanja * 20/100
    total_bayar = total_belanja - total_diskon
elif total_belanja >= 200000:
    total_diskon = total_belanja * 10/100
    total_bayar = total_belanja - total_diskon
else:
    total_bayar = total_belanja

print("Total belanja awal:", "Rp", total_belanja)
print("Total harga akhir:", "Rp", total_bayar)

status_poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"
print("Status poin:", status_poin)
