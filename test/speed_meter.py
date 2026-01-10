speed = float(input("Enter speed :"))

if speed < 0:
    print("Invalid speed")
elif speed >= 200:
    print("Speed value too high")
elif speed > 0 and speed <= 60:
    print("You are driving safely")
elif speed >= 61 and speed <=120:
    print("You are driving overspeed. Fine")
else:
    print("You are driving too fast. Heavy Fine")