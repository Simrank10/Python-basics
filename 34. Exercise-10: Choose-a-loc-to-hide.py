"""
Create a 3x3 matrix filled with "🥸". 
Ask the user to select a position (e.g., 23 for row 2, column 3) 
to hide their treasure by replacing the selected cell with "X". 
Display the updated matrix.
"""

print()
row1 = ["🧐", "🧐", "🧐"]
row2 = ["🧐", "🧐", "🧐"]
row3 = ["🧐", "🧐", "🧐"]

matrix = [row1, row2, row3]
#print(matrix)
print()
print(f"{row1}, \n{row2}, \n{row3}")

print()
position = input("Select a position to hide your treasure :")

#23
row_number = int(position[0])
col_number = int(position[1])

row_selected = matrix[row_number - 1]
row_selected[col_number - 1] = "X"
print()
print(f"We are hiding your treasure at your preferred location: \n{row1}, \n{row2}, \n{row3}")
