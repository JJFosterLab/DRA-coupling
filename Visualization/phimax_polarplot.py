import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

def read_tsv(filename):
    """Reads a TSV file and returns a dict with columns as keys and angle lists as values."""
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        headers = next(reader)
        columns = {h: [] for h in headers}

        for row in reader:
            for i, val in enumerate(row):
                if val.strip():
                    try:
                        columns[headers[i]].append(float(val))
                    except ValueError:
                        pass

    return columns

def plot_half_polar(data):
    """Plots the angles on a half polar plot using black symbols only."""
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_thetamin(0)
    ax.set_thetamax(180)

    markers = ['o', 's', '^', 'D', '*']  # different symbols per cell

    for idx, (label, angles_deg) in enumerate(data.items()):
        angles_rad = np.radians(angles_deg)
        radii = np.ones_like(angles_rad)
        ax.scatter(angles_rad, radii, label=label,
                   marker=markers[idx % len(markers)],
                   color='black',
                   s=80)

    ax.legend(loc='upper center')
    ax.set_theta_zero_location('N')  # N = top (north)
    ax.set_theta_direction(-1)       # clockwise

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python polar_plot.py data.tsv")
        sys.exit(1)

    filename = sys.argv[1]
    data = read_tsv(filename)
    plot_half_polar(data)
