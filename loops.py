lst = [16, 14, 5, 3]

# For
for i in range(len(lst)):
    print("lst[" + str(i) + "] = ", lst[i])

# do the same, put only print if the number is even


lst_a = []  # empty list

for i in range(0, 10, 1):   # start = 0, end = 10, step = 1,  if only one, then end, step is optional
    lst_a.append(i)

print(lst_a)    # is 10 part of the list? why do you think so?

# do the same, but change the step


# you can do this using comprehension list

lst_c = [i ** 2 for i in range(17)]
# what is lst_c

# do the same but lst_d must contain only odd number between 6 and 17

# While

k = 0
while k < 10:
    print("in the loop, k = ", k)
    k += 1

# difference between while and for loop?
