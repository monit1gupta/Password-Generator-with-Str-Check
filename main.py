#Password Generator
import random
import math

stringLetters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
stringNumbers = '0123456789'
stringSymbols = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
#Generate a random password
def passGen(strLen):
  a = random.randint(0, strLen)
  b = random.randint(0, (strLen - a))
  c = strLen - a - b
  letters = ''
  numbers = ''
  symbols = ''
  while a != 0:
    letters += random.choice(stringLetters)
    a -= 1
  while b != 0:
    numbers += random.choice(stringNumbers)
    b -= 1
  while c != 0:
    symbols += random.choice(stringSymbols)
    c -= 1
  return(letters + numbers + symbols)

#Check strength of the pass
def passEntropyCalc(pwd):
  #calculate password entropy
  r = 1
  l = len(pwd)
  E = 0
  hasLowercase = False
  hasUppercase = False
  hasNumbers = False
  hasSymbols = False
  #find if string is all lowercase, all uppercase, lowercase and uppercase
  for j in pwd:
    if j in stringLetters[0:27]:
      hasLowercase = True
    if j in stringLetters[26:]:
      hasUppercase = True
    if j in stringNumbers[:]:
      hasNumbers = True
    if j in stringSymbols[:]:
      hasSymbols = True

  r1 = 0
  r2 = 0
  r3 = 0
  if hasNumbers == True:
    r1=10
  if hasLowercase == True or hasUppercase == True:
    r2=26
  if hasSymbols == True:
    r3=32
  if hasLowercase == True and hasUppercase == True:
    r2=52
  r = r1+r2+r3
  E = math.log2(r**l)
  return E

def printStrength(e):
  if e <28:
    print("Password is very weak; might keep out family members")
  elif e>=28 and e < 35:
    print("Password is Weak; should keep out most people, often good for desktop login passwords")
  elif e>=35 and e < 59:
    print("Password is Reasonable; fairly secure passwords for network and company passwords")
  elif e>=60 and e < 127:
    print("Password is Strong; can be good for guarding financial information")
  else:
    print("Password is Very Strong; often overkill")



##DRIVER
#Ask user choice
print("Welcome to the password generator and strength checker, would you like to create a password or strength the check of your password?")
print("Enter 1 to generate and 2 to enter your own password")

while True:
  choiceFlag = input()
  if(choiceFlag in ('1','2')):
    print("Ok!")
    break
  print("that is not an option sorry!")
if choiceFlag == '1':
  print("How long would you like the password to be?")
  passLen = input()
  #generate pass
  print("Here's your password")
  pwdGen = passGen(int(passLen))
  print(pwdGen)
  #calculateEntropy
  passEntropy = passEntropyCalc(pwdGen)
  printStrength(passEntropy)

else:
  print("Please enter your password")
  userPass = input()
  passEntropy = passEntropyCalc(userPass)
  printStrength(passEntropy)

print("Thank you for using the password generator and strength checker")