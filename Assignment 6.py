string = input("Enter a word: ")
char = input("Enter a character : ")

count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1

print("The total number of times ", char, " has occurred = " , count)