# **Password Manager GUI**

## **Overview:**
This is the Day 29 project from the 100 Days of Code: The Complete Python Pro Bootcamp.

This is a Python-based Password Manager application that helps users securely store and manage their passwords locally. The app allows users to save login credentials for different websites, including the website name, email/username, and password. It also includes a password generator to create strong passwords with ease.

## **How It Works:**
1. Enter the **Website name** where you need to store login details.
2. Enter the **Email/Username** associated with the account.
3. Enter the **Password** (or use the **Generate Password** button to automatically create one).
4. Click **Add** to save the credentials to a **txt**, **csv** and **json** files.
5. A **Generate Password** button will create a random, secure password with a mix of letters, numbers, and symbols and **automatically copy it to your clipboard**.
6. The **Add** button saves the credentials in the files named `passwords.txt`, `passwords.csv`, `passwords.json` and clears the fields for the next entry.
7. The **Search** button will find the passwords if exist, otherwise it will display an error message.

## **Features:**
- **Password Generator** 
- **Save Credentials** 
- **Simple UI**
- **Save the data in txt, csv and json files**
- **Search for passwords**
   
## **Example:**
![alt text](https://github.com/Bosaif39/example-pics/blob/main/D_27tt.png?raw=true)

## **Requirements:**
* Python 3.x
* `tkinter` (pre-installed with Python)
* `random` (for generating random passwords)
* `pyperclip` (can be installed via `pip install pyperclip`)
* `json`
* `pandas`
* `os`
* **Image**: An image file `logo.png` for the app's logo (ensure it is in the same directory as the script).
