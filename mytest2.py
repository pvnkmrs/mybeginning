import re

pattern=r'(0?[1-9]|1[0-9]|2[0-9]|3[0-1])\-(0?[1-9]|1[0-2])\-19[0-9][0-9]'

# while True:
#     #validate date from 01-01-1900  to 12-12-1999
#     date=input('enter date in format of DD-MM-YYYY and number should be greater or equal to  01-01-1900 and less than 12-12-1999')
#
#     if re.match(pattern,date):
#         print(f'\nentered date is {date} , this is in correct format')
#     else:
#         print('\ndate not entered in correct format')

while True:
    print('good')


# print(f'\nentered date is {date}')

ls=[1,12,2,3,14,5,6,7]

#max sum of contiguous sub array of length 3

maxsum=0

step=4

for val in range(len(ls)):
    if val+step > len(ls):
        break
    subsum = sum(ls[val:val+step])
    if subsum>maxsum:
        maxsum=subsum

print(f'Max sum of contiguous sub array is {maxsum}')


