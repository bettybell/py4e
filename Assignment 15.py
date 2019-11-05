counts = {}
fname = input("Enter a file name: ")
fhand = open(fname)
for line in fhand:
    if line.startswith('From:'):
       line = line.strip()
       at = line.find('@')
       domain = line[at+1:]
       counts[domain] = counts.get(domain, 0)+1
print(counts)
