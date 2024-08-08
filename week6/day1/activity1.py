#using this list write a program which checks each item . and states if it a thruth or falsy value

truthy_or_falsy = [0, "Hello", "", "!!", 12, True, None, "", 0, False, "False"]


def check_truthy_or_falsy(item):
    return bool(item)


for item in truthy_or_falsy:
    result = "truthy" if check_truthy_or_falsy(item) else "falsy"
    print(f"The value {repr(item)} is {result}.")

