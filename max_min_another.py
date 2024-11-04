
x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))
x3 = int(input('Введите третье число: '))
if x1 < x2:
    buf = x1
    x1 = x2
    x2 = buf
if x1 < x3:
    buf = x1
    x1 = x3
    x3 = buf
if x2 > x3:
    buf = x2
    x2 = x3
    x3 = buf
print(x1,x2,x3,sep="\n")
