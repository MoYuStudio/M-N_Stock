import matplotlib.pyplot as plt
import pandas as pd

CSV_tf = 'data/transformed_data/transferred.csv'
data = pd.read_csv(CSV_tf)
plt.ion()

# Lock z axis

z_min = data['z_ICRF'].min()
z_max = data['z_ICRF'].max()

def set_range(ax):
    ax.set_zlim([z_min, z_max])

# fig 1
def plot_icrf():

    icrf = plt.figure(figsize=(8,8))
    ax = icrf.add_subplot(111, projection='3d')
    ax.scatter([0], [0], [0], color="red")
    colors = data['Opposition'].map({1: 'blue', 2: 'purple', 3: 'red', 4: 'red'})
    ax.scatter(data['x_ICRF'], data['y_ICRF'], data['z_ICRF'], color=colors)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # set_range(ax)

    ax.set_title("ICRF")

    icrf.canvas.manager.window.attributes('-topmost', 1)
    icrf.canvas.manager.window.attributes('-topmost', 0)

plot_icrf()

# fig 2
def plot_ecl():

    Ecliptic = plt.figure(figsize=(8,8))
    ax = Ecliptic.add_subplot(111, projection='3d')
    ax.scatter([0], [0], [0], color="red")
    colors = data['Opposition'].map({1: 'blue', 2: 'purple', 3: 'red', 4: 'red'})
    ax.scatter(data['x_Ecl'], data['y_Ecl'], data['z_Ecl'], color=colors)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    set_range(ax)

    ax.set_title("Ecliptic")

    Ecliptic.canvas.manager.window.attributes('-topmost', 1)
    Ecliptic.canvas.manager.window.attributes('-topmost', 0)

plot_ecl()

# fig 3
def plot_polar():

    Polar = plt.figure(figsize=(8,8))
    ax = Polar.add_subplot(111, projection='3d')
    ax.scatter(data['x_Pol'], data['y_Pol'], data['z_Ecl'])

    Polar.canvas.manager.window.attributes('-topmost', 1)
    Polar.canvas.manager.window.attributes('-topmost', 0)

    set_range(ax)

    ax.set_title("Polar")

plot_polar()

input("Press Enter to end")


