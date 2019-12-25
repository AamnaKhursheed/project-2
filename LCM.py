numA = int(input("Enter first number: "))
numB = int(input("Enter second number: "))

min_numb = min(numA, numB)

while(1):
    if(min_numb % numA == 0 and min_numb % numB == 0):
        print("LCM of two number is: ", min_numb)
        break
    min_numb += 1
