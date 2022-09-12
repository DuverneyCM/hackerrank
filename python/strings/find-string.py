# input:
# ABCDCDC
# CDC

# output: 
# 2

def count_substring(string, sub_string):
    count = 0
    lenSS = len(sub_string)
    for i in range( len(string[:-lenSS]) + 1 ):
        #print( string[i:i+len(sub_string)] )
        if (string[i:i+lenSS] == sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)