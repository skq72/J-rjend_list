from string import *
vokaali=["a","e","u","i","�","�","�"]
konsonanti="qwrtypsdfghjklzxcvbnm"
numbrid=digits
m�rkid=punctuation
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
        elif s in m�rkid:
            m+=1
        elif s==" ":
            t+=1
    print(f"V: {v}\nK: {k}\nN: {m}\nT: {t}")
else:
    print(f"Kokku on {len(tekst_list)}")
    for s in tekst_list:
        if s in vokaali:
            v+=1
        elif s in konsonanti:
            k+=1