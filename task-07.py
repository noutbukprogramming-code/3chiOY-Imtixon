import csv

mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]

with open("products.csv", "w") as f:
    data = csv.writer(f)

    data.writerow(["nom", "narx", "soni"])
    data.writerows(mahsulotlar)

print("Ma'lumotlar products.csv fayliga yozildi.")