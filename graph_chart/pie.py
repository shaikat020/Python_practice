import matplotlib.pyplot as plt

labels=  []

sizes= []

chart_title = input("Enter the chart title: ")


n = int(input("Enter the number of data points: "))

for i in range(n):
    xi = input(f"Enter name for point {i+1}: ")
    yi = int(input(f"Enter value for point {i+1}: "))
    
    #append data into list
    labels.append(xi)
    sizes.append(yi)

plt.pie(sizes,labels=labels, autopct='%1.1f%%')
plt.title(chart_title)
plt.show()