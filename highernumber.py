# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

# pseudocode
import tkinter as tk
import random
root = tk.Tk()
root.title("Input Five Numbers")

labels = []
entry_list = []

# Ask the user to input five numbers
# Input the first number
# Input the second number
# Input the third number
# Input the fourth number
# Input the fifth number
for i in range(5):
    label = tk.Label(root, text=f"Enter number {i+1}:", font=("Helvetica", 14))
    label.grid(row=i, column=0, pady=10, padx=15)
    labels.append(label)

    entry = tk.Entry(root, font=("Helvetica", 14))
    entry.grid(row=i, column=1, pady=10, padx=15)
    entry_list.append(entry)

root.mainloop()



# Check which number is the largest among the five
# if first number is greater than or equal to second number and first number is greater than or equal to third number and first number is greater than or equal to fourth number and first number is greater than or equal to fifth number:
# Largest number is the first number
# else if second number is greater than or equal to first number and second number is greater than or equal to third number and second number is greater than or equal to fourth number and second number is greater than or equal to fifth number:
# Largest number is the second number
# else if third number is greater than or equal to first number and third number is greater than or equal to second number and third number is greater than or equal to fourth number and third number is greater than or equal to fifth number:
# Largest number is the third number
# else if fourth number is greater than or equal to first number and fourth number is greater than or equal to second number and fourth number is greater than or equal to third number and fourth number is greater than or equal to fifth number:
# Largest number is the fourth number
# else:
# Largest number is the fifth number

# Print the largest number




