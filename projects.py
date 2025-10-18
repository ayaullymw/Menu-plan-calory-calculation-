import random
restoran_atauy = "FitFood"
print("Фитнес-ресторан:", restoran_atauy, "\n")
MENYU = (
    ("Протеинді смузи", 180, "сүт, протеин, банан", 1200),
    ("Жасыл смузи", 150, "шпинат, алма, киви", 1100),
    ("Омлет ақуыздан", 200, "жұмыртқа ақуызы, көкөніс", 1000),
    ("Тауық еті мен көкөніс", 350, "тауық, брокколи, сәбіз", 1800),
    ("Киноа салаты", 250, "киноа, авокадо, қызанақ", 1500),
    ("Жеміс салаты", 120, "банан, алма, киви", 900),
    ("Таңғы ас коктейлі", 220, "сүт, сұлы, жидектер", 1300),
    ("Йогурт + жидектер", 180, "йогурт, малина, қарақат", 1200),
    ("Тауық салаты", 300, "тауық, көкөніс, авокадо", 1700),
    ("Күріш пен балық", 400, "күріш, балық, көкөніс", 2200),
    ("Тауық филе стейк", 360, "тауық, дәмдеуіштер", 2000),
    ("Қарақұмық салаты", 220, "қарақұмық, көкөніс, қызанақ", 1400),
    ("Протеинді печенье", 150, "жұмыртқа, протеин, сұлы", 800),
    ("Сорпа көкөніс", 180, "қырыққабат, сәбіз, пияз", 900),
    ("Көкөніс омлет", 200, "жұмыртқа, көкөніс", 1100),
    ("Тауық бутерброд", 250, "тауық, нан, көкөніс", 1300),
    ("Авокадо салаты", 230, "авокадо, көкөніс, лимон", 1500),
    ("Йогурт смузи", 190, "йогурт, банан, жидектер", 1200)
)
tapsyrys_tarihy = {}

def tapsyrys_beru():
    while True:
        print("Меню:")
        for i, tagam in enumerate(MENYU, 1):
            print(i, tagam[0], "-", tagam[1], "kkal", "-", tagam[3], "tg", "| Құрамы:", tagam[2])

        tapsyrys_nomerleri = input("Таңдаған тағамдардың нөмірлерін үтір арқылы жазыңыз: ")
        tapsyrys_nomerleri = tapsyrys_nomerleri.split(",")
        tapsyrys_tizimi = []

        for n in tapsyrys_nomerleri:
            tapsyrys_tizimi.append(n.strip())

        tapsyrys = []
        jalpy_baga = 0
        jalpy_kaloriya = 0

        for n in tapsyrys_tizimi:
            if n.isdigit():
                indeks = int(n) - 1
                if 0 <= indeks < len(MENYU):
                    tapsyrys.append(MENYU[indeks])
                    jalpy_baga += MENYU[indeks][3]
                    jalpy_kaloriya += MENYU[indeks][1]

        if not tapsyrys:
            print("Ешқандай тағам табылмады, қайта енгізіңіз.")
            continue

        print("\nСіздің тапсырысыңыз:")
        for tagam in tapsyrys:
            print("-", tagam[0], "-", tagam[1], "kkal", "-", tagam[3], "tg", "| Құрамы:", tagam[2])
        print("Жалпы калория:", jalpy_kaloriya, "kkal")
        print("Жалпы бағасы:", jalpy_baga, "tg")

        rastau = input("\nТапсырыс қабылдаймыз ба? (иә/жоқ): ").lower()
        if rastau == "иә":
            nomer = random.randint(1000, 9999)
            dayyndau_uakyty = random.randint(5, 15)
            tapsyrys_tarihy[nomer] = {
                "tagamdar": [(t[0], t[3]) for t in tapsyrys],
                "uakyty": dayyndau_uakyty,
                "baga": jalpy_baga
            }
            print("Тапсырыс қабылданды! Нөмірі:", nomer)
            print("Дайындалу уақыты шамамен", dayyndau_uakyty, "минут.")
            break
        else:
            print("Менюді қайта таңдаңыз.")

def tapsyrys_koru():
    if not tapsyrys_tarihy:
        print("\nӘзірше ешқандай тапсырыс жоқ.")
        return

    nomer = input("Тапсырыс нөмірін енгізіңіз: ")
    if nomer.isdigit():
        nomer = int(nomer)
        if nomer in tapsyrys_tarihy:
            info = tapsyrys_tarihy[nomer]
            print("\nТапсырыс №", nomer)
            print("Таңдалған тағамдар:")
            for tagam_ati, bagasy in info["tagamdar"]:
                print("-", tagam_ati, "-", bagasy, "tg")
            print("Жалпы бағасы:", info["baga"], "tg")
            print("Қалған уақыт шамамен:", random.randint(1, info["uakyty"]), "минут")
        else:
            print("Мұндай тапсырыс табылмады.")
    else:
        print("Қате нөмір енгізілді.")

while True:
    print("\n^ Басты мәзір ^")
    print("1. Меню көру")
    print("2. Тапсырыс беру")
    print("3. Тапсырысты көру")
    print("4. Шығу")

    tandau = input("Таңдауыңызды енгізіңіз: ")

    if tandau == "1":
        print("\nАс мәзірі:")
        for i, tagam in enumerate(MENYU, 1):
            print(i, tagam[0], "-", tagam[1], "kkal", "-", tagam[3], "tg", "| Құрамы:", tagam[2])

    elif tandau == "2":
        tapsyrys_beru()

    elif tandau == "3":
        tapsyrys_koru()

    elif tandau == "4":
        print("Рахмет! Келесі жолы күтеміз!")
        break

    else:
        print("Қате таңдау. Қайта енгізіңіз.")

