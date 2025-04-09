# Collatz Conjecture program
def collatz_conjecture(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = (n * 3) + 1
        print(int(n), end = " ")
        steps += 1
    return steps

userInput=int((input("Enter an integer greater than 1: ")))
print("\nSteps: " + str(collatz_conjecture(userInput)))