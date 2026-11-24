class Barang:
    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    # Property
    @property
    def nama(self):
        return self.__nama

    @property
    def harga(self):
        return self.__harga

    @property
    def stok(self):
        return self.__stok

    # Setter
    @stok.setter
    def stok(self, jumlah):
        if jumlah >= 0:
            self.__stok = jumlah
        else:
            print("Stok tidak boleh negatif!")

    # Method
    def tampilkan_barang(self):
        print(f"{self.__nama} - Rp{self.__harga} - Stok: {self.__stok}")

    # Static Method
    @staticmethod
    def format_rupiah(angka):
        return "Rp" + format(angka, ",").replace(",", ".")


class Kasir:
    jumlah_transaksi = 0

    def __init__(self, nama_kasir):
        self.nama_kasir = nama_kasir
        self.keranjang = []

    # Method menambahkan barang
    def tambah_barang(self, barang, jumlah):
        if jumlah > 0 and jumlah <= barang.stok:
            self.keranjang.append((barang, jumlah))
            barang.stok -= jumlah
            print("Barang berhasil ditambahkan!")
        else:
            print("Jumlah tidak valid atau stok tidak cukup!")

    # Menghitung total belanja
    def hitung_total(self):
        total = 0
        for barang, jumlah in self.keranjang:
            total += barang.harga * jumlah
        return total

    # Method pembayaran
    def pembayaran(self, uang):
        total = self.hitung_total()

        if uang >= total:
            kembalian = uang - total
            Kasir.jumlah_transaksi += 1

            print("\n===== STRUK PEMBELIAN =====")
            print("Kasir:", self.nama_kasir)

            for barang, jumlah in self.keranjang:
                subtotal = barang.harga * jumlah
                print(barang.nama, "x", jumlah,
                      "=", Barang.format_rupiah(subtotal))

            print("Total:", Barang.format_rupiah(total))
            print("Bayar:", Barang.format_rupiah(uang))
            print("Kembalian:", Barang.format_rupiah(kembalian))
            print("===========================")

            self.keranjang.clear()
        else:
            print("Uang pembayaran kurang!")

    # Class Method
    @classmethod
    def total_transaksi(cls):
        return cls.jumlah_transaksi


# Membuat object barang
barang1 = Barang("Buku", 5000, 20)
barang2 = Barang("Pensil", 3000, 30)
barang3 = Barang("Penghapus", 2000, 25)

# Membuat object kasir
kasir = Kasir("Diny")

daftar_barang = [barang1, barang2, barang3]

# Menu program
while True:
    print("\n===== SISTEM KASIR =====")
    print("1. Lihat Barang")
    print("2. Tambah ke Keranjang")
    print("3. Lihat Total Belanja")
    print("4. Pembayaran")
    print("5. Jumlah Transaksi")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("\nDAFTAR BARANG")
        for i, barang in enumerate(daftar_barang, 1):
            print(i, end=". ")
            barang.tampilkan_barang()

    elif pilihan == "2":
        for i, barang in enumerate(daftar_barang, 1):
            print(i, barang.nama)

        pilih = int(input("Pilih nomor barang: "))

        if 1 <= pilih <= len(daftar_barang):
            jumlah = int(input("Masukkan jumlah: "))
            kasir.tambah_barang(daftar_barang[pilih - 1], jumlah)
        else:
            print("Nomor barang tidak tersedia!")

    elif pilihan == "3":
        total = kasir.hitung_total()
        print("Total belanja:",
              Barang.format_rupiah(total))

    elif pilihan == "4":
        total = kasir.hitung_total()

        if total > 0:
            print("Total pembayaran:",
                  Barang.format_rupiah(total))
            uang = int(input("Masukkan uang pembayaran: Rp"))
            kasir.pembayaran(uang)
        else:
            print("Keranjang masih kosong!")

    elif pilihan == "5":
        print("Jumlah transaksi:",
              Kasir.total_transaksi())

    elif pilihan == "6":
        print("Terima kasih sudah berbelanja!")
        break

    else:
        print("Pilihan tidak tersedia!")