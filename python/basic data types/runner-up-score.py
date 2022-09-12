# input: 
# 5
# 2 3 6 6 5

# output:
# 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_without_duplicates = list(dict.fromkeys(arr))
    arr_without_duplicates.sort()
    print(arr_without_duplicates[-2])