def tashqi_funksiya(koyfitsent):
    def ichki_funksiya(qiymat):
        return koyfitsent * qiymat
    return ichki_funksiya


koyfitsent = 4
qiymat = 7

funksiya = tashqi_funksiya(koyfitsent)
natija = funksiya(qiymat)

print(f"Natija: {natija}")