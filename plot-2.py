import matplotlib.pyplot as plt

# Plotting
plt.figure(figsize=(15, 8))

# Histogram of Collatz Sequence Lengths
plt.subplot(2, 3, 1)
plt.hist(num_it_2, bins=50, color='skyblue', edgecolor='black')
plt.title('Histogram of Collatz Sequence Lengths')
plt.xlabel('Sequence Length')
plt.ylabel('Frequency')

# Bar plot for Prime and Non-Prime Lengths
plt.subplot(2, 3, 2)
plt.bar(['Prime', 'Non-Prime'], [len(prime), len(notprime)], color=['green', 'red'])
plt.title('Number of Prime and Non-Prime Lengths')
plt.ylabel('Count')

# Pie chart for the Ratio of Non-Prime to Prime Lengths
plt.subplot(2, 3, 3)
labels = ['Prime', 'Non-Prime']
sizes = [len(prime), len(notprime)]
colors = ['green', 'red']
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Percentage of Non-Prime to Prime Lengths')

# Pie chart for the Ratio of Non-Prime to Prime numbers from 2 to cal_num
plt.subplot(2, 3, 4)
labels = ['Prime Numbers', 'Non-Prime Numbers']
sizes = [percentage_prime, percentage_notprime]
colors = ['green', 'red']
plt.pie(sizes,labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Percentage of Prime and Non-Prime Numbers up to ' + str(cal_num))

plt.tight_layout()
plt.show()
