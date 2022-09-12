def incr_char(character, n):
    return chr(ord(character) + n)

def print_rangoli(size):
    # your code goes here
    H = 2*(size-1) + 1
    W = 4*(size-1) + 1
    listChr = [chr(i) for i in range(ord('a'), ord('a')+size)]
    #listChr.reverse()

    for i in range(H):
        subList1 = listChr[abs(size - 1 - i):]
        subList2 = listChr[abs(size - 1 - i):]
        subList2.reverse()
        subList2.pop()
        subList = subList2 + subList1
        c = "-".join(subList)
        print(c.center(W,'-'))
        #print(c)
    
    """
    width = 4*(size - 1) + 1
    height = 2*(size - 1) + 1
    for i in range(height):
        rel_pos_center_V = abs(i + 1 - size)
        code_pos_V = size - rel_pos_center_V - 1
        # print(code_pos_V)
        txt = ""
        for j in range(width):            
            if j % 2 == 0:
                rel_pos_center_H = abs(j//2 + 1 - size)
                code_pos_H = code_pos_V - rel_pos_center_H
                if code_pos_H >= 0:
                    txt += incr_char('a', size - code_pos_H - 1) # str(code_pos_H)
                else:
                    txt += "-"
            else:
                txt += "-"
        print(txt)
    """
    
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)