# Programmers: Anthony DelVecciho
# Course: CS151, Dr. Rajeev
# Lab Number: 4
# Program Inputs: Data Used, Package Type, and whether or not user has a coupon
# Program Outputs: Amount Charged per month

# Define Function
def main():
    package = int(input("Input Package Type (1 = Green, 2 = Orange, 3 = Purple): "))
    dataused = int(input("Input Data Used in GB: "))
    coupon = int(input("Do You Have A Coupon (GREEN PACKAGE ONLY. 1 = Yes, 0 = No): "))
    if package == 1 and dataused <= 2 and coupon == 1 or coupon == 0:
        finalcharged = 49.99
    elif package == 1 and dataused > 2 and coupon == 0:
        finalcharged = 49.99 + (14.99 * (dataused - 2))
    elif package == 1 and dataused > 3 and coupon == 1:
        finalcharged = (49.99 + (14.99 * (dataused - 2))) - 20
    elif package == 2 and dataused <= 4:
        finalcharged = 69.99
    elif package == 2 and dataused > 4:
        finalcharged = 69.99 + (9.99 * (dataused - 4))
    elif package == 3 and dataused >= 0:
        finalcharged = 9.99
    print("Your amount charged for the month is $" + str(finalcharged))
    return finalcharged

main()

# Comments: Code wasn't working with word options (i.e. Green, Orange). No matter what I did it would not work so
# I resorted to using numbers.
