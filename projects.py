import random
import matplotlib.pyplot as plt
from utils import add_record, delete_record

FILENAME = "data.txt"

class Food:
    def __init__(self, name, calories, protein, fat, carbs, price):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.price = price

    def info(self):
        return f"{self.name}: {self.calories} ккал, {self.protein}г ақуыз, {self.fat}г май, {self.carbs}г көмірсу, {self.price}тг"

class SpecialFood(Food):
    def __init__(self, name, calories, protein, fat, carbs, price):
        super().__init__(name, calories, protein, fat, carbs, price)


    def info(self):
        return super().info()


MENYU = [
    Food("Протеинді смузи", 180, 20, 5, 25, 1200),
    Food("Жасыл смузи", 150, 5, 2, 30, 1100),
    Food("Омлет ақуыздан", 200, 15, 10, 5, 1000),
    Food("Тауық еті мен көкөніс", 350, 30, 10, 40, 1800),
    Food("Киноа салаты", 250, 8, 12, 35, 1500),
    Food("Жеміс салаты", 120, 2, 1, 28, 900),
    Food("Таңғы ас коктейлі", 220, 12, 4, 32, 1300),
    Food("Йогурт + жидектер", 180, 10, 3, 20, 1200),
    Food("Тауық салаты", 300, 25, 8, 15, 1700),
    Food("Күріш пен балық", 400, 35, 12, 50, 2200),
    Food("Тауық филе стейк", 360, 32, 10, 10, 2000),
    Food("Қарақұмық салаты", 220, 10, 8, 30, 1400),
    Food("Протеинді печенье", 150, 15, 5, 10, 800),
    Food("Сорпа көкөніс", 180, 5, 2, 15, 900),
    Food("Көкөніс омлет", 200, 12, 8, 5, 1100),
    Food("Тауық бутерброд", 250, 20, 5, 25, 1300),
    Food("Авокадо салаты", 230, 8, 12, 20, 1500),
    Food("Йогурт смузи", 190, 10, 3, 25, 1200)
]

tapsyrys_tarihy = {}

def load_from_file():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) != 3:
                    continue
                key, tagam_str, baga = parts
                tagamdar = [tuple(t.split(",")) for t in tagam_str.split(";")]
                tapsyrys_tarihy[key] = {"tagamdar": tagamdar, "baga": int(baga)}
    except FileNotFoundError:
        pass

def save_to_file():
    with open(FILENAME, "w", encoding="utf-8") as f:
        for key, val in tapsyrys_tarihy.items():
            tagam_str_list = []
            for t in val["tagamdar"]:
                # 5 элемент болмаса 0 қосамыз
                t_extended = list(t) + [0]*(5-len(t))
                tagam_str_list.append(",".join(map(str, t_extended)))
            tagam_str = ";".join(tagam_str_list)
            f.write(f"{key}|{tagam_str}|{val['baga']}\n")

def bar_menudy_koru():
    print("\nБарлық мәзір:")
    for i, t in enumerate(MENYU, 1):
        print(f"{i}. {t.info()}")


def tagam_izdeu():
    soz = input("Ізделетін тағамның атын немесе түрін жазыңыз: ").lower()
    tabylgan = []
    for i, t in enumerate(MENYU, 1):
        if soz in t.name.lower():
            tabylgan.append((i, t))
    if tabylgan:
        print("Табылған тағамдар:")
        for i, t in tabylgan:
            print(f"{i}. {t.info()}")
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
                    baga += MENYU[idx].price
            except:
                continue

        if not tapsyrys:
            print("Ешқандай тағам таңдалмады. Қайта енгізіңіз.")
            continue

        print("\nСіздің тапсырысыңыз:")
        for t in tapsyrys:
            print("-", t.info())

        rastau = input("Тапсырысты растау керек пе? (иә/жоқ): ").lower()
        if rastau == "иә":
            nomer = str(random.randint(1000, 9999))
            dayyndau_uakyty = random.randint(5, 15)
            add_record(tapsyrys_tarihy, nomer, {
                "tagamdar": [(t.name, t.price, t.protein, t.fat, t.carbs) for t in tapsyrys],
                "baga": baga,
                "uakyty": dayyndau_uakyty
            })
            save_to_file()
            print(f"\nТапсырыс қабылданды! Нөмірі: {nomer}, Жалпы баға: {baga} тг")
            print(f"Дайындалу уақыты: {dayyndau_uakyty} минут")
            break
        else:
            print("Тапсырыс беруді болдырмаймыз. Мәзірге қайта ораламыз.")
            break

def show_graph():
    nomer = input("График шығару үшін тапсырыс нөмірін енгізіңіз: ")
    if nomer not in tapsyrys_tarihy:
        print("Мұндай тапсырыс жоқ.")
        return

    info = tapsyrys_tarihy[nomer]
    tagamdar = info["tagamdar"]  

    total_protein = sum([int(t[2]) for t in tagamdar])
    total_fat = sum([int(t[3]) for t in tagamdar])
    total_carbs = sum([int(t[4]) for t in tagamdar])
    total_calories = sum([int(t[2])*4 + int(t[3])*9 + int(t[4])*4 for t in tagamdar])

    labels = ["Ақуыз (г)", "Май (г)", "Көмірсу (г)"]
    values = [total_protein, total_fat, total_carbs]

    plt.figure(figsize=(6, 6))
    colors = ["#9AE3CA", "#EDE69A", "#CAABED"]
    explode = (0.05, 0.05, 0.05)
    plt.pie(values, labels=labels,
            autopct=lambda p: f"{p:.1f}%\n({int(p*sum(values)/100)}г)",
            startangle=140, shadow=True, explode=explode, colors=colors)

    plt.title(f"Сіздің таңдаған тағамдарыңыздың ақуыз, май, көмірсу үлесі\nЖалпы калория: {total_calories} ккал", fontsize=14)
    plt.show()


def tapsyrys_koru():
    nomer = input("Тапсырыс нөмірін енгізіңіз: ")
    if nomer in tapsyrys_tarihy:
        info = tapsyrys_tarihy[nomer]
        print("Тапсырыс №", nomer)
        for t in info["tagamdar"]:
            print(f"- {t[0]}: {t[2]}г ақуыз, {t[3]}г май, {t[4]}г көмірсу, {t[1]}тг")
        print("Жалпы баға:", info["baga"])
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
    print("7. График шығару")
    print("8. Шығу")

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
        show_graph()
    elif choice == "8":
        print("Бағдарлама аяқталды.")
        break
    else:
        print("Қате таңдау")
