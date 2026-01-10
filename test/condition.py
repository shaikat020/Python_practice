units = float(input("Enter the units : "))

total_cost = 0.0
# tariff slabs
if units <= 75:
    total_cost = units * 4
elif units <= 200:
    total_cost = (75 * 4) + ((units - 75) * 5.45)
elif units <= 300:
    total_cost = (75 * 4) +( 125 * 5.45) + ((units -200) * 5.70)
elif units <= 400:
    total_cost = (75 * 4) +( 125 * 5.45) + (100 * 5.70) + ((units - 300) * 6.02)
elif units <= 600:
    total_cost = (75 * 4) +( 125 * 5.45) + (100 * 5.70) + (100 * 6.02) + ((units - 400) * 9.30)
else:
    total_cost = (75 * 4) +( 125 * 5.45) + (100 * 5.70) + (100 * 6.02) + ((600 - 400) * 9.30) + ((units - 600) * 10.70)

if units > 400 and total_cost > 3000:
    print("5 charge")
    charge = total_cost * 0.05
    total_cost = total_cost + charge # total_cost += charge
    

print("Total cost of electricity : ", total_cost)

# Amake whatsapp e knock diyo