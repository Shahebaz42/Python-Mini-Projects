#phonebook application
#it is used to store the contact and performing some operatons(CRUD) to handle the phonebook
phonebook = {
    "asher": 9091236578,
    "amar": 9010547682,
    "bean":7089564320,
    "brown" :8090567088,
    "captow":7700554428,
    "chahar":2344567761
}
print(".........welcome to the phonebook application.........") # greeting to the user
while True:#loop is used to asking input again and again until user exit from the application
        userchoice = input("would you like to proceed or exit :")#taking userchoice as input
        if userchoice=="exit":
            break
        if userchoice == "proceed":
            userinput = input("Which operation do you want to perform :")#taking particular operation from user to perform that partcular operation
            if userinput == "add":#nested if-else block
                name = input("Enter name :")
                if name in phonebook:
                    print("The name is already exist add with another name!")
                else: 
                    num =input("Enter num :")
                    phonebook.update({name:num})#adding data into phonebook  
                    print("contact added successfully!")
            elif userinput =="delete": 
                removing =input("Enter the name you want to delete :")
                if removing not in phonebook:
                    print("the contact is not exist in phonebook!")
                else:
                    del phonebook[removing]#deleting data from phonebook
                    print("contact deleted successfull!")
            elif userinput == "search":    
                key = input("which name you would like to search in phonebook :")
                if key in phonebook: # checking if search data is there or not in phonebook
                    print("searched name is present in the phonebook","\n",key,":",phonebook[key])
                else:
                    print(f"there is no {key} is present in the phonebook!")
            elif userinput == "display":
                for key in phonebook:# this loop is used to display the data in line by line(not in conjusted)
                    print(key,":",phonebook[key]) #printing the key and corresponding value
print(".........Successfully closed the phonebook application.........") # application closure information to the user 
     

