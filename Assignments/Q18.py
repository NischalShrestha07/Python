# WAP TO PRINT DATE,TIME FOR TODAY AND NOW.


from datetime import datetime
todayDate=datetime.today().date()

currentTime=datetime.now().time()

print(f"Today's date is: {todayDate}")
print(f"Today's current Time is: {currentTime}")