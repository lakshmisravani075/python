import random
import math

# 1. Generate 5 random floats between 0 and 1
print("Random floats between 0 and 1:")
for _ in range(5):
    print(random.random())

# 2. Dice roll simulator using random.randint
dice = random.randint(1, 6)
print("\nDice rolled:", dice)

# 3. Convert 90 degrees to radians
degrees = 90
radians = math.radians(degrees)
print(f"\n{degrees} degrees in radians is:", radians)

# 4. Factorial of a user-given number
num = int(input("\nEnter a number to find factorial: "))
print("Factorial of", num, "is:", math.factorial(num))

# 5. Shuffle a list of 10 integers
numbers = list(range(1, 11))
print("\nOriginal list:", numbers)
random.shuffle(numbers)
print("Shuffled list:", numbers)
