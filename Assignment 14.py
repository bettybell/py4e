counts = {}
fname = input("Enter a file name: ")
fhand = open(fname)
for line in fhand:
    if line.startswith('From') :
        line = line.split()
        email_sender = line[1]
        counts[email_sender] = counts.get(email_sender, 0) + 1
        max = email_sender

for sender in counts:
    if counts[sender] > counts[max]:
        max = sender

print('Most number of emails sent by:', max, 'with', counts[max], 'emails')