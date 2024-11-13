def hitung_total(jumlah_barang):
    total_harga =0
    for a in range (1, jumlah_barang +1):
        harga = float(input(f"masukan harga barang ke-{a}: "))
        total_harga += harga
    return total_harga
jumlah_barang = int(input("masukan jumlah barang:"))
total = hitung_total(jumlah_barang)
print(f"total dari{jumlah_barang} barang adalah : Rp{total}")