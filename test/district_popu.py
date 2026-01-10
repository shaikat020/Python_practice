districts = ["Dhaka", "Chattogram", "Rajshahi", "Khulna", "Sylhet", "Barishal", "Rangpur", "Mymensingh"]
population_millions = [21, 9, 2.9, 2.5, 3.4, 2.3, 2.8, 1.6]
rivers = ["Padma", "Jamuna", "Meghna", "Teesta", "Karnaphuli"]

print("Task-1 ")
for i in range(len(districts)):
    print(f"The population of {districts[i]} is {population_millions[i]} million.")
print("Task-2 ")
for i in range(len(districts)):
    if population_millions[i] >3:
        print(f"{districts[i]} has a population greater than 3 million.")
print("Task-3 ")

districts.insert(8, "Cox's Bazar")
population_millions.append(2.7)
print(f"Added district: {districts[-1]} with population {population_millions[-1]} million.")

print("Task-4 ")
if "Teesta" in rivers:
    rivers.remove("Teesta")
print("Updated river list:", rivers)

print("Task-5 ")
user_input = input("Enter the name of a district: ")
if user_input in districts:
    index = districts.index(user_input)
    print(f"The population of {user_input} is {population_millions[index]} million.")
else:
    print("District not found.")
    
print("Task-6 ")
print("Number of districts : ", len(districts))
print("Number of rivers : ", len(rivers))

print("Task-7 ")
large= []
for i in range(len(districts)):
    if population_millions[i]>5:
        large.append(districts[i])

print("Districts with population greater than 5 million:", large)

print("Task-8 ")
min_population = min(population_millions)
max_population = max(population_millions)

min_population_index = population_millions.index(min_population)
max_population_index = population_millions.index(max_population)

print(f"District with the smallest population: {districts[min_population_index]} ({min_population} million)")
print(f"District with the largest population: {districts[max_population_index]} ({max_population} million)")

print("Sorted population")
sorted_population = sorted(population_millions)
print("Population in ascending order:", sorted_population)
# decending order   
sorted_population = sorted(population_millions, reverse=True)
print("Population in descending order:", sorted_population)
