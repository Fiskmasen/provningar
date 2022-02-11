s = input("Ge hit en sträng: ")
c = input("Ange ett tecken du vill hitta: ")
lst = []
for pos, char in enumerate(s):
    if(char == c):
        lst.append(pos)
print(lst)