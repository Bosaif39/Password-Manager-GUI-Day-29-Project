from tkinter import * 
from tkinter import messagebox  
from random import choice, randint, shuffle  
import pyperclip  

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """
    Generates a random password that includes a mix of letters, numbers, and symbols.
    - Password length: 8 to 10 letters
    - Symbol count: 2 to 4 symbols
    - Number count: 2 to 4 numbers
    The generated password is displayed in the password entry field and copied to the clipboard.
    """
    # Define character sets for password generation
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random sections for the password using list comprehension 
    password_letters = [choice(letters) for _ in range(randint(8, 10))]  
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]  
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]  

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Join the list of characters into a single string to form the password
    password = "".join(password_list)
    # Insert the generated password into the password entry field
    password_entry.insert(0, password)
    # Copy the generated password to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # Check if website and password fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        
    else:
        # Show a confirmation dialog before saving the data
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            # Append the data to the 'data.txt' file
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                # Clear the entry fields after saving
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")  
window.config(padx=50, pady=50)  

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")  
canvas.create_image(100, 100, image=logo_img)  
canvas.grid(row=0, column=1)  

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)  

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)  

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)  

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)  
website_entry.focus()  # Focus on the website entry field when the window is opened

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)  
email_entry.insert(0, "angela@gmail.com")  

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)  

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)  

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)  

window.mainloop()
