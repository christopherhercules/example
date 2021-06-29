#defining a function
# def function_name ():
# parameters


def add(num1,num2):
    return num1 + num2

# function definition
def concatenate(str1, str2):
    print(str1 + " " + str2)


# argument

num1 = [2, 4, 6, 8, 10]
num2 = [1, 3, 5, 7, 9]
State_dictionary = {
    "AZ": "Arizona",
    "TX": "Texas",
    "CA": "Californa",
    "NM": "New Mexico",
    "FL": "Florida"
}

# index 0, 1, 2, 3, 4
i = 0
solution = 0

while i <= 4:
    solution = add(num1[0+i],num2[0+i])
    print(solution)
    i = i + 1
    state = input("State? ")
    print(State_dictionary[state])
    concatenate(State_dictionary[state], "is cool")

# function invocation
concatenate("Hello", "python")


