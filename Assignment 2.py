#Assignment 2
#Name: CHOO YONG HAN


string = "hello"

OtherString = {}

for i in string:
    if i in OtherString:
        OtherString[i] += 1 
    else:
        OtherString[i] = 1 

print("Number of occurrences of each character :\n" + str(OtherString))