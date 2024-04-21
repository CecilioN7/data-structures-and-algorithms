num = list(range(100))
print(type(num))

a = list(range(10))
print(type(a))

b = [i for i in range(10)]
print(type(b))

index = 0

def for_loop(list):
    for i in list:
        print(list[i])

def while_loop(list, i):
    while i < len(list):
        curr_number = list[i]
        print(curr_number)
        i += 1

def nested_for_loop(array1, array2):
    for i in array1:
        for j in array2:
            print('i:', i, ' j:', j, ' ', end='')
            curr_num = array1[i] + array2[j]
            print(curr_num)
    print('size: ', i * j)

def control_statements():
    print("Break")
    for i in range(10):
        if i == 5:
            break
        print(i)
    print("-" * 10)

print('FOR LOOP')
for_loop(num)
print('\n')

print('WHILE LOOP')
while_loop(num, index)
print('\n')

print('NESTED FOR LOOP')
nested_for_loop(a, b)
print('\n')

print('NESTED FOR LOOP')
control_statements()
print('\n')