class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# Creating a user instance
user1 = User("dilip", "dilip@example.com")

# Accessing attributes
print("Username:", user1.username)
print("Email:", user1.email)
