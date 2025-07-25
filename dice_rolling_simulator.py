#Dice Rolling Simulator
import random
print("🎲....Dice Rolling Simulator....🎲")
player1 = int(input("🧑player1 enter how many dice you want to roll 🎲 :"))#dice rolling by player 1
player2 = int(input("🧑player2 enter how many dice you want to roll 🎲 :"))#dice rolling by player 2
result1 =[]
result2 = []
def dice(player1,player2,sum1= 0,sum2= 0):
    print("...........🧑player1................")
    for i in range(player1):
        dice_1 = random.randint(1,6)#for generating random numbers
        result1.append(dice_1)
    print("After rolling the dice",player1,"times you got :",result1)
    for i in result1:
        sum1+=i
    print("The sum of your dice numbers you got for each rolling is :",sum1)
    print("...........🧑player2................")
    for i in range(player2):
        dice_2= random.randint(1,6)
        result2.append(dice_2)
    print("After rolling the dice",player2,"times you got :",result2)
    for i in result2:
        sum2+=i
    print("The sum of your dice numbers you got for each rolling is :",sum2)
    print(".................................................................................................")
    if sum1>sum2:
        print("Wow! 🧑player1 you got more numbers than player2 and you have won the dice rolling simulater")
    else:
        print("Wow! 🧑player2 you got more numbers than player1 and you have won the dice rolling simulater") 
    print(".................................................................................................")    
data = dice(player1,player2)  
print(data)  
