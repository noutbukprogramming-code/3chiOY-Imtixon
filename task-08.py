import json

with open("products.json", "r") as f:
    mahsulotlar = json.load(f)

nom = input("Mahsulot nomi: ")
miqdor = int(input("Yangi miqdor: "))

topildi = False

for mahsulot in mahsulotlar:
    if mahsulot["nom"] == nom:
        mahsulot["miqdor"] = miqdor
        topildi = True
        break

if topildi:
    with open("products.json", "w") as f:
        json.dump(mahsulotlar, f)
    print("Mahsulot miqdori yangilandi!")
else:
    print("Mahsulot topilmadi!")