import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

home_dir = os.path.expanduser("~")
file_path = '/home/codes/'
# List of files
files = ['Large_mesh.xlsx','small_mesh.xlsx', 'power_law.xlsx']

# Set the width of each bar
bar_width = 0.2

# Iterate over the file list
for file_name in files:
    # Full path to the file
    file_path = os.path.join(home_dir, file_path,file_name)

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Extract the necessary columns for plotting
    x = df['Graph']
    y1 = df['MP-SCC']
    y2 = df['GPU-SCC']
    y3 = df['iSpan']

    # Calculate the x-axis positions for each set of bars
    x_pos = np.arange(len(x))

    # Create a new figure and axis for each file
    fig, ax = plt.subplots()

    # Plot the column graph
    ax.bar(x_pos - bar_width, y1, width=bar_width, label='MP-SCC')
    ax.bar(x_pos, y2, width=bar_width, label='GPU-SCC')
    ax.bar(x_pos + bar_width, y3, width=bar_width, label='iSpan')

    # Set the tick positions and labels for x-axis
    ax.set_xticks(x_pos)
    ax.set_xticklabels(x)

    # Set the title, x-label, y-label, and legend
    ax.set_title('Throughput (Mvertices/s) of MP-SCC, GPU-SCC, and iSpan ({})'.format(file_name))
    ax.set_xlabel('Graphs')
    ax.set_ylabel('Throughput (Mvertices/s)')
    ax.legend()

    # Adjust the layout to prevent overlapping labels
    plt.tight_layout()

    # Display the chart
    plt.show()
