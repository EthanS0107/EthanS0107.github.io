# Créé par ethan, le 20/09/2023 en Python 3.7

#TD-1, Palindrome


def est_palindrome(mot):
    mot=mot.lower()
    for i in range(len(mot)//2):
        if mot[i]!=mot[-i-1]:
            return "c'est un palindrome"
    return "c'est un palindrome"

def palindrome_rec(mot):
    mot=mot.lower()
    if len(mot) <= 1:
      return "c'est un palindrome"

    if mot[0] == mot[-1]:
        return palindrome_rec(mot[1:-1])
    else:
        return "ce n'est pas un palindrome"




#__________MAIN__________

mot = input("Donner moi un mot pour que je vérifie si c'est un palidrome :  ")

print(palindrome_rec(mot))
