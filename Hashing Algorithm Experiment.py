# Hashing Algorithm Experiment

import math
import secrets
import string

plainTxt = input("What would you like to hash? ")
saltedPlainTxt = ''
hashedParameter = 0
orderValue = 0
hashedResult = []
newHashOrder = []
finalHash = ''

# Generate and add salt
def generateSalt():
    global saltedPlainTxt, plainTxt, salt
    for i in range(1):
        salt = (
        "".join(
            secrets.choice(
            string.punctuation
            + string.digits
            + string.ascii_lowercase
            + string.ascii_uppercase
            )
            for i in range(14)
        )
        )
    saltedPlainTxt = plainTxt + salt
    print('Salted Password: ' + saltedPlainTxt)
    return saltedPlainTxt

# Convert hash to ASCII and then to binary
def binaryConverter():
    global saltedPlainTxt
    for c in saltedPlainTxt:
        saltedPlainTxt = ord(c)
        saltedPlainTxt = bin(saltedPlainTxt)[2:].zfill(8)
        hashedResult.append(saltedPlainTxt)

# Generate number to pad hash
def hashPadValue():
    global hashedParameter
    hashedParameter = list(map(int, hashedResult))
    hashedParameter = sum(hashedParameter)
    for i in range(2):
        hashedParameter = hashedParameter ** 4 + 16
        hashedParameter = hashedParameter / 262144

# Reduce size of the hashParameter and append it
def appendHash():
    global hashList, hashedResult
    hashSqrt = int(math.sqrt(hashedParameter))
    print(hashSqrt)
    hashList = [a for a in str(hashSqrt)]
    for c in hashList:
        hashList = ord(c)
        hashList = bin(hashList)[2:].zfill(8)
        hashedResult.append(hashList)

# Trim hash to 64 items to get 512 bits
def trimHash():
    global hashedResult
    hashedResult = hashedResult[:65]

# Alter binary character values
def alterHash():
    global hashedResult
    hashedResult[0::2] = ['{0}{1}{2}{3}1{5}{6}{7}'.format(*binaryUnit) for binaryUnit in hashedResult[0::2]]
    hashedResult[0::9] = ['{0}{1}1{3}{4}{5}{6}{7}'.format(*binaryUnit) for binaryUnit in hashedResult[0::9]]
    hashedResult[1::4] = ['{0}{1}{2}{3}{4}{5}0{7}'.format(*binaryUnit) for binaryUnit in hashedResult[1::4]]
    hashedResult[2::11] = ['{0}{1}{2}{3}{4}{5}{6}1'.format(*binaryUnit) for binaryUnit in hashedResult[2::11]]
    hashedResult[4::8] = ['{0}{1}{2}{3}{4}0{6}{7}'.format(*binaryUnit) for binaryUnit in hashedResult[4::8]]
    hashedResult[5::15] = ['{0}1{2}{3}{4}{5}{6}{7}'.format(*binaryUnit) for binaryUnit in hashedResult[5::15]]
    hashedResult[6::6] = ['{0}{1}{2}1{4}{5}{6}{7}'.format(*binaryUnit) for binaryUnit in hashedResult[6::6]]
    hashedResult[7::7] = ['{0}{1}{2}{3}0{5}{6}{7}'.format(*binaryUnit) for binaryUnit in hashedResult[7::7]]

# Reorder hashedResult
def newOrder():
    global newHashOrder, hashedResult
    newHashOrder = [13, 46, 30, 27, 21, 55, 34, 33, 62, 28, 61, 59, 60, 
    14, 2, 57, 37, 4, 38, 18, 10, 64, 20, 1, 41, 17, 23, 6, 51, 3, 16, 
    24, 43, 11, 53, 52, 48, 49, 5, 42, 12, 50, 36, 44, 63, 58, 47, 35,
    9, 25, 32, 26, 56, 54, 31, 15, 29, 19, 39, 7, 8, 22, 45, 40]
    # Index hashedResult with newOrder list
    hashedResult = [hashedResult[i] for i in newHashOrder]

# Convert binary back to Unicode
def convertToUnicode():
    global hashedResult, finalHash
    for c in hashedResult:
        finalHash += chr(int(c,2))

generateSalt()
binaryConverter()
hashPadValue()
appendHash()
trimHash()
alterHash()
newOrder()
convertToUnicode()
print(hashedResult)
print('Hash: ' + finalHash)
