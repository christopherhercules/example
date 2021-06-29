# for loop : number of iterations known
word = ""

for num in range(5, 20):
    word = word + "*"

print(word)


# while loop : number iterations Not known

number = 1001

# exit condition

while number > 1000:
    number = number * 2
    if number > 1000000:
        break
    print(number)

print("finished")
