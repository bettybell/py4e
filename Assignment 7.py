str = 'X-DSPAM-Confidence:0.8475'
find = str.find(':')
after = len(str)
number = str[find+1:after]
float_number = float(number)

print(number)
print(float_number)