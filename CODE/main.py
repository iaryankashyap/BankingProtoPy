from os import system
from time import sleep

def encrypt(text, key="ZXCVMNBLKJFGHDSAQWEYTRUIOP"):
    '''Encrypts the normal text as per the key'''
    if len(key) != 26 or key.isupper() == False or isstring(text) == False:
        print("KeyError: Key is not valid")
        return
    else:
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cipher_text = ""
        key_list = list(key)
        normal_list = list(normal)
        new_plain = text.upper()

        for i in range(len(new_plain)):
            if new_plain[i].isalpha():
                index = normal_list.index(new_plain[i])
                cipher_text = cipher_text + key_list[index]
            else:
                cipher_text = cipher_text + new_plain[i]
        return cipher_text


def decrypt(text, key="ZXCVMNBLKJFGHDSAQWEYTRUIOP"):
    '''Decrypts the encrypted text as per the key'''

    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain_text = ""
    key_list = list(key)
    normal_list = list(normal)
    new_plain = text.upper()
    if len(key) != 26 or key.isupper() == False or isstring(text) == False:
        print("KeyError: Key is not valid")
        return
    else:
        for i in range(len(text)):
            if new_plain[i].isalpha():
                index = key_list.index(new_plain[i])
                plain_text = plain_text + normal_list[index]
            else:
                plain_text = plain_text + new_plain[i]
        return plain_text


def phonecheck(phone):
    if len(phone)==10:
        return True
    else:
        return False

def register(username,password):

    '''SQL Queries to add entries to the SQL table for username and password, 
    just add the username and password entered by user to the sql table'''

    print("Hello,\nWelcome to Banking portal.")

def passwordchecker(username,password):
    '''Just write query to fetch username and balance from sql table
    and compare it with the username and password entered by the user'''


def portallogged(username):
    print("Logged in successfully")
    sleep(1)
    system("cls")
    print("Hello",username,"welcome")
    inp=1
    c=0
    while c==0: 
        print("What you want to do?")
        print("[1] Withdraw Money")
        print("[2] Deposit Money")
        print("[3] Check Balance")
        p=int(input("Enter your choice:"))
        sleep(1)
        system('cls')
        if p==1:
            deduct=float(input("Enter Amount to WIthdraw:"))
            #SQL QUERY TO UPDATE BALANCE (BALANCE-deduct)
            newbalance = #SQL QUERY TO FETCH NEW BALANCE
            print("Withdraw Success! New Balance:", newbalance)
        elif p==2:
            deposit=float(input("Enter Amount to Deposit:"))
            #SQL QUERY TO UPDATE BALANCE (BALANCE+deduct)
            newbalance = #SQL QUERY TO FETCH NEW BALANCE
            print("Deposit Success! New Balance:", newbalance)

        elif p==2:
            balance= #SQL QUERY TO FETCH NEW BALANCE
            print("Your Balance is : ", balance)
        else:
            print("Invalid input")
            continue

#__MAIN__
   
sleep(1)
n=input("Press enter to continue..")
system("cls")
print("[1] Login")
print("[2] Sign up")
print("[3] Quit")
entry=int(input("Enter Your Choice:"))

#Output Customization

system("cls")
print("Processing")
sleep(1)
system("cls")
print("Processing.")
sleep(1)
system("cls")
print("Processing..")
sleep(1)
system("cls")

#LOOP

a=2
while a==2:
    if entry==1:
        username=input("Enter Your Username:")
        password=decrypt(input("Enter Your Password:"))
        if passwordchecker(username,password):
             portallogged(username)   
             break
        else:
            print("Wrong Credentials")
            sleep(1)
            system("cls")
            continue      
    if entry==2:
        name=input("Enter Your Name:")
        phone=input("Enter Your Phone:")
        if phonecheck(phone)==False:
            print("Invalid input")
            sleep(1)
            continue
        email=input("Enter Your Email Id:")
        username=input("Enter a Username:")
        password=input("Enter a Password:")
        conps=input("Confirm Password:")
        if conps!=password:
            password=encrypt(password)
            print("Passwords Doesn't match")
            sleep(2)
            system("cls")
            
                
        else:
            print("Registered Sucessfully")
            register(username,password) 
            continue  
    if entry==3:
        break
    else:
        print("Invalid Input")
        continue

#HOLDING THE OUTPUT

f=input()