import random


def function_jack():
    if random.random() <= 4/52:
        return "Jack"
    else:
        return "Jack is not here now :("


def function_king():
    if random.random() <= 4/52:
        return "King"
    else:
        return "King is not here now :("


def function_king_or_jack():
    if random.random() <= 8/52:
        return "King or Jack"
    else:
        return "King or Jack is not here now :("


def function_king_and_jack():
    if random.random() <= (4/52)*(4/52):
        return "King and Jack"
    else:
        return "King and Jack is not here now :("


def jack_king_or_6_or_king():
    if random.random() <= (4/52)*3:
        return "King or Jack or 6"
    else:
        return "King or Jack or 6 is not here now :("


def function_heart_or_jack():
    if random.random() <= 16/52:
        return "Heart or Jack"
    else:
        return "Heart or Jack is not here now :("


def function_heart_and_jack():
    if random.random() <= (4/52)*(12/52):
        return "Heart and Jack"
    else:
        return "Heart and Jack is not here now :("


def function_heart_and_jack_or_6():
    if random.random() <= (11/52)*((4/52)+(4/52)):
        return "Heart and (Jack or 6)"
    else:
        return "Heart and (Jack or 6) is not here now :("


def function_heart_and_jack_and_6():
    if random.random() <= (11/52)*(4/52)*(4/52):
        return "Heart and Jack and 6"
    else:
        return "Heart and Jack and 6 is not here now :("


print(function_jack())
print(function_king())
print(function_king_or_jack())
print(function_king_and_jack())
print(jack_king_or_6_or_king())
print(function_heart_or_jack())
print(function_heart_and_jack())
print(function_heart_and_jack_or_6())
print(function_heart_and_jack_and_6())
