def check_space(string):

    count = 0

    for i in range (0, len (string)):
        if string[i] == " ": 
            count += 1

    return (count)

string = input("Mata i en sträng: ")

print("number of spaces ",check_space(string))