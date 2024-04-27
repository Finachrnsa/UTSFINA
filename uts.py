def hitung_usia():
    tahun_lahir = int(input("Masukkan tahun lahir Anda: "))
    tahun_sekarang = 2022
    usia = tahun_sekarang - tahun_lahir
    print("Usia Anda saat ini adalah", usia, "tahun")

def hitung_sisa_angsuran():
    total_angsuran = int(input("Masukkan total angsuran: "))
    angsuran_terbayar = int(input("Masukkan jumlah angsuran yang sudah dibayarkan: "))
    sisa_angsuran = total_angsuran - angsuran_terbayar
    print("Sisa tahun angsuran yang harus dibayar adalah", sisa_angsuran, "tahun")

def hitung_bmi():
    berat_badan = float(input("Masukkan berat badan (kg): "))
    tinggi_badan = float(input("Masukkan tinggi badan (m): "))
    bmi = berat_badan / (tinggi_badan ** 2)
    print("BMI Anda adalah", bmi)

while True:
    print("\nMenu Pilihan:")
    print("A. Hitung usia saat ini")
    print("B. Hitung sisa tahun angsuran")
    print("C. Hitung berat badan BMI")
    print("D. Keluar")

    pilihan = input("Pilih menu (A/B/C/D): ")

    if pilihan.upper() == "A":
        hitung_usia()
    elif pilihan.upper() == "B":
        hitung_sisa_angsuran()
    elif pilihan.upper() == "C":
        hitung_bmi()
    elif pilihan.upper() == "D":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih A, B, C, atau D.")