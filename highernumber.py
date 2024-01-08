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
    number1 = float(entry_list[0].get())
    number2 = float(entry_list[1].get())
    number3 = float(entry_list[2].get())
    number4 = float(entry_list[3].get())
    number5 = float(entry_list[4].get())


# Check which number is the largest among the five
# if first number is greater than or equal to second number and first number is greater than or equal to third number and first number is greater than or equal to fourth number and first number is greater than or equal to fifth number:
# Largest number is the first number
    if number1 >= number2 and number1 >= number3 and number1 >= number4 and number1 >= number5:
        result_label.config(text=f"Largest number is: {number1}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")
        
# else if second number is greater than or equal to first number and second number is greater than or equal to third number and second number is greater than or equal to fourth number and second number is greater than or equal to fifth number:
# Largest number is the second number
    elif number2 >= number1 and number2 >= number3 and number2 >= number2 and number2 >= number5:
        result_label.config(text=f"Largest number is: {number2}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")
        
# else if third number is greater than or equal to first number and third number is greater than or equal to second number and third number is greater than or equal to fourth number and third number is greater than or equal to fifth number:
# Largest number is the third number
    elif number3 >= number1 and number3 >= number2 and number3 >= number4 and number3 >= number5:
        result_label.config(text=f"Largest number is: {number3}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")
        
# else if fourth number is greater than or equal to first number and fourth number is greater than or equal to second number and fourth number is greater than or equal to third number and fourth number is greater than or equal to fifth number:
# Largest number is the fourth number
    elif number4 >= number1 and number4 >= number2 and number4 >= number3 and number4 >= number5:
        result_label.config(text=f"Largest number is: {number4}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")
        
# else:
# Largest number is the fifth number
    else:
        result_label.config(text=f"Largest number is: {number5}", font=("Helvetica", 16, "bold"), bg="#AEC6CF", fg="#20B2AA")


root = tk.Tk()
root.title("Find the Largest Number")
root.geometry("430x360")

# Welcome Page
welcome_frame = tk.Frame(root, width=430, height=360) 
welcome_frame.pack_propagate(0)  


gradient_image = tk.PhotoImage(file="up.png")
background_label = tk.Label(welcome_frame, image=gradient_image)
background_label.place(relwidth=1, relheight=1)

welcome_label = tk.Label(welcome_frame, text="Hi! Please input five numbers.", font=("Tahoma", 19, "bold"), bg="white")
welcome_label.pack(pady=110)

continue_button = tk.Button(welcome_frame, text="Continue", command=show_main_window, font=("Courier New", 18, "bold"), bg="green", fg="white")
continue_button.pack()


welcome_frame.gradient_image = gradient_image

welcome_frame.pack()


# Main Page
main_frame = tk.Frame(root)

photo = tk.PhotoImage(file="slsl.png")
background_label = tk.Label(main_frame, image=photo)
background_label.place(relwidth=1, relheight=1)

main_frame.pack_forget()  

labels = []
entry_list = []

def check_largest():
    numbers = [float(entry_list[i].get()) for i in range(5) if entry_list[i].get()]
    if numbers:
        largest_index = numbers.index(max(numbers))
        largest = max(numbers)
        
        result_label.config(text=f"Largest number is: {largest}", font=("Tahoma", 16, "bold"), bg="#39FF14", fg="black")
        
        for i, entry in enumerate(entry_list):
            if float(entry.get()) == largest:
                entry.config(bg="#39FF14")  
            
            else:
                entry.config(bg="white") 
    else:
        result_label.config(text="Please enter at least one number.", font=("Helvetica", 14), fg="#39FF14")


for i in range(5):
    label = tk.Label(main_frame, text=f"Enter number {i+1}:", font=("Helvetica", 14))
    label.grid(row=i, column=0, pady=10, padx=15)
    labels.append(label)
    
    entry = tk.Entry(main_frame, font=("Helvetica", 14, ))
    entry.grid(row=i, column=1, pady=10, padx=15)
    entry_list.append(entry)

find_button = tk.Button(main_frame, text="Find Largest", command=check_largest, font=("Helvetica", 14), bg="green", fg="white")
find_button.grid(row=5, columnspan=2, pady=20)

result_label = tk.Label(main_frame, text="", font=("Helvetica", 20))
result_label.grid(row=7, columnspan=2)


root.mainloop()
