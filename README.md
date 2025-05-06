# **Password Manager GUI**

## **Overview:**
This is the Day 29 project from the 100 Days of Code: The Complete Python Pro Bootcamp.

This is a Python-based Password Manager application that helps users securely store and manage their passwords locally. The app allows users to save login credentials for different websites, including the website name, email/username, and password. It also includes a password generator to create strong passwords with ease.

## **How It Works:**
1. Enter the **Website name** where you need to store login details.
2. Enter the **Email/Username** associated with the account.
3. Enter the **Password** (or use the **Generate Password** button to automatically create one).
4. Click **Add** to save the credentials to a txt and csv files.
5. The app will display a confirmation message with the details you've entered.
6. A **Generate Password** button will create a random, secure password with a mix of letters, numbers, and symbols and **automatically copy it to your clipboard**.
7. The **Add** button saves the credentials in a two files named `passwords.txt`, `passwords.csv` and clears the fields for the next entry.

## **Features:**
- **Password Generator** 
- **Save Credentials** 
- **Simple UI**
- **Save the data in txt and csv files**
   
## **Example:**
![alt text](https://raw.githubusercontent.com/Bosaif39/example-pics/refs/heads/main/D_29.png?token=GHSAT0AAAAAADDL7KRAPB7UAPDWSBVEGT3G2AZU4HA)

## **Requirements:**
- Python 3.x
- Tkinter (pre-installed with Python)
- Pandas
- Pyperclip (can be installed via pip: `pip install pyperclip`)
- An image file `logo.png` for the app's logo (make sure to place it in the same directory as the script).
