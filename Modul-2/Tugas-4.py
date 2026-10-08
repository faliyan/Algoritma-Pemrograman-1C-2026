pin = int(input("masukkan Pin 3 digit :"))
jam = int(input("masukkan jam kedatangan (0-23):"))

digit_pertama = pin // 100
digit_kedua = (pin // 10) % 10
digit_ketiga = pin % 10

print("Digit pertama:", digit_pertama)
print("Digit kedua:", digit_kedua)
print("Digit ketiga:", digit_ketiga)

if pin % 5 == 0:
    if jam < 12:
        print("Garasi Pagi Terbuka")
    else:
        print("Garasi Malam Terbuka, Lampu Dinyalakan")

elif pin % 2 == 0:
    if digit_pertama + digit_ketiga == digit_kedua:
        print("Garasi VIP Terbuka Khusus Bos")
    else:
        print("Kode Genap Ditolak, Alarm Berbunyi!")

else:
    print("Akses Ditolak Sepenuhnya")

status_cctv = "Mode Malam Merekam" if jam > 18 else "Mode Siang Standby"
print(status_cctv)
