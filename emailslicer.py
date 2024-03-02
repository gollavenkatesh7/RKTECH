#              Task -1
#           EMAIL SLICER


def email_slicer(email):
    # Split the email address into username and domain
    username, domain = email.split('@')

    # Display the output
    print("Input:")
    print(email)
    print("Output:")
    print(f"Your username is {username} & domain is {domain}")


# Example usage
input_email = input("Enter the Email ID: ")
email_slicer(input_email)
