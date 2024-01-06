

def menu():
    print("This program performs operations on fractions. Enter")
    print("1 : To add fraction")
    print("2 : To subtract fraction")
    print("3 : To multiply fraction")
    print("4 : To divide fraction")
    print("9 : To exit the program")

def addFractions(param1, param2, param3, param4):
    numQty = param1 * param4 + param2 * param3
    denQty = param2 * param4
    return numQty, denQty

def subtractFractions(param1, param2, param3, param4):
    numQty = param1 * param4 - param2 * param3
    denQty = param2 * param4
    return numQty, denQty

def multiplyFractions(param1, param2, param3, param4):
    numQty = param1 * param3
    denQty = param2 * param4
    return numQty, denQty

def divideFractions(param1, param2, param3, param4):
    numQty = param1 * param4
    denQty = param2 * param3
    return numQty, denQty

def main():
    denom_mistake_first = True
    numera_mistake_first = True
    denom_mistakeSecond = True

    while True:
        menu()
        userSelection = int(input())
        if userSelection == 9:
            break
        elif userSelection < 1 or userSelection > 4:
            print("Invalid choice. Please try again.")
            continue
        else:
            print("For fraction 1:")
            param1 = int(input("Enter the numerator: "))
            print()
            param2 = int(input("Enter the denominator: "))
            print()
            while param2 == 0:
                if denom_mistake_first:
                    print("The denominator must be nonzero.")
                    print()
                    denom_mistake_first = False
                else:
                    param2 = int(input("Enter the denominator: "))
                    print()
            print("For fraction 2:")
            param3 = int(input("Enter the numerator: "))
            print()
            while param3 == 0 and userSelection == 4:
                if numera_mistake_first:
                    print("To divide, the second fraction must be nonzero.")
                    numera_mistake_first = False
                else:
                    param3 = int(input("Enter a nonzero number for the numerator: "))
                    print()
            param4 = int(input("Enter the denominator: "))
            print()
            while param4 == 0:
                if param3 == 0 and numera_mistake_first:
                    print("To divide, the second fraction must be nonzero.")
                    numera_mistake_first = False
                elif denom_mistakeSecond:
                    print("The denominator must be nonzero.")
                    denom_mistakeSecond = False
                else:
                    param4 = int(input("Enter the denominator: "))
                    print()
            if userSelection == 1:
                numQty, denQty = addFractions(param1, param2, param3, param4)
                print(f"{param1}/{param2} + {param3}/{param4} = {numQty}/{denQty}\n")
            elif userSelection == 2:
                numQty, denQty = subtractFractions(param1, param2, param3, param4)
                print(f"{param1}/{param2} - {param3}/{param4} = {numQty}/{denQty}\n")
            elif userSelection == 3:
                numQty, denQty = multiplyFractions(param1, param2, param3, param4)
                print(f"{param1}/{param2} * {param3}/{param4} = {numQty}/{denQty}\n")
            elif userSelection == 4:
                while param3 == 0:
                    if numera_mistake_first:
                        print("To divide, the second fraction must be nonzero.")
                        numera_mistake_first = False
                    else:
                        param3 = int(input("Enter a nonzero number for the numerator: "))
                        print()
                while param4 == 0:
                    if denom_mistakeSecond:
                        print("The denominator must be nonzero.")
                        denom_mistakeSecond = False
                    else:
                        param4 = int(input("Enter the denominator: "))
                        print()
                numQty, denQty = divideFractions(param1, param2, param3, param4)
                print(f"{param1}/{param2} / {param3}/{param4} = {numQty}/{denQty}\n")
          


main()