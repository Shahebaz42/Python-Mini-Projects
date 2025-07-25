#Ramdom Password Generator
import random
import string
val = string.ascii_letters+string.digits+string.punctuation
pass_len = 15
password = ""
for i in range(pass_len):
    password+=random.choice(val)
print("strongly suggested password is:",password)
