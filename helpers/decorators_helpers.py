


def is_email_valid(func):
    def wrapper(email, y, a, z):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper



def is_number_valid(func):
    def wrapper(first_name, last_name, email, phone):
        if len(phone)==10:
            print("ok")
            if "0" in email[0]:
                func(first_name, last_name, email, phone)

        else: print("No!")
    return wrapper

