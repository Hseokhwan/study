str_var = '1000'
res = int(str_var) + 1
print(res)

str_var = 'alghost'
if str_var.isdigit():
    res = int(str_var) + 1
    print(res)
else:
    print(str_var)

int_val = 1000
res = 100 + 200
print('Result: ' + str(res))
print(str(int_val))

str_var = 'alghost'
tuple_var = (1, 2, 3)

print(list(str_var))
print(list(tuple_var))

list_var = [1, 2, 3]
print(tuple(list_var))