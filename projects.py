
import random
from utils import add_record, delete_record

FILENAME = "data.txt"

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

def load_from_file():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                key, tagam_str, baga = line.strip().split("|")
                tagamdar = [tuple(t.split(",")) for t in tagam_str.split(";")]
                tapsyrys_tarihy[key] = {"tagamdar": tagamdar, "baga": int(baga)}
    except FileNotFoundError:
        pass

def save_to_file():
    with open(FILENAME, "w", encoding="utf-8") as f:
        for key, val in tapsyrys_tarihy.items():
            tagam_str = ";".join([f"{t[0]},{t[1]}" for t in val["tagamdar"]])
            f.write(f"{key}|{tagam_str}|{val['baga']}\n")

def bar_menudy_koru():
    print("\nБарлық мәзір:")
    for i, t in enumerate(MENYU, 1):
        print(f"{i}. {t[0]} - {t[1]} ккал - {t[3]} тг | Құрамы: {t[2]}")

def tagam_izdeu():
    soz = input("Ізделетін тағамның атын немесе түрін жазыңыз: ").lower()
    tabylgan = []
    for i, t in enumerate(MENYU, 1):
        if soz in t[0].lower() or soz in t[2].lower():
            tabylgan.append((i, t))
    if tabylgan:
        print("Табылған тағамдар:")
        for i, t in tabylgan:
            print(f"{i}. {t[0]} - {t[1]} ккал - {t[3]} тг | Құрамы: {t[2]}")
    else:
        print("Мұндай тағам табылмады.")

def tapsyrys_qosu():
    while True:
        bar_menudy_koru()
        nums = input("Таңдаған тағамдардың нөмірін үтір арқылы жазыңыз: ").split(",")
        tapsyrys = []
        baga = 0
        for n in nums:
            try:
                idx = int(n.strip()) - 1
                if 0 <= idx < len(MENYU):
                    tapsyrys.append(MENYU[idx])
                    baga += MENYU[idx][3]
            except:
                continue

        if not tapsyrys:
            print("Ешқандай тағам таңдалмады. Қайта енгізіңіз.")
            continue

        print("\nСіздің тапсырысыңыз:")
        for t in tapsyrys:
            print("-", t[0], "-", t[1], "ккал -", t[3], "тг")

        rastau = input("Тапсырысты растау керек пе? (иә/жоқ): ").lower()
        if rastau == "иә":
            nomer = str(random.randint(1000, 9999))
            add_record(tapsyrys_tarihy, nomer, {"tagamdar": [(t[0], t[3]) for t in tapsyrys], "baga": baga})
            save_to_file()
            print(f"Тапсырыс қабылданды! Нөмірі: {nomer}, Жалпы баға: {baga} тг")
            break
        else:
            print("Тапсырыс беруді болдырмаймыз. Мәзірге қайта ораламыз.")
            break

def tapsyrys_qosu():
    while True:
        bar_menudy_koru()
        nums = input("Таңдаған тағамдардың нөмірін үтір арқылы жазыңыз: ").split(",")
        tapsyrys = []
        baga = 0
        for n in nums:
            try:
                idx = int(n.strip()) - 1
                if 0 <= idx < len(MENYU):
                    tapsyrys.append(MENYU[idx])
                    baga += MENYU[idx][3]
            except:
                continue

        if not tapsyrys:
            print("Ешқандай тағам таңдалмады. Қайта енгізіңіз.")
            continue

        print("\nСіздің тапсырысыңыз:")
        for t in tapsyrys:
            print("-", t[0], "-", t[1], "ккал -", t[3], "тг")

        rastau = input("Тапсырысты растау керек пе? (иә/жоқ): ").lower()
        if rastau == "иә":
            nomer = str(random.randint(1000, 9999))
            # Дайындалу уақыты 5-15 минут
            dayyndau_uakyty = random.randint(5, 15)
            add_record(tapsyrys_tarihy, nomer, {
                "tagamdar": [(t[0], t[3]) for t in tapsyrys],
                "baga": baga,
                "uakyty": dayyndau_uakyty
            })
            save_to_file()
            print(f"Тапсырыс қабылданды! Нөмірі: {nomer}, Жалпы баға: {baga} тг")
            print(f"Дайындалу уақыты: {dayyndau_uakyty} минут")  # Тапсырыс бергенде шығады
            break
        else:
            print("Тапсырыс беруді болдырмаймыз. Мәзірге қайта ораламыз.")
            break
def tapsyrys_koru():
    nomer = input("Тапсырыс нөмірін енгізіңіз: ")
    if nomer in tapsyrys_tarihy:
        info = tapsyrys_tarihy[nomer]
        print("Тапсырыс №", nomer)
        for t, b in info["tagamdar"]:
            print("-", t, "-", b, "тг")
        print("Жалпы баға:", info["baga"])
        # Қалған уақытты кездейсоқ шығару
        remaining = random.randint(1, info["uakyty"])
        print(f"Қалған уақыт шамамен: {remaining} минут")
    else:
        print("Мұндай тапсырыс жоқ.")


def tapsyrys_ozh():
    nomer = input("Жою үшін тапсырыс нөмірін енгізіңіз: ")
    if nomer in tapsyrys_tarihy:
        delete_record(tapsyrys_tarihy, nomer)
        save_to_file()
        print("Тапсырыс жойылды.")
    else:
        print("Мұндай тапсырыс жоқ.")

load_from_file()

while True:
    print("\n^ Басты мәзір ^")
    print("1. Барлық мәзірді көру")
    print("2. Тағам іздеу")
    print("3. Тапсырыс беру")
    print("4. Тапсырысты көру")
    print("5. Тапсырысты жою")
    print("6. Барлық тапсырыстар")
    print("7. Шығу")

    choice = input("Таңдауыңызды енгізіңіз: ")
    if choice == "1":
        bar_menudy_koru()
    elif choice == "2":
        tagam_izdeu()
    elif choice == "3":
        tapsyrys_qosu()
    elif choice == "4":
        tapsyrys_koru()
    elif choice == "5":
        tapsyrys_ozh()
    elif choice == "6":
        for k, v in tapsyrys_tarihy.items():
            print("№", k, ":", v)
    elif choice == "7":
        print("Бағдарлама аяқталды.")
        break
    else:
        print("Қате таңдау")
