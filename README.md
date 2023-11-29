# Fathur Rahman
# 2309076021
# program untuk mengetahui bilangan ganjil atau genap dan mengalikan dengan bilangan terdekatnya

bilangan = int(input("Input Bilangan: "))
def cek_dan_perkalian(bilangan):
    if bilangan % 2 == 0:  # Jika bilangan genap
        print(f"{bilangan} adalah bilangan genap")
    else:  # Jika bilangan ganjil
        print(f"{bilangan} adalah bilangan ganjil")
    return bilangan

bilangan_berikutnya = bilangan + 1
hasil = bilangan*bilangan_berikutnya
print(f"Hasil perkalian dari {bilangan} dengan bilangan berikutnya({bilangan_berikutnya}) adalah {hasil}")
