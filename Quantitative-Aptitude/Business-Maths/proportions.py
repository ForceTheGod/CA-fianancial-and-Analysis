#proportion checker in python

ratio11 = int(input("Enter the first ratio's first term "))
ratio12 = int(input("Enter the first ratio's second term "))
ratio21 = int(input("Enter the second ratio's first term "))
ratio22 = int(input("Enter the second ratio's second term "))

if (ratio11 * ratio22) == (ratio12 * ratio21):
    print("Ratios are in proportion")
else:
    print("Ratios are NOT in proportion")
