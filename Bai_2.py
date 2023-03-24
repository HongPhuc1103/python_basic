def count_lowercase_uppercase(string):
    num_lowercase = 0
    num_uppercase = 0

    for char in string:
        if char.islower():
            num_lowercase += 1
        elif char.isupper():
            num_uppercase += 1

    return (num_lowercase, num_uppercase)

user_input = input("Enter a string: ")

num_lowercase, num_uppercase = count_lowercase_uppercase(user_input)

print(f"Number of lowercase characters: {num_lowercase}")
print(f"Number of uppercase characters: {num_uppercase}")
