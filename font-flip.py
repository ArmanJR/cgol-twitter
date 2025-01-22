# A small 3×5 block font for demonstration.
# Each entry is a list of (x, y) pixel coordinates to plot for that letter,
# with (0,0) at the top-left corner of the letter's bounding box.
letter_pixels = {
    'H': [
        (0,0),(1,0),(2,0),
        (0,1),(2,1),
        (0,2),(1,2),(2,2),
        (0,3),(2,3),
        (0,4),(2,4)
    ],
    'E': [
        (0,0),(1,0),(2,0),
        (0,1),
        (0,2),(1,2),(2,2),
        (0,3),
        (0,4),(1,4),(2,4)
    ],
    'L': [
        (0,0),
        (0,1),
        (0,2),
        (0,3),
        (0,4),(1,4),(2,4)
    ],
    'O': [
        (0,0),(1,0),(2,0),
        (0,1),(2,1),
        (0,2),(2,2),
        (0,3),(2,3),
        (0,4),(1,4),(2,4)
    ],
    'W': [
        (0,0),(2,0),
        (0,1),(2,1),
        (0,2),(1,2),(2,2),
        (0,3),(1,3),(2,3),
        (0,4),(2,4)
    ],
    'R': [
        (0,0),(1,0),(2,0),
        (0,1),(2,1),
        (0,2),(1,2),(2,2),
        (0,3),(2,3),
        (0,4),(2,4)
    ],
    'D': [
        (0,0),(1,0),(2,0),
        (0,1),(2,1),
        (0,2),(2,2),
        (0,3),(2,3),
        (0,4),(1,4),(2,4)
    ],
    ' ': []
}

# Define your desired word here (all caps).
word = "HELLO WO"

LETTER_WIDTH = 3
LETTER_HEIGHT = 5
LETTER_SPACING = 1      # number of blank columns between letters

# Build assembly instructions to draw the word.
program_lines = []
program_lines.append("erase")

x_offset = 0
base_y = 5  # vertical offset so letters won't be at the top edge.

for ch in word:
    ch = ch.upper()
    # If a character isn't in our dictionary, skip or treat as space.
    if ch not in letter_pixels:
        x_offset += (LETTER_WIDTH + LETTER_SPACING)
        continue
    
    for (px, py) in letter_pixels[ch]:
        # Flip horizontally by using (LETTER_WIDTH - 1 - px) 
        flipped_x = (LETTER_WIDTH - 1) - px
        
        # Now build assembly lines to plot that pixel at (flipped_x + x_offset, py + base_y).
        program_lines.append(f"write a1 {flipped_x + x_offset}")
        program_lines.append(f"write a2 {py + base_y}")
        program_lines.append("disp a1 a2")
    
    # Move to the next letter's "column start" (3 wide + 1 blank column).
    x_offset += (LETTER_WIDTH + LETTER_SPACING)

# Add an infinite jump so we don't keep running off the end.
program_lines.append("goto 9999")

# Combine into one multiline string for the main script.
program = "\n".join(program_lines)
print(program)

