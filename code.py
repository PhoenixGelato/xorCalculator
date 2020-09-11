e = open("inputtext.txt").readlines()
num1 = e[0].strip('\n')
num2 = e[1]
loop = len(num1)
ne = 0
num3 = ''
while ne < loop:
    if num1[ne] == num2[ne]:
        num3 += '0'
    else:
        num3 += '1'
    ne = ne + 1
f = open("outputtext.txt", 'w')
f.write(num1 + '\n')
f.write('xor\n')
f.write(num2 + '\n')
f.write('=\n')
f.write(num3 + '\n')
f.close()