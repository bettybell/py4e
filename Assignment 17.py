hours = {}
list = []
fname = input('Enter file name: ')
fhandle = open(fname)
for line in fhandle:
    if line.startswith('From '):
        time = line.split()[5]
        hour = time.split(":")[0]
        hours[hour] = hours.get(hour, 0) + 1
for i in hours:
    list.append((i, hours[i]))

sorted_list = sorted(list)

for item in sorted_list:
    print(item[0], item[1])