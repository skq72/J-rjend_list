from random import *
wrds=["kala","tubli","õun","banaan"]
rnd=choice (wrds)
rndlist=list(rnd)
k=len(rndlist)
for i in range(0,6,1):
    o=-1
    print ("Arva ära sõna. Teil on ", 6-i, "katsed")
    answer=input ("[] "*k)
    answerlist=list (answer) 
    for a in range(0, k, 1):
        o+=1
        if answerlist[o]==rndlist[o]:
            print(answerlist[o], end=" ")

        else:
            print ("*", end=" ")
    print()
    if answer==rnd:
        print("Õige! sõna oli:", rnd, )
        break
    else:
        print("Viga! ", 6-i-1, " ")
        #