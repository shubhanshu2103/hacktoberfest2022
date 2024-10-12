def val(c):
    if c >= '0' and c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10;
 
def toDeci(str,base):
    llen = len(str)
    power = 1
    num = 0
  
    for i in range(llen - 1, -1, -1):

        if val(str[i]) >= base:
            print('Invalid Number')
            return -1
        num += val(str[i]) * power
        power = power * base
    return num

strr = input("enter the number you want to convert in base")
base = int(input("base of that number"))
print('Decimal equivalent of', strr, 'in base', base, 'is',  toDeci(strr, base))
 
