import random
import string

def generate_password(length, complexity):
    characters = ''
    
    if complexity == 'low':
        characters += string.ascii_lowercase
    elif complexity == 'medium':
        characters += string.ascii_letters + string.digits
    elif complexity == 'high':
        characters += string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user for password length and complexity
    length = int(input("Enter the desired password length: "))
    
    print("Select complexity level:")
    print("1. Low (only lowercase letters)")
    print("2. Medium (letters and digits)")
    print("3. High (letters, digits, and special characters)")
    
    complexity_option = input("Choose an option (1, 2, or 3): ")
    
    complexity_map = {
        '1': 'low',
        '2': 'medium',
        '3': 'high'
    }
    
    complexity = complexity_map.get(complexity_option, 'low')
    
    # Generate and display the password
    password = generate_password(length, complexity)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
