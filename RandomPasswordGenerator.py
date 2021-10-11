import random
import string

def passwordGenerator(passwordLength = 8):
    allChars = string.ascii_letters + string.digits + string.punctuation
    temp = random.sample(allChars, passwordLength)
    return ''.join(temp)

passwordLength_ = int(input("What is the Password Length: "))
print("Your Password is", passwordGenerator(passwordLength_))
