import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))
#hour = int(input("enter the hour: "))
print(hour)

if(hour>=0 and hour<12):
    print("goodmorning dear")
elif(hour>=12 and hour<17):
    print("goodafternoon dear")
else:
    print("goodevening dear")