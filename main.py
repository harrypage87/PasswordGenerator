import random
import string

#Ask user what the password is for
app = input("Enter the application this password is for: ")

letters = string.ascii_letters  
numbers = string.digits
special = "!?@/$%&*"

#PEnsure atleast 1 of each is picked
password = [
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(numbers),
    random.choice(special),
]

#Fill the rest to make 16 characters
chars = letters + numbers + special
password += [random.choice(chars) for _ in range(16 - len(password))]

#Shuffle so we dont always start lower -> upper -> number -> special
random.shuffle(password)

# Print the result
print(f"Your {app} password is: {''.join(password)}")
