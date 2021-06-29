# Weather Project

score = 90.1
passed = True


if score >= 90:
    print("You got an A, Great Job!!")
    passed = True
elif score >= 80 and score < 90:
    print("You got a B, Not Bad!!")
    passed = True
elif score >= 70 and score < 80:
    print("You got a C, pretty average!!")
    passed = True
elif score >= 60 and score < 70:
    print("You got a D, pretty much failed, depends on school!!")
    passed = True
else:
    print("You Failed Try again")
    passed = False

if passed:
    print("moving to next grade level")
else:
    print("Don't be a failure")


