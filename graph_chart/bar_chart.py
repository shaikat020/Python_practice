import matplotlib.pyplot as plt

x=  []

y= []

chart_title = input("Enter the chart title: ")
x_label = input("Enter the x-axis label: ")
y_label = input("Enter the y-axis label: ")

n = int(input("Enter the number of data points: "))

for i in range(n):
    xi = input(f"Enter {x_label} for point {i+1}: ")
    yi = float(input(f"Enter {y_label} for point {i+1}: "))
    
    #append data into list
    x.append(xi)
    y.append(yi)

plt.bar(x,y)
plt.title(chart_title)
plt.xlabel(x_label)
plt.ylabel(y_label)
plt.show()