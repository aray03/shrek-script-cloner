import os
stall=input("\n\n\n\n\n\n\n\n<><><> Press Enter To Begin <><><>")
amount=1000
for num in range(amount):

    shrek = open(( 'shrek'+str(num)+'.txt' ), 'w')
    os.remove('shrek' +str(num) + '.txt')
    os.system('clear')
    print((int(num/amount*1000)/100+0), "%"  )

    
    shrek.close()
stall=input(' The Work Has Been Finished ')