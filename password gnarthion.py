import random

input = input("Please enter the number of characters in your password 6 or 9 or 12    :")

caracter = ("A","B" ,"C" ,"D" ,"E" ,"F" ,"G" ,"H" ,"I" ,"J" ,"K" ,"L" ,"M" ,"N" ,"O" ,"P" ,"Q" ,"R" ,"S" ,"T" ,"U" ,"V" ,"W" ,"X" ,"Y" ,"Z")

smal_car = ("a","b" ,"c" ,"d" ,"e" ,"f" ,"g" ,"h" ,"i" ,"j" ,"k" ,"l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" ,"z")

numb = ("0","1","2","3","4","5","6","7","8","9")

all_car = caracter + smal_car + numb

if input == "6":
    password_len = 6

    password = [random.choice(all_car) for _ in range(password_len)]

    output = ''.join(password)

    print(f"Your password is: {output}")

elif input == "9":
    password_len = 9

    password = [random.choice(all_car) for _ in range(password_len)]

    output = ''.join(password)

    print(f"Your password is: {output}")

elif input == "12":
    password_len = 12

    password = [random.choice(all_car) for _ in range(password_len)]

    output = ''.join(password)

    print(f"Your password is: {output}")

else:
    print("your choice is not true")

    TOKEN: Final = "6612038003:AAEcAnlNksa7XN3QFWwA7y_W59P4ubMtGbQ"
    BOT_USERNAME: Final = "@im_passbot"