#ÜL1
# from string import *
# vokaali=["a","e","u","i","ü","ö","ä"]
# konsonanti="qwrtypsdfghjklzxcvbnm"
# numbrid=digits
# märkid=punctuation
# v=k=n=m=t=0
# tekst=input("Sisend: ").lower()
# tekst_list=list(tekst)
# if tekst_list.index(" ")>0:
#     print("See on lause")
#     for s in tekst_list:
#         if s in vokaali:
#             v+=1
#         elif s in konsonanti:
#             k+=1
#         elif s in numbrid:
#             n+=1
#         elif s in märkid:
#             m+=1
#         elif s==" ":
#             t+=1
#     print(f"V: {v} \nK: {k} \nN: {m} \nT: {t}")
# else:
#     print(f"Kokku on {len(tekst_list)}")
#     if s in vokaali:
#        v+=1
#     elif s in konsonanti:
#        k+=1
#     print(f"Vokaali: {v} \nKonsonanti: {k}")
#ÜL2.1
# from os import lstat


# elemendid=[]
# for i in range(5):
#     name=input("Kirjuta nimi:")
#     elemendid.append(name)
# sorted_names=sorted(elemendid)
# print("Soorteritud nimed:", sorted_names)
# print("Viimane valitud nimi:", elemendid[-1])
# index=int(input("Kirjuta nime index kui tahad tema muuta (0-4):"))
# new_name=input("Kirjutage uus nimi:")
# if 0<= index <len(elemendid):
#     elemendid[index]=new_name
#     print("Uus loend nimega", elemendid)
# else:
#     print("Vale index")
# #ÜL2.2
# students=("Nastja","Arseni","Arseni","Nastja","Kirill")
# unique_studends=list(set(students))
# print("Loend ilma korduseta", unique_studends)
# #ÜL2.3
# vanus=43,13,54,43,65,24,15,34,51,87
# print(vanus)
# min_vanus=min(vanus)
# print(f"\nKõige noorem on {min_vanus}")
# max_vanus=max(vanus)
# print(f"Kõige vanem on {max_vanus}")
# summa=sum(vanus)
# print(f"Vanuste summa on {summa}")
# keskmine=summa/len(vanus)
# print(f"Keskmine vanus on {keskmine}")
#ÜL5
def swap_elements(lst, n):
    lenght=len(lst)
    if lenght<2:
        print("Loendis peab olema minimum kaks elementi!!!")
        return lst
n=min(n,lenght//2)
for i in range(n):
    lst[i], lst[-(i+1)]=lst[-(i-1)], lst[i]
return lst
user_list=input("Siselda elemendid"...)