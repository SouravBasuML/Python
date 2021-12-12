
# ---------------------------------------------------------------------------------------------------------------------
# While Loop:
# ---------------------------------------------------------------------------------------------------------------------
# 'Break' will break out of the loop
# 'Continue' will skip that particular loop iteration

# While loop can have else block:
# When the condition becomes False and the loop runs normally, the else clause will execute. However, if the loop is
# terminated prematurely by either a break or return statement, the else clause won’t execute at all.
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("xxx")


# ---------------------------------------------------------------------------------------------------------------------
# For Loop:
# ---------------------------------------------------------------------------------------------------------------------
print("\nFor Loop:")
for letter in "Sourav Basu":
    print(letter)

print("\n")
name_list = ["AAA", "BBB", "CCC", "DDD"]
for name in name_list:
    print(name)

print("\n")
for num in range(5):
    print(num)              # 0 to 4

print("\n")
for num in range(5, 10):
    print(num)              # 5 to 9

print("\n")
for num in range(5, 10, 2):
    print(num)              # 5, 7, 9

print('\n')
for num1 in range(3):
    for num2 in ['a', 'b', 'c']:
        print(num1, num2)

print('\n')
for num1 in range(3):
    for num2 in ['a', 'b', 'c']:
        print(num1, num2)
        if num2 == 'b':
            break                   # if you break from nested loop, control comes to outer loop
    print('in first loop')


# ---------------------------------------------------------------------------------------------------------------------
# One-Line For Loop:
# ---------------------------------------------------------------------------------------------------------------------

[print(letter) for letter in 'Sourav Basu']

name_list = ["AAA", "BBB", "CCC", "DDD"]
[print(name) for name in name_list]
print([name for name in name_list])             # prints a list

[print(num) for num in range(5)]
print([num for num in range(5)])                # prints a list

[print(num) for num in range(5, 10)]

[print(num) for num in range(5, 10, 2)]

[print(num1, num2) for num1 in range(3) for num2 in ['a', 'b', 'c']]
