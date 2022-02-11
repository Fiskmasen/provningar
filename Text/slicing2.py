def isPalindrome(a): 
    return a == a [::-1] 


a = input("Skriv in ett ord: ")
ord = isPalindrome(a)

while ord == False:
    print ("Nej, detta är inte ett palindrom. Försök igen.")
    a = input("Skriv in ett ord: ")
    ord = isPalindrome(a)
 
print("Ja, det är ett palindrom.")