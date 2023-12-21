# fungsi Awalan
def awalan():
    print("================================")
    print("         SELAMAT DATANG")
    print("    Program Luas Bangun Datar")
    print()
    print("Silahkan Pilih Rumus: ")
    print("1. Rumus Luas Persegi")
    print("2. Rumus Luas Persegi Panjang")
    print("3. Rumus Luas Segitiga")
    print("4. Rumus Luas Lingkaran")
    print("5. Rumus Luas Trapesium")
    print("================================")

    rumus = int(input("Masukkan Nomor rumus: "))
    if rumus == 1:
        print("Rumus Luas Persegi")
        def form_persegi():
            sisi = float(input("Masukkan nilai Sisi: "))
            return sisi**2
        print("Luas Persegi tersebut adalah: " + str(form_persegi()))
    elif rumus == 2:
        print("Rumus Luas Persegi Panjang")
        def form_perPanjang():
            panjang = float(input("Masukkan nilai Panjang: "))
            lebar = float(input("Masukkan nilai Lebar: "))
            return panjang*lebar
        print("Luas Persegi Panjang tersebut adalah: " + str(form_perPanjang()))
    elif rumus == 3:
        print("Rumus Luas Segitiga")
        def form_segitiga():
            alas = float(input("Masukkan nilai Alas: "))
            tinggi = float(input("Masukkan nilai Tinggi: "))
            return 1/2 *alas *tinggi
        print("Luas Segitiga tersebut adalah: " + str(form_segitiga()))
    elif rumus == 4:
        print("Rumus Luas Lingkaran")
        def form_lingkaran(ruas):
            ruas = float(input("Masukkan nilai Ruas: "))
            return 3.14 * ruas**2
        print("Luas Lingkaran tersebut adalah: " + str(form_lingkaran()))
    elif rumus == 5:
        print("Rumus Luas Trapesium")
        def form_trapesium():
            sisi_A = float(input("Masukkan nilai Sisi A: "))
            sisi_B = float(input("Masukkan nilai Sisi B: "))
            tinggi = float(input("Masukkan nilai Tinggi: "))
            return 1/2*(sisi_A+sisi_B)*tinggi
        print("Luas Trapesium tersebut adalah: " + str(form_trapesium()))
    else:
        print("Nomor yang anda masukkan tidak ada")                            
awalan()