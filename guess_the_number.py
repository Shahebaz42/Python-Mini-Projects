##Guess The Number##
import random as rm
target = rm.randint(1,100)

while True:
    userchoice=(input("Guess number or Quit :"))
    if(userchoice == "Quit"):
        break
    userchoice = int(userchoice)
    if(userchoice == target):
        print("Success :Guessed Correct Number")
        break
    elif(userchoice<target):
        print("Number was too small,Take a bigger number!")   
    else:
        print("Number was too Big,Take a smaller number!")   

print(".....................Game is Over.........................")         
