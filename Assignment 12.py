list = []
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print('Invalid input')
        continue
    list.append(number)

if len(list) == 0:
    print('Please enter a number, no maximum and minimum.')
else:
    print('Maximum: ', max(list))
    print('Minimum: ', min(list))