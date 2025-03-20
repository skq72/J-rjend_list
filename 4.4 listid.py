#ÜL1
from string import *
vokaali=["a","e","u","i","ü","ö","ä"]
konsonanti="qwrtypsdfghjklzxcvbnm"
numbrid=digits
märkid=punctuation
v=k=n=m=t=0
tekst=input("Sisend: ").lower()
tekst_list=list(tekst)
if tekst_list.index(" ")>0:
    print("See on lause")
    for s in tekst_list:
        if s in vokaali:
            v+=1
        elif s in konsonanti:
            k+=1
        elif s in numbrid:
            n+=1
        elif s in märkid:
            m+=1
        elif s==" ":
            t+=1
    print(f"V: {v} \nK: {k} \nN: {m} \nT: {t}")
else:
    print(f"Kokku on {len(tekst_list)}")
    if s in vokaali:
       v+=1
    elif s in konsonanti:
       k+=1
    print(f"Vokaali: {v} \nKonsonanti: {k}")



#ÜL2.1
from os import lstat
elemendid=[]
for i in range(5): #Запрос 5 имён
    name=input("Kirjuta nimi:")
    elemendid.append(name) #Добавление а список
sorted_names=sorted(elemendid) # Сортировка по алфовиту
print("Soorteritud nimed:", sorted_names)
print("Viimane valitud nimi:", elemendid[-1]) #Показываем последнее имя
index=int(input("Kirjuta nime index kui tahad tema muuta (0-4):")) #Запрос на изменение имени
new_name=input("Kirjutage uus nimi:")
if 0<= index <len(elemendid): #меняем имя в списке
    elemendid[index]=new_name#На новое
    print("Uus loend nimega", elemendid)#Вывод нового списка
else:
    print("Vale index") #Вывод сообщения об ошибке

#ÜL2.2
students=("Nastja","Arseni","Arseni","Nastja","Kirill")
unique_studends=list(set(students))# Убибараем повторы
print("Loend ilma korduseta", unique_studends) #Список без повторов

#ÜL2.3
vanus=43,13,54,43,65,24,15,34,51,87 #список
print(vanus)
min_vanus=min(vanus) #мин возраст из списка
print(f"\nKõige noorem on {min_vanus}")
max_vanus=max(vanus)#макс возраст из списка
print(f"Kõige vanem on {max_vanus}")
summa=sum(vanus)#сумма возрастов
print(f"Vanuste summa on {summa}")
keskmine=summa/len(vanus)#средний всех возрастов
print(f"Keskmine vanus on {keskmine}")


#ÜL4
loend={"1":"Tallinn", "2":"Narva,Narva-Jõesu", "3":"Kohtla-Järve", "4":"Ida-Virumaa, Lääne-Virumaa, Jõgevamaa", "5":"Tartu", "6":"Tartumaa, Põlvamaa, Võrumaa, Valgamaa", "7":"Viljandimaa, Järvamaa, Harjumaa, Raplamaa", "8":"Pärnumaa", "9":" Läänemaa, Hiiumaa, Saaremaa"}
olge_kodus=["1","2","3"] #Уезды при которых нужно писать "Olge kodus"
index=input("Siseta posti index (5 numbrid): ") #Запрос индекса
if len(index) == 5 and index.isdigit(): #Проверка типа и длинны данных
    first_digit = index[0]
    if first_digit in loend:
        print(f"See indeks on piirkonnale omane: {loend[first_digit]}")
        if first_digit in olge_kodus: # В зависимости от уездв пишем сообщение
            print("Olge kodus!")
        else:
            print("Kanna maski!")
    else:
        print("´Tundmatu piirkond!")
else:
    print("Viga! Indexis peab olema 5 numbri!") # Сообщаем об ошибке если написано больше или меньше цифр


#ÜL15
numbrid = [1, 2, 3, 4]
estonian = ["üks", "kaks", "kolm", "neli"]
english = ["one", "two", "three", "four"]
italian = ["uno", "due", "tre", "quattro"]
numbrid.extend([5, 6]) # Добовляем два элемента
estonian.extend(["viis", "kuus"])
print(f"{'Arv:':<10}{'Eesti':<10}{'English':<10}{'Italian':<10}") # Выводим таблицу
for i in range(min(len(numbrid), len(estonian), len(english), len(italian))): 
    print(f"{numbrid[i]:<10}{estonian[i]:<10}{english[i]:<10}{italian[i]:<10}")
if "tre" in italian: # Проверяем есть ли TRE в итальянском языке
    print("\nSõna (tre) on Itaalia loendis.")
else:
    print("\nSõna (tre) ei ole Itaalia loendis.")
all_words = list(map(str, numbrid)) + estonian + english + italian  # Объеденяем и сортируем
all_words.sort()
print("\nKõik soorteritud elemendid.") # Выводим список
print(all_words)


#ÜL5
sisend = input("Sisestage numbrid komadega eraldatult: ") #Ввод чисел
numbrid = list(map(int, sisend.split(',')))#Переобразуем в список
if len(numbrid) < 2:# Проверка колво элементов
    print("Listis peab olema vähemalt 2 elementi!")
    exit()
n = int(input("Mitu elementi soovite vahetada?: "))
if n > len(numbrid) // 2:
    print("Vahetatavate elementide arv ei saa olla suurem kui pool listi pikkusest!")
    exit()
pikkus = len(numbrid) #Определяем длину списка
for i in range(n):
    numbrid[i], numbrid[pikkus-1-i] = numbrid[pikkus-1-i], numbrid[i]
print("Muutunud list:", numbrid) # Выводим список


#ÜL11
n = int(input("Sisestage tähtede arv: ")) #Запрос колво букв
tähed=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'][:n]
korduvad_tähed = [tähed[i] * (i + 1) for i in range(n)]#Создаём список где каждая буква повторяется i+1 раз
print("Esimene järjend:", tähed) # Выводим список nr1
print("Teine järjend:", korduvad_tähed)# Выводим список nr2