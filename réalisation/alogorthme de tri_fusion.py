# Créé par ethan, le 03/03/2024 en Python 3.7
from random import randint

def Liste_ordonnée(n) :
    L = [randint(1,20)]
    for ind in range(1,n) :
        L.append(L[ind-1]+randint(1,20))
    return L


def fusion_rec (L1,L2) :
    tmp = ()
    if len(L1)!=0 and len(L2) == 0 :
        return L1
    if len(L1)==0 and len(L2) != 0 :
        return L2
    if len(L1)!=0 and len(L2)!=0 :
        if L1[0] <= L2[0] :
            tmp = [L1[0]] + fusion_rec(L1[1: ],L2)
            return tmp
        else :
            tmp = [L2[0]] + fusion_rec(L1,L2[1: ])
            return tmp


def tri_fusion(L) :
    if len(L) == 1 :
        return L
    else :
        tmp = len(L)//2
        return fusion_rec(tri_fusion(L[0:tmp]), tri_fusion(L[tmp:]))


#===============================================================================
#                                    Main
#===============================================================================

x = 2
n = 10

L1 = Liste_ordonnée(n)
L2 = Liste_ordonnée(n)
L3 = fusion_rec(L1,L2)

Print("La liste 1 est : ",L1)
Print("La liste 2 est : ",L2)
print("La fusion de deux liste est : ",L3)
