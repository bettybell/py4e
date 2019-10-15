fname = input("Enter the file name: ")
fhand = open(fname)
count = 0
sum = 0
answer = 0
for line in fhand:
    if line.startswith("X-DSPAM-Confidence:",) :
        float_number = float(line[line.find('0'):len(line)])
        count = count + 1
        sum = float_number + sum
answer = sum / count
print ("Average spam confidence:", answer)