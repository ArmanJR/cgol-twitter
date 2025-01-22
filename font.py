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
    # If you want a space character to skip some columns:
    ' ': []
}

# Choose any word you wish (all uppercase letters).
word = "HELLO"

# Build the assembly instructions to draw each letter in the word.
# Each letter is 3 pixels wide and 5 tall; we’ll move x_offset by 4 so there’s 1 blank column gap.
program_lines = []
program_lines.append("erase")  # Clears the screen

x_offset = 0
base_y = 5  # Move the word down a bit; you can adjust easily.

for ch in word:
    ch = ch.upper()
    # If not in our dictionary, treat it as a space.
    if ch not in letter_pixels:
        x_offset += 4
        continue
    for (px, py) in letter_pixels[ch]:
        program_lines.append(f"write a1 {px + x_offset}")
        program_lines.append(f"write a2 {py + base_y}")
        program_lines.append("disp a1 a2")
    x_offset += 4

# Add an infinite loop at the end to halt.
program_lines.append("goto 9999")

# Combine into a single multiline string.
program = "\n".join(program_lines)

# Now 'program' is your final assembly code to place in the main script.
# For example:
print(program)
