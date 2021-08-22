#Project
#Name: CHOO YONG HAN


import random
import string

ID = ""
characters_list = list(string.ascii_letters + string.digits)

for i in range(6):
  ID += random.choice(characters_list)

print("6 character OTP is: ", ID)