s = input()
ls = ''.join(' '+el for el in s)
lst = ls.split()
lst = [int(lst[i]) for i in range(len(lst))]
if sum(lst[:3]) == sum(lst[3:]):
    print('Счастливый')
else:
    print('Обычный')