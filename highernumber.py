# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement.

# pseudocode

import tkinter as tk
import random

def show_main_window():
    welcome_frame.pack_forget()
    main_frame.pack()
    
def find_largest():
    numbers = [float(entry_list[i].get()) for i in range(5) if entry_list[i].get()]
    
    if numbers:
        largest = max(numbers)
        result_label.config(text=f"The largest number is: {largest}", font=("Helvetica", 16, "bold"), fg="#20B2AA", bg="#90EE90")
    else:
        result_label.config(text="Please enter at least one number.", font=("Helvetica", 14), fg="#FF0000")
        


# Ask the user to input five numbers
# Input the first number
# Input the second number
# Input the third number
# Input the fourth number
# Input the fifth number
  
def check_largest():
    num1 = float(entry_list[0].get())
    num2 = float(entry_list[1].get())
    num3 = float(entry_list[2].get())
    num4 = float(entry_list[3].get())
    num5 = float(entry_list[4].get())
    find_largest(num1, num2, num3, num4, num5)
    
# Check which number is the largest among the five
# if first number is greater than or equal to second number and first number is greater than or equal to third number and first number is greater than or equal to fourth number and first number is greater than or equal to fifth number:
# Largest number is the first number
    if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
        result_label.config(text=f"Largest number is: {num1}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")
        
# else if second number is greater than or equal to first number and second number is greater than or equal to third number and second number is greater than or equal to fourth number and second number is greater than or equal to fifth number:
# Largest number is the second number
    elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
        result_label.config(text=f"Largest number is: {num2}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")
        
# else if third number is greater than or equal to first number and third number is greater than or equal to second number and third number is greater than or equal to fourth number and third number is greater than or equal to fifth number:
# Largest number is the third number
    elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
        result_label.config(text=f"Largest number is: {num3}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")
        
# else if fourth number is greater than or equal to first number and fourth number is greater than or equal to second number and fourth number is greater than or equal to third number and fourth number is greater than or equal to fifth number:
# Largest number is the fourth number
    elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
        result_label.config(text=f"Largest number is: {num4}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")
        
# else:
# Largest number is the fifth number
    else:
        result_label.config(text=f"Largest number is: {num5}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")
 
        
root = tk.Tk()
root.title("Find the Largest Number")
root.geometry("430x360")

# Welcome Page
welcome_frame = tk.Frame(root, width=430, height=360) 
welcome_frame.pack_propagate(0)  


gradient_image = tk.PhotoImage(file="up.png")
background_label = tk.Label(welcome_frame, image=gradient_image)
background_label.place(relwidth=1, relheight=1)

welcome_label = tk.Label(welcome_frame, text="Hi! Please input five numbers.", font=("Helvetica", 20), bg="white")
welcome_label.pack(pady=110)

continue_button = tk.Button(welcome_frame, text="Continue", command=show_main_window, font=("Helvetica", 16), bg="green", fg="white")
continue_button.pack()

welcome_frame.gradient_image = gradient_image

welcome_frame.pack()


# Main Page
main_frame = tk.Frame(root)

photo = tk.PhotoImage(file="pic.png")
background_label = tk.Label(main_frame, image=photo)
background_label.pack(fill="both", expand=True)

main_frame.pack_forget()

labels = []
entry_list = []

for i in range(5):
    label = tk.Label(main_frame, text=f"Enter number {i+1}:", font=("Helvetica", 14))
    label.pack(pady=10, padx=15)
    labels.append(label)

    entry = tk.Entry(main_frame, font=("Helvetica", 14))
    entry.pack(pady=10, padx=15)
    entry_list.append(entry)

result_label = tk.Label(main_frame, text="", font=("Helvetica", 16))
result_label.pack(pady=10)

# Print the largest number
find_button = tk.Button(main_frame, text="Find Largest", command=find_largest, font=("Helvetica", 14))
find_button.pack(pady=20)

result_label = tk.Label(main_frame, text="", font=("Helvetica", 20))
result_label.pack(pady=10)

root.mainloop()


