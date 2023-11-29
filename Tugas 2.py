# Fathur Rahman
# 2309076021
# Mengurutkan bilagan

def susun_bilangan():
    bilangan = [19, 5, 26, 84, 57, 81, 9, 69, 43]
    return bilangan

# Ascending(Terkecil ke terbesar)
bilangan = susun_bilangan()
bilangan_terurut = sorted(bilangan)
print("Bilangan setelah disusun secara ascending:", bilangan_terurut)

# Descending (Terbesar ke terkecil)
bilangan_terurut = sorted(bilangan, reverse=True)
print("Bilangan setelah disusun secara descending:", bilangan_terurut)
