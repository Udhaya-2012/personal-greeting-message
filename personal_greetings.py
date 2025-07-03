# personal_greeting.py

def personal_greeting():
    # Step 1: Get input from user
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    favorite_color = input("Enter your favorite color: ")

    # Step 2: Create a personalized message
    message = (
        f"\nHello, {name}! 👋\n"
        f"You are {age} years young and your favorite color is {favorite_color}.\n"
        f"{favorite_color.capitalize()} is such a wonderful color—it reflects your personality beautifully!\n"
        "Have a fantastic day! 🌟"
    )

    # Step 3: Print the message
    print(message)

# Step 4: Run the function
if __name__ == "__main__":
    personal_greeting()
