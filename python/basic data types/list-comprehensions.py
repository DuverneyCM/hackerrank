#input: 1 1 1 2

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    """
    perm = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                #print([i,j,k])
                if i+j+k != n:
                    perm.append([i,j,k])
    """
    perm = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(perm)
