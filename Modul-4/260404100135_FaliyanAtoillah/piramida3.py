while True:
    n = int(input("Masukkan angka (bilangan bulat positif): "))
    if n <= 0:
        print("Bilangan tidak boleh nol atau negatif, ulangi.")
    else:
        break

for i in range(1, n + 1):

    # Piramida angka pertama
    for j in range(1, i + 1):
        print(j, end="")

    # Spasi pemisah kedua piramida
    for k in range(1, 2 * (n - i) + 2):
        print(" ", end="")

    # Piramida angka kedua
    for j in range(i, 0, -1):
        print(j, end="")

    print()