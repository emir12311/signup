# Sign-Up and Admin Panel 🧾  

I kinda made this a while ago but forgot to post it.. oops 😅

This project is a **Sign-Up and Admin Panel** built with **Python** and **PyQt5**, connected to a local **SQLite** database.  

## How it works  
1. The main window gives two options:  
   - **Sign Up:** Opens a registration form.  
   - **Admin Login:** Opens a password-protected admin panel.  
2. The **Sign-Up Form** collects:  
   - Name, surname, email, and phone number  
   - Gender and date of birth  
3. All data gets stored locally in a SQLite database (`mydatabase.db`).  
4. The **Admin Panel** lets you view all registered users from the database.  
5. Admin access is protected by a hashed password.  

## What I learned while making it    
- **Integrating SQLite3** for local data storage.    
- **Managing multiple UI files** created in Qt Designer.  

## Dependencies  
```bash
pip install pyqt5
```

## Files  
The project includes:  
- `signupwindow.py` → Form app interface 
- `mainwindow.py` → Main app interface  
- `adminwindow.py` → Admin panel interface  
- `signup.py` → The main python file that connects all the interfaces together with the logic  

## Note 📝  
Like my other projects, this is the **first version only**.  
I’m not improving or rewriting it unless it’s a really special project.  
This GitHub is meant to show my growth over time, from my earliest code to whatever I make in the future.
