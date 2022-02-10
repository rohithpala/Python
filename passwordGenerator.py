from random import sample
import string


def passwordGenerator(passwordLength=8):
    allChars = string.ascii_letters + string.digits + string.punctuation
    return "".join(sample(allChars, passwordLength))


if __name__ == "__main__":
    passwordLength_ = int(input("What is the Password Length: "))
    print("Your Password is", passwordGenerator(passwordLength_))
    