# module that generates random values
import secrets
# module with a ready made collection of characters
import string

# Concatenation to make sure all letters, digits and punctuation is included
characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

password_length = 0

while password_length<12:
    password_length = int(input("Enter password length (minimum 12 characters):"))
    if password_length<12:
        print("That is not long enough for a secure password.")

# Empty list created
password = []
# Making sure the password has a variety of characters to make it more secure
password.append(secrets.choice(string.ascii_uppercase))
password.append(secrets.choice(string.ascii_lowercase))
password.append(secrets.choice(string.digits))
password.append(secrets.choice(string.punctuation))

# Generates and adds a random character for each position in the password
for i in range(0,password_length-4):
    # choice() is a function in the secrets module that generates a random value in characters
    character=secrets.choice(characters)
    password.append(character)

# Shuffles characters in the list
secrets.SystemRandom().shuffle(password)

# Joins the list items into one string
password_string = "".join(password)
print(f"This is your randomly generated password: {password_string}")