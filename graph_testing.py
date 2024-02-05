# # Sample dictionary
# my_dict = {'apple': 3, 'banana': 1, 'orange': 2, 'grape': 4}

# # Sorting the dictionary by values
# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# # Displaying the sorted dictionary
# print(sorted_dict)

import matplotlib.pyplot as plt

# Sample data as dictionary
data = {'Category A': 10, 'Category B': 20, 'Category C': 15, 'Category D': 25}
data = dict(sorted(data.items(), key=lambda item: item[1]))

# Extract categories and values from the dictionary
categories = list(data.keys())
values = list(data.values())

# Create a horizontal bar chart
plt.barh(categories, values)

# Adding labels and title
plt.xlabel('Values')
plt.ylabel('Categories')
plt.title('Horizontal Bar Chart')

# Show the plot
plt.show()


