count = 0
while True:
    fname = input("Enter the file name: ")
    if fname == "NA NA BOO BOO" :
        print("NA NA BOO BOO - You have been punk'd!")
        break
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        continue
    break
for line in fname:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lines in", fname)
exit()