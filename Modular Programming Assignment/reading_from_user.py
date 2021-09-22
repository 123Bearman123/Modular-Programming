def read_between_and3(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = int(input(prompt))
            if 1 <= number <= 3:
                something_is_wrong = False
            else:
                print("Between 1 and 3...")
        except:
            print("Must be numeric...")
    return number


def read_nonempty_alphabetical_string(prompt):
    something_is_wrong = True
    while something_is_wrong:
        s = input(prompt)
        copy_without_spaces = s.replace(" ", "")
        if len(s) > 0 and copy_without_spaces.isalpha():
            something_is_wrong = False
        else:
            print("Letters only please...")
    return s


def read_nonnegative_integer(prompt):
    something_is_wrong = True
    while something_is_wrong:
        try:
            number = int(input(prompt))
            if number >= 0:
                something_is_wrong = False
            else:
                print("Non-negative numbers please...")
        except:
            print("Must be numeric...")
    return number