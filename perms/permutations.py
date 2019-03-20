def numOfPerm(string):
    """Input a [string] into this function and it will
       output the number of different combinations that
       are possible to make with it. Assumes that there
       are no double-ups of letters. Returns an integer.
        - By GIHS RPC"""
    string = str(string)
    multip = [1]
    ans = 1
    for i in range(len(string)):
        multip.append((len(string)-i))
    for thing in multip:
        ans = ans*thing
    return ans
