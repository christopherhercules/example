# List : stroing multiple related values in the same variable.
weekly_temp = [45, 67, 90, 45, 75, 80]
# index:        0,  1,  2,  3,  4,  5

# Slicing the list
print(weekly_temp[3:])
print(weekly_temp)


weekly_temp[2] = 60
print(weekly_temp)

for temp in weekly_temp:
    temp =  (temp - 32) * (5/9)
    print(int(temp))





