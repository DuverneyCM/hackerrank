# input: qA2
# output 
"""
True
True
True
True
True
"""

if __name__ == '__main__':
    s = input()
    boolList = [False]*5
    for char in s:
        if char.isalnum(): boolList[0] = True
        if char.isalpha(): boolList[1] = True
        if char.isdigit(): boolList[2] = True
        if char.islower(): boolList[3] = True
        if char.isupper(): boolList[4] = True
        #if all(boolList): break
        
    for i in range(5):
        print( boolList[i] )