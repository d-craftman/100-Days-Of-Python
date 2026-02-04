# Project: Secure Input Masking Utility
# Studio: The Craftroom Studios
# Author: Areo Jeremiah

username = input('Username: ')
password = input('Password: ')

# Logic: Calculate length and generate mask
password_length = len(password)
hidden_password = '*' * password_length

print(f"Welcome, {username}. Your password {hidden_password} is {password_length} characters long.")