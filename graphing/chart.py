#!/usr/bin/env python3

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Pineapple', 'Bacon', 'Cheese', 'Chicken', 'Onion', 'Bell Pepper'
sizes = [15, 20, 30, 20,10,5]
explode = (0, 0, 0.1, 0, 0, 0)  # only "explode" the 3rd slice (i.e. 'Cheese')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Hawaiian Pizza")
plt.savefig("/home/student/static/pie.png")
print("Fin")
