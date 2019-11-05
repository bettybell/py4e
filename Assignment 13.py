counts = {}
fname = input("Enter a file name: ")
fhand = open(fname)
for line in fhand:
    if line.startswith('From') :
        line = line.split()
        email = line[1]
        counts[email] = counts.get(email, 0) + 1
print(counts)
