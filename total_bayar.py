print("Program menghitung total pembayaran")
print("Dengan diskon dinamis dari user !")

total_transaksi = float(input("Masukan total transasi : "))
total_diskon = total_transaksi * 0.1
total_transaksi_diskon = (total_transaksi - total_diskon)
total_pajak = total_transaksi_diskon * 0.11
total_bayar = (total_transaksi_diskon + total_pajak)

print("total transaksi anda : ",total_transaksi)
print("total diskon yang diterima (10%) : ",total_diskon)
print("total transaksi dengan diskon ",total_transaksi_diskon)
print("total pajak (11 %) : ",total_pajak)
print("total yang harus dibayar ",total_bayar)
