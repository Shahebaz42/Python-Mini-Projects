#Bill Splitter(make sure that split the bill equally/fairly )
net_bill = int(input("Enter the Total Bill :"))
workers = int(input("Enter the no.of Workers :"))
final_amount = True
def bill(net_bill,workers):
    print("............................................................................")
    print("Total Bill :",net_bill)
    print("No.of Workers :",workers)
    final_amount = round((net_bill/workers),2)#this will calculate how much amount will each worker can take
    print("After Splitting the Bill each person got exactly Rs.",final_amount)
    if net_bill == 0:
        print("There is no Bill that has passed so I can't give you amount")
    elif workers ==1:
        print("I can't split the bill because there is only one worker")
    elif net_bill<workers:
        print("The bill has passed less and workers are more so each worker got less amount as they didn't expect ")    
    print("............................................................................")    
data = bill(net_bill,workers)   
print(data)
