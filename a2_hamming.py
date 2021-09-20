def hextobinary (value): # converts a hex string to binary
    print ("hex: ", value) 
    res = bin(int(value, 16)).zfill(8)[2:]
    print ("binary: ", str(res)) 
    return res

def evenify(value1, value2): # takes in two binary values, making sure they are of equal length, adding values if not
    diff= len(value1) - len(value2)
    if(diff < 0):
        value1 = "0"*(-diff) + value1
    if(diff > 0):
        value2 = "0"*(diff) + value2
    return [value1, value2]

def hammingdistance(hex1,hex2): # calculates the number of positions where the binary values do not match between two hex strings 
    one = hextobinary(hex1)
    two = hextobinary(hex2)
    onetwo = evenify(one, two)
    output = sum(val1 != val2 for val1, val2 in zip(onetwo[0], onetwo[1]))
    print ("distance", str(output))
    return output 