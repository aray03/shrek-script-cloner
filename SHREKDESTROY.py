import os
stall=input("\n\n\n\n\n\n\n\n<><><> Press Enter To Begin <><><>")
amount=input("How many copies do we need to remove?: ")

count = 0
newNum = 0
amount=int(amount)
for num in range(amount):

    try:
        os.remove('shrek' +str(num) + '.txt')
        count = count+1
    except FileNotFoundError:
       count = count

    #The print statement to make sure we are not repeating %s
    if int((num/amount)*10000)/100 > newNum:
        print(str(int((num/amount)*10000)/100) + "%")
        newNum = int((num/amount)*10000)/100

os.system('cls' if os.name == 'nt' else 'clear')
print("100%")
print("Deleted", count, "Files")
print("The Work Has Been Finished!")