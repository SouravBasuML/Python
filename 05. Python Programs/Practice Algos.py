# ---------------------------------------------------------------------------------------------------------------------
# Reverse a signed integer
# ---------------------------------------------------------------------------------------------------------------------
# n = -123456789
# print(int('-' + str(n)[:0:-1]) if str(n)[0] == '-' else int(str(n)[::-1]))

# ---------------------------------------------------------------------------------------------------------------------
# Return average word length in a sentence
# ---------------------------------------------------------------------------------------------------------------------
# sentence = "Hi all, my name is Tom...I am originally from Australia"
#
# for punctuation in ",.!;:?":
#     sentence = sentence.replace(punctuation, ' ')
# sent_split = sentence.split()
# print(round(sum(len(word) for word in sent_split) / len(sent_split), 2))


# ---------------------------------------------------------------------------------------------------------------------
# Return the index of the first non-repeating character in a string
# ---------------------------------------------------------------------------------------------------------------------
# a = 'aabbccddddeedddd'
# letter_count = [a.count(letter) for letter in a]
# print(letter_count.index(1) if 1 in letter_count else -1)


# ---------------------------------------------------------------------------------------------------------------------
# Determine a string is Palindrome by removing atmost 1 character
# ---------------------------------------------------------------------------------------------------------------------
# s = 'malayalam'
# for i in range(len(s)):
#     t = s[:i] + s[i+1:]
#     if t == t[::-1]:
#         print(True)
#         break
#     if i == len(s) - 1:
#         print(False)


# ---------------------------------------------------------------------------------------------------------------------
# Determine if an array of integers is monotonic (increasing or decreasing)
# ---------------------------------------------------------------------------------------------------------------------
# a = [9, 8, 8, 7, 7, 2, 1, 2]
# a = [1, 2, 2, 3, 3, 5, 7, 2]
#
# icount, dcount = (0, 0)
# for i in range(len(a) - 1):
#     if a[i+1] >= a[i]:
#         icount += 1
#     if a[i+1] <= a[i]:
#         dcount += 1
# if icount==len(a) - 1 or dcount==len(a) - 1:
#     print(True)
# else:
#     print(False)

# # Alternate Solution:
# # all() returns 'True' if all items in an iterable are true, else returns 'False'
# print(all(a[i+1] >= a[i] for i in range(len(a) - 1)) or all(a[i+1] <= a[i] for i in range(len(a) - 1)))


# ---------------------------------------------------------------------------------------------------------------------
# Move 0s to end of an integer array, keeping the relative order of elements
# ---------------------------------------------------------------------------------------------------------------------
# a = [1, 0, 8, 0, 0, 0, 0, 12, 1, 0, 4, 0, 0, 6, 0]
# for i in a:
#     if 0 in a:
#         a.remove(0)
#         a.append(0)
# print(a)


# ---------------------------------------------------------------------------------------------------------------------
# Replace None values in an array with the most recent non-None value
# ---------------------------------------------------------------------------------------------------------------------
# a = [None, 2, 9, None, None, None, 4, 3, None, None]
# temp = 0
# for i in range(len(a)):
#     if a[i] is not None:
#         temp = a[i]
#     else:
#         a[i] = temp
# print(a)


# ---------------------------------------------------------------------------------------------------------------------
# Given 2 sentences, return:
# 1. An array with words that appear in one and not in other
# 2. An array with words that appear in both
# 3. An array with words in common
# ---------------------------------------------------------------------------------------------------------------------
# s1 = 'We are really pleased to meet you in our city'
# s2 = 'The city was hit by a really heavy storm'
# set_s1 = set(s1.split())
# set_s2 = set(s2.split())
# print(set_s1.symmetric_difference(set_s2))          # ^
# print(set_s1.union(set_s2))                         # |
# print(set_s1.intersection(set_s2))                  # &
# print(set_s1.difference(set_s2))                    # -


# ---------------------------------------------------------------------------------------------------------------------
# Print prime numbers between a given range
# ---------------------------------------------------------------------------------------------------------------------
# l, u = (20, 100)
# prime = []
# for i in range(l, u+1):
#     for n in range(2, int(i/2)):
#         if i % n == 0:
#             break
#     else:
#         prime.append(i)
# print(prime)
