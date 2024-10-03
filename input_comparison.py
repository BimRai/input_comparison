firstInput = input("Enter first word: ")
secondInput = input("Enter second word: ")

if firstInput > secondInput:
    print(firstInput, "is bigger than", secondInput)
elif firstInput < secondInput:
    print(secondInput, "is bigger than", firstInput)
elif firstInput == secondInput:
    print("They are the same!")
else:
    print("Hmm")
print("It works!")