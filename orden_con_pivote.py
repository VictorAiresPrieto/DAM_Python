import random

numbers = [14, 54, 21, 9, 100, 2]

numbers = []
for i in range(10):
    numbers.append(random.randrange(-100, 100))
for i in range (len(numbers)-1):
    for j in range (i+1, len(numbers)):
        if numbers[i] > numbers[j]:
            transition_var = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = transition_var
print(numbers)