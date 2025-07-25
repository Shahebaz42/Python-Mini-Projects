#lucky_dram mini project using python
import random 
lucky = random.randint(1,5)
print("LETS START THE LUCKY_DRAW!!")
while True:
    member_num= int(input("WHAT IS YOUR LUCKY NUMBER :"))
    if member_num == lucky:
        print("CONGRATULATIONS YOUR NUMBER GOT MATCHED WITH THE LUCKY_DRAW NUMBER!")
        val = random.choice(["1KG_GOLD","BIKE","3KG_SILVER","RS.250k_CASH"])
        print("YOU GOT :",val)
        break
    else:
        print("!............BETTER LUCK NEXT TIME..........!") 
