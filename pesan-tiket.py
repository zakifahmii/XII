def line():
    print("=========================")

print("Selamat Datang di Hotel Del Luna")

print("Tipe Kamar: Superior, Deluxe, Premium")
room_type = input("Masukkan Tipe Kamar: ")
lama_inap = int(input("Masukkan Lama Anda Menginap: "))

if room_type == "Superior":
    if lama_inap <= 2:
        price = 200000 * lama_inap
    elif lama_inap <= 4:
        price = 200000 * lama_inap
    elif lama_inap >= 5:
        price = 600000
elif room_type == "Deluxe":
    if lama_inap <= 2:
        price = 150000 * lama_inap
    elif lama_inap >= 4:
        price = 150000 * lama_inap
elif room_type == "Premium":
    if lama_inap <= 2:
        price = 100000 * lama_inap
    elif lama_inap >= 4:
        price = 100000 * lama_inap

line()
print("Kamar",room_type,"telah dipilih, dengan lama inap selama",lama_inap,"hari")
print("Harga kamar sebesar",price,"Rupiah")
