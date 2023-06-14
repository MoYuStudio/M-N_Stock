import matplotlib.pyplot as plt
import pandas as pd

dropped_file = 'data/transformed_data/dropped.csv'

data = pd.read_csv(dropped_file)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter([0], [0], [0], color="red")

ax.scatter(data['x_Ecl'], data['y_Ecl'], data['%_Changed'])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()