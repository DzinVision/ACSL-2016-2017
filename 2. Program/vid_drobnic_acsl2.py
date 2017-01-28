# Vid Drobnič
# Gimnazija Vič, 4.b
# Intermediate 3
# Language: Python 3.6

for _ in range(5):
    numbers_str = input()
    numbers = [int(numbers_str[1:int(numbers_str[0])+1])]
    buff = ''
    for number in reversed(numbers_str[int(numbers_str[0])+1:]):
        buff += number
        if int(buff) > numbers[-1]:
            numbers.append(int(buff))
            buff = ''
    print(' '.join(map(str, numbers)))
