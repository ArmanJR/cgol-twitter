import matplotlib.pyplot as plt

# Define the grid size (12 columns x 6 rows)
# Define the grid size (32x32)
columns, rows = 32, 32

# Original list of coordinates to shade (adjusted for 0-based indexing in Python)

shaded_cells = []

# it was [man khodam ra sakhtam # reshto] at first but this would require 512MB of RAM
# so it's now [zendegi # reshto] with 256MB

man = [
    (1,4),(1,5),(1,6),
    (2,4),(2,6),
    (3,4),(3,5),(3,6),
    (4,6),
    (5,6),
    (6,6),
    (7,6),(7,7),(7,8),(7,9),
    (8,9),
    (9,4),(9,9),
    (10,9),
    (11,6),(11,7),(11,8),(11,9)
]

offset_x = 1
offset_y = 1
man = [(x + offset_x, y + offset_y) for x, y in man]

khodam = [
    (1,4),(1,5),(1,6),
    (2,4),(2,6),
    (3,2),(3,4),(3,6),
    (4,6),
    (5,6),
    (6,5),(6,6),(6,7),(6,8),(6,9),
    (7,5),(7,6),(7,9),
    (8,5),(8,6),(8,9),
    (10,4),(10,5),(10,6),
    (11,4),(11,6),
    (12,4),(12,6),
    (14,4),(14,5),(14,6),
    (15,4),(15,6),
    (16,4),(16,5),(16,6),
    (17,6),(17,7),(17,8),(17,9)
]

offset_x = 14
offset_y = 1
khodam = [(x + offset_x, y + offset_y) for x, y in khodam]

ra = [
    (1,6),(1,7),(1,8),(1,9),
    (2,9),
    (3,2),(3,3),(3,4),(3,5),(3,6)
]

offset_x = 4
offset_y = 12
ra = [(x + offset_x, y + offset_y) for x, y in ra]

sakhtam = [
    (1,5),(1,6),
    (2,6),
    (3,5),(3,6),
    (4,6),
    (5,5),(5,6),
    (6,6),
    (7,2),(7,3),(7,4),(7,5),(7,6),
    (9,4),(9,5),(9,6),
    (10,4),(10,6),
    (11,2),(11,4),(11,6),
    (12,6),
    (13,6),
    (14,2),(14,4),(14,5),(14,6),
    (15,1),(15,6),
    (16,6),
    (17,4),(17,5),(17,6),
    (18,4),(18,6),
    (19,4),(19,5),(19,6),
    (20,6),(20,7),(20,8),(20,9),(20,10)
]

offset_x = 10
offset_y = 12
sakhtam = [(x + offset_x, y + offset_y) for x, y in sakhtam]

hashtag = [
    (1,2),(1,4),
    (2,1),(2,2),(2,3),(2,4),(2,5),
    (3,2),(3,4),
    (4,1),(4,2),(4,3),(4,4),(4,5),
    (5,2),(5,4)
]

offset_x = 7
offset_y = 19
hashtag = [(x + offset_x, y + offset_y) for x, y in hashtag]

reshto = [(5,1),(10,1),
    (9, 2), (6, 2), (4, 2),
    (12, 4), (9, 4), (7, 4), (5, 4), (3, 4), (1, 4), (11, 4),
    (1, 5), (1, 6), (12, 5), (11, 5), (10, 5), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), 
    (11, 6), 
    (12, 7), (2, 7), (1, 7), (11, 7)]

offset_x = 14
offset_y = 19
reshto = [(x + offset_x, y + offset_y) for x, y in reshto]

zendegi = [
    (1,4),(1,7),(1,8),(1,9),
    (2,9),
    (3,9),
    (4,4),(4,6),(4,7),
    (5,7),
    (6,7),
    (7,1),(7,5),(7,6),(7,7),
    (8,1),(8,2),(8,5),(8,7),
    (9,2),(9,3),
    (10,3),(10,5),(10,6),(10,7),
    (11,7),
    (12,7),(12,8),(12,9),
    (13,9),
    (14,9),
    (15,7),(15,8),(15,9),
]

offset_x = 10
offset_y = 5
zendegi = [(x + offset_x, y + offset_y) for x, y in zendegi]


shaded_cells = zendegi + hashtag + reshto

print(shaded_cells)

# Create a copy and flip both horizontally and vertically
flipped_cells = [(columns + 1 - x, y) for x, y in shaded_cells]

# Convert to 0-based indices for Python
shaded_cells_zero_based = [(x-1, y-1) for x, y in flipped_cells]

# Create the grid with a larger figure size
fig, ax = plt.subplots(figsize=(20, 20))  # Increased figure size
ax.set_aspect('equal')

# Draw the grid
for x in range(columns):
    for y in range(rows):
        # Check if the current cell is shaded
        if (x, y) in shaded_cells_zero_based:
            color = 'gray'
        else:
            color = 'white'
        # Draw a rectangle for each cell
        ax.add_patch(plt.Rectangle((x, y), 1, 1, edgecolor='black', facecolor=color))
        
        # Add cell numbers with smaller font size
        ax.text(x + 0.5, y + 0.5, f'({columns-x},{y+1})', 
                ha='center', va='center', fontsize=4)  # Reduced font size

# Add row numbers on the right with smaller font
for y in range(rows):
    ax.text(columns + 0.2, y + 0.5, f'Row {y+1}', 
            ha='left', va='center', fontsize=6)

# Add column numbers on the top with smaller font
for x in range(columns):
    ax.text(x + 0.5, -0.2, f'Col {columns-x}', 
            ha='center', va='top', fontsize=6)

# Set the axis limits with some padding for labels
ax.set_xlim(-0.5, columns + 0.5)
ax.set_ylim(-0.5, rows)

# Remove axis ticks
ax.set_xticks([])
ax.set_yticks([])

plt.show()