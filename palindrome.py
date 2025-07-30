def is_palindrome(text: str) -> bool:
    # Remove non-alphanumeric characters and convert to lowercase
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print("It's a palindrome!")
    else:
        print("Not a palindrome.")
