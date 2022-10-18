print("Program menghitung luas trapesium")

lebar_bawah = float(input("Masukan lebar bawah trapesium :"))
lebar_atas = float(input("Masukan lebar atas trapesium :"))
tinggi = float(input("Masukan tinggi dari trapesium :"))

luas = ((lebar_atas + lebar_bawah) / 2) * tinggi

print("luas dari trapesium adalah :",luas)