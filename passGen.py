import random
import string


def passwordGen(length, num=False, strength='Weak'):
    """length of password,
    num if want a number,
    strength(weak,strong,very) """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    letter = lower + upper
    punctuation = string.punctuation
    pwd = ''
    if strength == 'Weak':
        if num:
            length -= 2
            for _ in range(2):
                pwd += random.choice(digits)
        for _ in range(length):
            pwd += random.choice(lower)
    elif strength == 'Strong':
        if num:
            ran = random.randint(0, length//3)
            length -= ran
            for _ in range(ran):
                pwd += random.choice(digits)
            for _ in range(length):
                pwd += random.choice(letter)
    elif strength == 'Very Strong':
        ran = random.randint(0, length//2)
        if num:
            length -= ran
            for _ in range(ran):
                pwd += random.choice(digits)
        length -= ran
        for _ in range(ran):
            pwd += random.choice(punctuation)
        for _ in range(length):
            pwd += random.choice(letter)
    pwd = list(pwd)
    random.shuffle(pwd)
    passwrd = ''.join(pwd)
    return passwrd


# print(passwordGen(5, False, 'Very Strong'))
