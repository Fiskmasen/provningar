def check_tecken(string):

    count = 0
    for tecken in range(0, len(string)):
        if string[tecken] != " ":
            count = count + 1
       
    return count

string = input("Mata i en sträng: ")

print("Antalet tecken: ",check_tecken(string))