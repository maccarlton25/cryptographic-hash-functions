import hashlib, string, random

def evenify(value1, value2): # adds leading 0's if two string values are not equal
    diff= len(value1) - len(value2)
    if(diff < 0):
        value1 = "0"*(-diff) + value1
    if(diff > 0):
        value2 = "0"*(diff) + value2
    return [value1, value2] # returns 'evenified' values as an array

def hammingdistance(val1,val2): # calculates the number of indicies where values don't match
    values = evenify(val1, val2)
    output = sum(va1 != va2 for va1, va2 in zip(values[0], values[1]))
    return output

def generateString(n): # generates a random string with length of n
    all_characters = string.hexdigits
    newstring = ''
    for x in range(0,n): 
        newstring = newstring + random.choice(all_characters)
    return newstring

def find_collision(n): # finds two random strings that generate sha256 hash values that match for the first n didgets 
    string1 = generateString(n*2)
    hash1 = hashlib.sha256(string1).digest().encode('hex')[:n*2]
    string2 = generateString(n*2)
    hash2 = hashlib.sha256(string2).digest().encode('hex')[:n*2]
    while hammingdistance(hash1, hash2) > 0 : 
        string1 = generateString(n*2)
        hash1 = hashlib.sha256(string1).digest().encode('hex')[:n*2]
        string2 = generateString(n*2)
        hash2 = hashlib.sha256(string2).digest().encode('hex')[:n*2]
    return (string1, string2) # returns values as a tuple

