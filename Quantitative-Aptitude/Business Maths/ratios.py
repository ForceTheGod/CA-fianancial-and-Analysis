# writing a code where user inputs ratio and it calculates inverse, duplicate, triplicate, sub triplicate and sub triplicate of the ratio

user1 = int(input("Enter the ratio's first term "))
user2 = int(input("Enter the ratio's second term "))

print(f"Original ratio is {user1}:{user2}")
print(f"Inverse ratio is {user2}:{user1}")
print(f"Duplicate ratio is {user1 ** 2}:{user2 **2}")
print(f"Triplicate ratio is {user1 ** 3}:{user2 ** 3}")
print(f"Sub duplicate ratio is {user1 ** 0.5}:{user2 ** 0.5}")
print(f"Sub triplicate ratio is {user1 ** 0.3333}:{user2 ** 0.3333}")

# comparing two ratios to see which is bigger

import math

ratio11 = int(input("Enter the first ratio's first term "))
ratio12 = int(input("Enter the first ratio's second term "))
ratio21 = int(input("Enter the second ratio's first term "))
ratio22 = int(input("Enter the second ratio's second term "))

common = math.lcm(ratio12,ratio22)

if (ratio11 * (common / ratio12))/(common) > (ratio21 * (common / ratio22))/(common):
    print(f"The greater ratio is {ratio11}:{ratio12}")
else:
    print(f"The greater ratio is {ratio21}:{ratio22}")
