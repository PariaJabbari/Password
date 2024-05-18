from os import system


while True:

    char_upper = False
    char_lower = False
    char_digit = False
    char_punctuation = False
    char_other = False
    password_len = True

    # Get user's password
    user_password = input("\nChoose a password for your profile.\
                        \n\nQualifications:\
                        \nThe password you enter should contain:\
                        \n\n\U0001F506 1. Uppercase Letters\
                        \n\U0001F506 2. Lowercase Letters\
                        \n\U0001F506 3. Numbers\
                        \n\U0001F506 4. Punctuations\
                        \n\U0001F506 5. At least 8 characters\n ")
    system("cls")

    # region check if the password matches the conditions
    for char in user_password:
        if char.isupper():
            char_upper = True
        elif char.islower():
            char_lower = True
        elif char.isdigit():
            char_digit = True
        elif 33 <= ord(char) <= 47 or 58 <= ord(char) <= 64 or 91 <= ord(char) <= 96 or 123 <= ord(char) <= 126:
            char_punctuation = True
        else:
            char_other = True
    # endregion

    # region result
    if not char_upper:
        print("\u274c The password should have at least 1 uppercase letter.")
    else:
        print("\u2714 The password should have at least 1 uppercase letter.")
    if not char_lower:
        print("\u274c The password should have at least 1 lowercase letter.")
    else:
        print("\u2714 The password should have at least 1 lowercase letter.")
    if not char_digit:
        print("\u274c The password should have at least 1 number.")
    else:
        print("\u2714 The password should have at least 1 number.")
    if not char_punctuation:
        print("\u274c The password should have at least 1 punctuation.")
    else:
        print("\u2714 The password should have at least 1 punctuation.")
    if len(user_password) < 8:
        password_len = False
        print("\u274c The password should have at least 8 characters.")
    else:
        print("\u2714 The password should have at least 8 characters.")
    if char_other:
        print("\u274c The password should just contain:\
            \n   1. Uppercase Letters\
            \n   2. Lowercase Letters\
            \n   3. Numbers\
            \n   4. Punctuations")
    else:
        print("\u2714 The password should just contain:\
            \n   1. Uppercase Letters\
            \n   2. Lowercase Letters\
            \n   3. Numbers\
            \n   4. Punctuations")
    # endregion
        
    # region password confirmation
    if char_upper and char_lower and char_digit and char_punctuation and password_len and not char_other:

        password_confirmation = input("\nPassword Confirmation:\
                                      \n\nEnter the password again.\n\U0001F449")
        system("cls")

        if user_password == password_confirmation:
            print("\033[32mThe password is choosen for your profile.\033[0m ")
            break

        print("\033[91mTwo passwords you entered do not match.\033[0m")
    # endregion
