#dictionary ini menyimpan daftar produk
produk = {"Laptop": 5500000, "Smartphone": 3000000, "Tablet": 2000000, "Smartwatch":
1500000, "Headphone": 500000 }

#ini variabel global untuk nantinya di isi dalam kode bberikutnya
umur =""
member = "" 
gadget = ""
jumlahUnit = ""
tawar =""

#ini fungsi diskon nah disini saya lupa logika dictionarinya
def diskon(jumlahUnit):
    produk["Laptop"] * jumlahUnit // 100

#ini fungsi tawar nah disini saya lupa logika dictionarinya
def tawar():
    nilai1 = ""
    nilai1 = input("masukkan nilai")
    if nilai1 > gadget:
        print("Penawaran ditolak. Harga asli digunakan.")
    else:
        print("Penawaran diterima")


while True :
    nama = input("masukkan nama anda : ")
    umur = input("masukkan umur anda : ")
    print("1. Laptop Rp", produk["Laptop"] )
    print("2. SmartPhone Rp", produk["Smartphone"])
    print("3. Tablet Rp", produk["Tablet"] )
    print("4. martWatch Rp", produk["Smartwatch"])
    print("5. Headphone Rp" , produk["Headphone"])
    gadget = input("ingin membeli apa? ")

    if umur < "17":
        print("maaf anda belum cukup umur untuk membeli produk ini")
        break
    elif gadget == "1":
        print("maaf anda belum cukup umur untuk membeli produk ini")
        break
    elif gadget == "5":
        print("maaf anda belum cukup umur untuk membeli produk ini")
        break
        

    member = input("apakah anda member ?(ya/tidak) : ")
    if member == "ya":
        diskon()
    jumlahUnit = input("ingin membeli berapa : ")
    tawar = input("apakah anda ingin menawar ?? (ya/ tidak) : ")
    if tawar == "ya":
        tawar()

    print("=== Struk Pembelian")
    print("nama :", nama)
    print("produk dibeli :", produk["Headphone"])
    print("jumlah unit :", jumlahUnit)
    print("Harga :", jumlahUnit)
    print("Sub total :", jumlahUnit)





