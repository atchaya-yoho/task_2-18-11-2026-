import matplotlib.pyplot as plt

# Data
months=["Jan","Feb","Mar","Apr"]
sales=[100,50,120,200]

# 2x2 chart
fig, axs=plt.subplots(2,2)
fig.set_size_inches(10,7)

# Bar chart
axs[0,0].bar(months,sales,color="blue")
axs[0,0].set_title("Sales Bar chart")

# line chart
axs[0,1].plot(months,sales,marker="o",color="orange")
axs[0,1].set_title("Sales Line Chart")

# Scatter plot
axs[1,0].scatter(months,sales,color="brown")
axs[1,0].set_title("Sales Scatter")

# Histogram
marks=[45,55,60,60,70,75,80,85,90,90]
axs[1,1].hist(marks)
axs[1,1].set_title("Marks Histogram")

plt.tight_layout()
plt.savefig("all_charts.png")
plt.show()
print("charts done")
