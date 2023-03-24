"tyyyiyiuioyi"
import random


def p1():
 p = int(input("Введите число:"))
 l = [1,2,3,4,5]
 if p in l:
    print(l, p, "Поздравляю, Вы угадали число!")
 else:
    print(l, p, "Нет такого числа!")


def p2():

 l = [1,2,3,4,4,5,5,6,7,7,7,7,7,7]
 print(*filter(lambda x : l.count(x) > 1, l))

def p3():

 ned = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
 d = int(input("сколько выходных?"))
 for i in ned:
    print("Рабочие", *ned[:-d])
    print("Выходные", *ned[:-d])
    break

def p4():

 from random import sample
 cp1 = ("Петров", "Иванов", "Кашин")
 cp2 = ("Махичев", "Лопухов", "Селюнина")
 sport = tuple(random.sample(cp1, 3)+random.sample(cp2, 3))
 print("Другая группа", *cp1)
 print("Моя группа", *cp2)
 print(*sport, len(sport))
 if "Петров" in sport:
     print("Фамилия Петров входит в список секции раз:", sport.count("Петров"))
 else:
     print ("Петрова нет в секции")

def p5():
    countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин",
                      "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерладны": "Амстердам",
                      "Франция": "Париж", "Белоруссия": "Минск", "Болгария": "София", "Польша": "Варшава",
                      "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                      "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(countries_dict)
    for i in countries_dict:
        a = input("Введите страну")
        print(countries_dict[i])
        for key in sorted(countries_dict):
            print(key, ' - ', countries_dict[key])



def p6():
    a = input('Введите слово')
    points_ru = {1: 'АВЕИНОРСТ',
                 2: 'ДКЛМПУ',
                 3: 'БГЁЬЯ',
                 4: 'ЙЫ',
                 5: 'ЖЗХЦЧ',
                 8: 'ШЭЮ',
                 10: 'ФЩЪ'}
    print(a, ' ', sum(points_ru))

def p7():
    zk = set()
    sp = []
    stud = {"Петров": {"Английский","Китайский"},
            "Иванов": {"Китайский"},
            "Кашин": {"Французский","Итальянский"},
            "Махичев": {"Испанский"},
            "Лопухов": {"Итальянский", "Испанский"},
            "Селюнина": {"Японский"}}
    for stud, zk in stud.items():
        zk.update(zk)
        if "Китайский" in zk:
            sp.append(stud)
            sorted_zk = sorted(list(zk))
            print(sp)
            print(sorted_zk)

p7()


