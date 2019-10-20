count = 0
fname = input("Enter a file name: ")
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From') : continue
    line = line.split()
    line = line[1]
    print(line)
    count = count + 1
print("There were", count, "lines in the file with From as the first word")