import os
stall=input("\n\n\n\n\n\n\n\n<><><> Press Enter To Begin <><><>")
amount=input("How many copies do we need to remove?: ")

amount=int(amount)
for num in range(amount):

    try:
        os.remove('shrek' +str(num) + '.txt')
        os.system('cls' if os.name == 'nt' else 'clear')
    except FileNotFoundError:
        os.system('cls' if os.name == 'nt' else 'clear')
    print(int(num/amount*1000)/(amount/100), "%"  )

os.system('cls' if os.name == 'nt' else 'clear')
print("100 %")
print("The Work Has Been Finished!")