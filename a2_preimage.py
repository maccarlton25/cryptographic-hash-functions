import hashlib, string, random

def hammingdistance(val1,val2): # calculates the number of indicies where values don't match
    output = sum(val1 != val2 for val1, val2 in zip(val1, val2)) # != is used as an xor operator 
    return output
def generateString(n): # generates random string of length n 
    all_characters = string.hexdigits
    newstring = ''
    for x in range(0,n): 
        newstring = newstring + random.choice(all_characters)
    return newstring
def find_preimage(target, n): # generates random hash values until the first n characters match the target hash
    target = target.encode('hex')[:n*2]
    random_string = generateString(n*2)
    random_hash = hashlib.sha256(random_string).digest().encode('hex')[:n*2]
    while hammingdistance(target, random_hash) > 0 : 
        random_string = generateString(n*2)
        random_hash = hashlib.sha256(random_string).digest().encode('hex')[:n*2]
    return random_string # returns the generated string that matches the first n hash values of the target
    
