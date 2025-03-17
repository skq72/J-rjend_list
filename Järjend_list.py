sõne="Programmeerimine"
print(sõne)
list_sõne=list(sõne)
print(list_sõne)
print(f"Viies täht: {list_sõne[4]}")
print(f"Sõnes on {len(sõne)}t")
elemendid=[]
#APPEND
for i in range(5):
    elemendid.append(input("{i+1}. element: "))  #Добавляет элемент в конец списка
print(elemendid)
for e in elemendid:
    print(e)
#EXTEND
list_sõne. extend(elemendid)
print(list_sõne)
print(elemendid)
#INSERT
elemendid.insert(0,"A")
print(elemendid)
#REMOVE
elemendid.remove("A")
print(elemendid)
#POP
elemendid.pop(0)
elemendid.pop()
print(elemendid)
#INDEX
ind=list_sõne.index("r")
print(f"Täht r on {ind}-indeksiga")
#COUNT
k=list_sõne.count("r")
print(f"Täht r kohtume {k} korda sõnas {sõne}")
#SORT
list_sõne.sort(reverse=True)
print(list_sõne)
#REVERSE
list_sõne.reverse()
print(list_sõne)
#COPY
list_sõne2=list_sõne.copy
#CLEAR
list_sõne2.clear()
print(list_sõne2)