# age: int
# name: str
# height: float
# is_human: bool

#                               TYPE HINT
# Określenie "age" jako "int" or określenie typ wartości jaki ma wyjś z funkcji na "bool"
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(19):
    print("You may Pass")
else:
    print("Pay a fine ")





