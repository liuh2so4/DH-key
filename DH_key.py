import time

def function_hex_to_decimal(hex):
    decimal = 0
    for i in range(0, len(hex)):
        if hex[i] == '0':
            decimal = decimal * 16
        elif hex[i] == '1':
            decimal = decimal * 16 + 1
        elif hex[i] == '2':
            decimal = decimal * 16 + 2     
        elif hex[i] == '3':
            decimal = decimal * 16 + 3
        elif hex[i] == '4':
            decimal = decimal * 16 + 4
        elif hex[i] == '5':
            decimal = decimal * 16 + 5
        elif hex[i] == '6':
            decimal = decimal * 16 + 6
        elif hex[i] == '7':
            decimal = decimal * 16 + 7
        elif hex[i] == '8':
            decimal = decimal * 16 + 8
        elif hex[i] == '9':
            decimal = decimal * 16 + 9
        elif hex[i] == 'a' or hex[i] == 'A':
            decimal = decimal * 16 + 10
        elif hex[i] == 'b' or hex[i] == 'B':
            decimal = decimal * 16 + 11
        elif hex[i] == 'c' or hex[i] == 'C':
            decimal = decimal * 16 + 12
        elif hex[i] == 'd' or hex[i] == 'D':
            decimal = decimal * 16 + 13
        elif hex[i] == 'e' or hex[i] == 'E':
            decimal = decimal * 16 + 14
        elif hex[i] == 'f' or hex[i] == 'F':
            decimal = decimal * 16 + 15
        elif hex[i] == ':':
        	decimal = decimal
        else:
            print("Your data doesn't make sence. Please reload the process again.")
    return decimal

g = 2
p = function_hex_to_decimal("00:9f:db:8b:8a:00:45:44:f0:04:5f:17:37:d0:ba:2e:0b:27:4c:df:1a:9f:58:82:18:fb:43:53:16:a1:6e:37:41:71:fd:19:d8:d8:f3:7c:39:bf:86:3f:d6:0e:3e:30:06:80:a3:03:0c:6e:4c:37:57:d0:8f:70:e6:aa:87:10:33")
a = function_hex_to_decimal(str(input('input a = ')))
b = function_hex_to_decimal(str(input('input b = ')))

#TA
start = time.time()
A = pow(g, a, p)
TA = time.time() - start
#TB
start = time.time()
B = pow(g, b, p)
TB = time.time() - start
#TKA
start = time.time()
KA = pow(B, a, p)
TKA = time.time() - start
#TKB
start = time.time()
KB = pow(A, b, p)
TKB = time.time() - start

print('A = ',A)
print('Ta = ',TA)
print('B = ',B)
print('Tb = ',TB)
print('KA = ',KA)
print('TKA = ',TKA)
print('KB = ',KB)
print('TKB = ',TKB)

