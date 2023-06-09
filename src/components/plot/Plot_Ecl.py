import matplotlib.pyplot as plt
import pandas as pd

CSV_tf = "Z:\\desktop\\Transferred.csv"

data = pd.read_csv(CSV_tf)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter([0], [0], [0], color="red")

colors = data['Opposition'].map({1: 'blue', 2: 'purple', 3: 'red', 4: 'red'})
ax.scatter(data['x_Ecl'], data['y_Ecl'], data['z_Ecl'], color=colors)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()