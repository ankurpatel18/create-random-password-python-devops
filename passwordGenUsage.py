#!/usr/local/bin/python3

from passwordGeneratorModule import createNewPassword

newMinLen = input("Insert Minimum length for password ")
newMaxLen = input("Insert Maximum length for password ")

if newMinLen == '':
    print("Will use default password length minimum 8")
    newMinLen = 8

if newMaxLen == '':
    print("Will use default password length maximum 16 ")
    newMaxLen = 16
    
newPassword = createNewPassword(int(newMinLen), int(newMaxLen))

print("Your New Passwod is :", newPassword)
print("New Password Length :", len(newPassword))