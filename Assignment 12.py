list = []
while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        number = float(number)
    except:
        print('Invalid input')
    list.append(number)
print('Maximum: ', max(list))
print('Minimum: ', min(list))