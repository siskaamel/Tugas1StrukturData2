#konversi harga barang dari satuan ke dus
nama_barang =str(input("masukan nama barang : "))
harga_barangsatuan=int(input("masukan harga barang : "))
isi_barangsatudus=int(input("masukan jumlah satudus : "))

#perhitungan 
total_hargasatudus = harga_barangsatuan * 12
print(f'Harga_BarangSatuDus : {total_hargasatudus}')